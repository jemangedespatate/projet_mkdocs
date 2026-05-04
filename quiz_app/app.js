const app = (() => {
    // Game State
    const state = {
        teams: [
            { id: 'cyan', name: 'Equipe #2BFAFA', score: 0 },
            { id: 'rose', name: 'Equipe Rose', score: 0 },
            { id: 'vert', name: 'Equipe Vert', score: 0 },
            { id: 'rouge', name: 'Equipe Rouge', score: 0 }
        ],
        currentTeamIndex: 0,
        availableQuestions: [],
        currentQuestion: null
    };

    // DOM Elements
    const elements = {
        teamsContainer: document.getElementById('teams-container'),
        currentTeamDisplay: document.getElementById('current-team-display'),
        remainingInfo: document.getElementById('remaining-info'),

        // Screens
        stateSelect: document.getElementById('state-select'),
        stateQuestion: document.getElementById('state-question'),
        stateAnswer: document.getElementById('state-answer'),
        stateEnd: document.getElementById('state-end'),

        // Question Screen
        qDiff: document.getElementById('q-diff'),
        qAuthor: document.getElementById('q-author'),
        qEnonce: document.getElementById('q-enonce'),

        // Answer Screen
        aDiff: document.getElementById('a-diff'),
        aAuthor: document.getElementById('a-author'),
        aEnonce: document.getElementById('a-enonce'),
        aReponse: document.getElementById('a-reponse'),
        ptsWin: document.getElementById('pts-win')
    };

    const getPoints = (diff) => {
        if (diff === 'facile') return 1;
        if (diff === 'moyenne') return 2;
        if (diff === 'difficile') return 3;
        return 1;
    };

    const renderTeams = () => {
        elements.teamsContainer.innerHTML = state.teams.map((t, index) => `
            <div class="team-card ${t.id} ${index === state.currentTeamIndex ? 'active' : ''}">
                <div class="team-name">${t.name}</div>
                <div class="team-score">${t.score} pts</div>
            </div>
        `).join('');

        const currentTeam = state.teams[state.currentTeamIndex];
        elements.currentTeamDisplay.textContent = currentTeam.name;
        elements.currentTeamDisplay.className = `current-team text-${currentTeam.id}`;
    };

    const showScreen = (screenId) => {
        [elements.stateSelect, elements.stateQuestion, elements.stateAnswer, elements.stateEnd].forEach(el => {
            el.classList.remove('active');
        });
        document.getElementById(screenId).classList.add('active');
    };

    const init = () => {
        // Deep copy from questions.js (assumes questionsData is available)
        state.availableQuestions = JSON.parse(JSON.stringify(questionsData));
        renderTeams();
        updateRemainingInfo();
    };

    const updateRemainingInfo = () => {
        const counts = { facile: 0, moyenne: 0, difficile: 0 };
        const currentTeam = state.teams[state.currentTeamIndex];

        state.availableQuestions.forEach(q => {
            if ((q.groupe || "").toLowerCase() === currentTeam.id) {
                if (counts[q.difficulte] !== undefined) counts[q.difficulte]++;
            }
        });

        const total = counts.facile + counts.moyenne + counts.difficile;
        if (total === 0) {
            elements.remainingInfo.innerHTML = `L'équipe n'a plus de questions à poser ! Veuillez passer au tour suivant.`;
        } else {
            elements.remainingInfo.innerHTML = `Questions de l'équipe restantes : <span style="color:var(--diff-facile)">${counts.facile} Faciles</span> | <span style="color:var(--diff-moyenne)">${counts.moyenne} Moyennes</span> | <span style="color:var(--diff-difficile)">${counts.difficile} Difficiles</span>`;
        }
    };

    const renderMarkdown = (text) => {
        return DOMPurify.sanitize(marked.parse(text));
    };

    const drawQuestion = (difficulty) => {
        const currentTeam = state.teams[state.currentTeamIndex];
        let pool = state.availableQuestions.filter(q => (q.groupe || "").toLowerCase() === currentTeam.id);

        if (difficulty !== 'random') {
            pool = pool.filter(q => q.difficulte === difficulty);
        }

        if (pool.length === 0) {
            alert(`Aucune question '${difficulty}' restante pour cette équipe !`);
            return;
        }

        const randomIndex = Math.floor(Math.random() * pool.length);
        state.currentQuestion = pool[randomIndex];

        // Remove from available
        state.availableQuestions = state.availableQuestions.filter(q => q !== state.currentQuestion);

        // Update Question Screen
        elements.qDiff.textContent = state.currentQuestion.difficulte;
        elements.qDiff.className = `badge diff-badge ${state.currentQuestion.difficulte}`;

        let authorTeam = state.currentQuestion.groupe || 'Inconnu';
        let authorName = state.currentQuestion.nom || 'Anonyme';
        elements.qAuthor.innerHTML = `Proposée par : <span>${authorName} (Equipe ${authorTeam})</span>`;

        elements.qEnonce.innerHTML = renderMarkdown(state.currentQuestion.enonce);

        showScreen('state-question');
    };

    const showAnswer = () => {
        // Update Answer Screen
        elements.aDiff.textContent = state.currentQuestion.difficulte;
        elements.aDiff.className = `badge diff-badge ${state.currentQuestion.difficulte}`;

        let authorTeam = state.currentQuestion.groupe || 'Inconnu';
        let authorName = state.currentQuestion.nom || 'Anonyme';
        elements.aAuthor.innerHTML = `Proposée par : <span>${authorName} (Equipe ${authorTeam})</span>`;

        elements.aEnonce.innerHTML = renderMarkdown(state.currentQuestion.enonce);
        elements.aReponse.innerHTML = renderMarkdown(state.currentQuestion.reponse);

        const pts = getPoints(state.currentQuestion.difficulte);
        const authorTeamId = authorTeam.toLowerCase();

        // Generate buttons for eligible teams
        const resolutionActions = document.getElementById('resolution-actions');
        resolutionActions.innerHTML = '';

        state.teams.forEach(t => {
            if (t.id !== authorTeamId) {
                const btn = document.createElement('button');
                btn.className = `btn btn-success`;
                btn.innerHTML = `${t.name} a trouvé ! (+${pts} pts)`;
                btn.onclick = () => {
                    awardPointsToTeam(t.id, pts);
                    btn.disabled = true;
                    btn.style.opacity = '0.5';
                    btn.innerHTML = `${t.name} a trouvé ! (✓)`;
                    
                    const btnNobody = document.getElementById('btn-nobody');
                    if(btnNobody) {
                        btnNobody.disabled = true;
                        btnNobody.style.opacity = '0.5';
                    }
                    
                    const btnPenalize = document.getElementById('btn-penalize');
                    if(btnPenalize) {
                        btnPenalize.disabled = true;
                        btnPenalize.style.opacity = '0.5';
                    }
                };
                resolutionActions.appendChild(btn);
            }
        });

        // Reset nobody button
        const btnNobody = document.getElementById('btn-nobody');
        if (btnNobody) {
            btnNobody.disabled = false;
            btnNobody.style.opacity = '1';
        }

        const btnPenalize = document.getElementById('btn-penalize');
        if (btnPenalize) {
            btnPenalize.disabled = false;
            btnPenalize.style.opacity = '1';
        }

        showScreen('state-answer');
    };

    const awardPointsToTeam = (teamId, points) => {
        const targetTeam = state.teams.find(t => t.id === teamId);
        if (targetTeam) {
            targetTeam.score += points;
            renderTeams(); // Update leaderboard immediately
        }
    };

    const awardPointsToAuthor = () => {
        const authorTeamName = (state.currentQuestion.groupe || "").toLowerCase();
        const targetTeam = state.teams.find(t => t.id === authorTeamName);
        if (targetTeam) {
            targetTeam.score += 1;
            renderTeams();
        } else {
            alert(`Impossible d'attribuer le point, groupe auteur inconnu : ${authorTeamName}`);
        }

        // Disable other buttons
        const btnNobody = document.getElementById('btn-nobody');
        if(btnNobody) {
            btnNobody.disabled = true;
            btnNobody.style.opacity = '0.5';
        }
        
        const btnPenalize = document.getElementById('btn-penalize');
        if(btnPenalize) {
            btnPenalize.disabled = true;
            btnPenalize.style.opacity = '0.5';
        }

        const btns = document.getElementById('resolution-actions').querySelectorAll('.btn-success');
        btns.forEach(b => {
            b.disabled = true;
            b.style.opacity = '0.5';
        });
    };

    const penalizeAuthor = () => {
        const authorTeamName = (state.currentQuestion.groupe || "").toLowerCase();
        const targetTeam = state.teams.find(t => t.id === authorTeamName);
        if (targetTeam) {
            targetTeam.score -= 1;
            renderTeams();
        } else {
            alert(`Impossible d'attribuer la pénalité, groupe auteur inconnu : ${authorTeamName}`);
        }
        
        // Disable other buttons
        const btnNobody = document.getElementById('btn-nobody');
        if (btnNobody) {
            btnNobody.disabled = true;
            btnNobody.style.opacity = '0.5';
        }
        
        const btnPenalize = document.getElementById('btn-penalize');
        if (btnPenalize) {
            btnPenalize.disabled = true;
            btnPenalize.style.opacity = '0.5';
        }
        
        const btns = document.getElementById('resolution-actions').querySelectorAll('.btn-success');
        btns.forEach(b => {
            b.disabled = true;
            b.style.opacity = '0.5';
        });
    };

    const nextTurn = () => {
        state.currentQuestion = null;
        state.currentTeamIndex = (state.currentTeamIndex + 1) % state.teams.length;

        renderTeams();
        updateRemainingInfo();

        if (state.availableQuestions.length === 0) {
            // End Game
            let winner = [...state.teams].sort((a, b) => b.score - a.score)[0];
            document.getElementById('winner-display').innerHTML = `L'${winner.name} gagne avec ${winner.score} pts !`;
            showScreen('state-end');
        } else {
            showScreen('state-select');
        }
    };

    // Public API
    return {
        init,
        drawQuestion,
        showAnswer,
        awardPointsToTeam,
        awardPointsToAuthor,
        penalizeAuthor,
        nextTurn
    };
})();

// Initialize on load
window.addEventListener('DOMContentLoaded', app.init);

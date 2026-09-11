# 📅 Calendrier NSI Terminale

<div id="calendar-app">

<div class="class-selector-bar" id="class-selector-bar">
  <span class="class-selector-label">🏫 Ma classe :</span>
  <div class="class-buttons" id="class-buttons"></div>
</div>

<div class="cal-header">
  <button class="cal-nav" id="prev-btn">&#8249;</button>
  <span class="cal-title" id="cal-title"></span>
  <button class="cal-nav" id="next-btn">&#8250;</button>
</div>

<div class="cal-legend">
  <span class="legend-item"><span class="dot cours"></span> Cours</span>
  <span class="legend-item"><span class="dot devoir"></span> Devoir</span>
  <span class="legend-item"><span class="dot tp"></span> TP</span>
  <span class="legend-item"><span class="dot evaluation"></span> Évaluation</span>
</div>

<div class="cal-grid" id="cal-grid"></div>

<div class="cal-popup" id="cal-popup">
  <div class="cal-popup-inner">
    <button class="popup-close" id="popup-close">✕</button>
    <h3 id="popup-date"></h3>
    <div id="popup-content"></div>
  </div>
</div>

</div>

<style>
#calendar-app {
  font-family: 'Roboto', sans-serif;
  max-width: 900px;
  margin: 0 auto;
  padding: 1rem;
}
.class-selector-bar {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  flex-wrap: wrap;
  background: var(--md-code-bg-color);
  border-radius: 12px;
  padding: 0.75rem 1.2rem;
  margin-bottom: 1.2rem;
}
.class-selector-label {
  font-weight: 700;
  font-size: 0.95rem;
  white-space: nowrap;
}
.class-buttons {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.class-btn {
  padding: 0.35rem 1rem;
  border-radius: 20px;
  border: 2px solid var(--md-primary-fg-color);
  background: transparent;
  color: var(--md-primary-fg-color);
  font-weight: 700;
  font-size: 0.88rem;
  cursor: pointer;
  transition: background 0.18s, color 0.18s;
}
.class-btn:hover,
.class-btn.active {
  background: var(--md-primary-fg-color);
  color: white;
}
.cal-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  margin-bottom: 1rem;
}
.cal-title {
  font-size: 1.5rem;
  font-weight: 700;
  text-transform: capitalize;
  color: var(--md-primary-fg-color);
}
.cal-nav {
  background: var(--md-primary-fg-color);
  color: white;
  border: none;
  border-radius: 50%;
  width: 2.2rem;
  height: 2.2rem;
  font-size: 1.4rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.2s;
}
.cal-nav:hover { opacity: 0.75; }
.cal-legend {
  display: flex;
  gap: 1.2rem;
  justify-content: center;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.85rem;
}
.dot { width: 11px; height: 11px; border-radius: 50%; display: inline-block; }
.dot.cours      { background: #4a9eff; }
.dot.devoir     { background: #ff8c42; }
.dot.tp         { background: #43c67a; }
.dot.evaluation { background: #e05252; }
.cal-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 6px;
}
.cal-day-name {
  text-align: center;
  font-weight: 700;
  font-size: 0.8rem;
  padding: 6px 0;
  color: var(--md-default-fg-color--light);
  text-transform: uppercase;
}
.cal-day {
  min-height: 72px;
  border-radius: 10px;
  padding: 6px;
  cursor: pointer;
  border: 2px solid transparent;
  transition: border-color 0.2s, background 0.2s;
  background: var(--md-code-bg-color);
}
.cal-day:hover       { border-color: var(--md-primary-fg-color); }
.cal-day.empty       { background: transparent; cursor: default; border: none; }
.cal-day.today       { border-color: var(--md-accent-fg-color); }
.day-num { font-weight: 700; font-size: 0.95rem; color: var(--md-default-fg-color); }
.cal-day.today .day-num { color: var(--md-accent-fg-color); }
.event-dots { display: flex; flex-wrap: wrap; gap: 3px; margin-top: 4px; }
.event-chip {
  font-size: 0.65rem;
  padding: 2px 5px;
  border-radius: 4px;
  color: white;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
}
.event-chip.cours      { background: #4a9eff; }
.event-chip.devoir     { background: #ff8c42; }
.event-chip.tp         { background: #43c67a; }
.event-chip.evaluation { background: #e05252; }
.cal-popup {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: 9999;
  align-items: center;
  justify-content: center;
}
.cal-popup.active { display: flex; }
.cal-popup-inner {
  background: var(--md-default-bg-color);
  border-radius: 16px;
  padding: 2rem;
  max-width: 440px;
  width: 90%;
  position: relative;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}
.popup-close {
  position: absolute;
  top: 1rem; right: 1rem;
  background: none; border: none;
  font-size: 1.2rem; cursor: pointer;
  color: var(--md-default-fg-color--light);
}
.popup-close:hover { color: var(--md-primary-fg-color); }
#popup-date {
  margin: 0 0 1rem 0;
  font-size: 1.2rem;
  color: var(--md-primary-fg-color);
  text-transform: capitalize;
}
.popup-section-title {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--md-default-fg-color--light);
  margin: 0.8rem 0 0.4rem;
}
.popup-event {
  display: flex;
  align-items: flex-start;
  gap: 0.7rem;
  padding: 0.7rem;
  border-radius: 10px;
  margin-bottom: 0.5rem;
  background: var(--md-code-bg-color);
}
.popup-event-icon { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; margin-top: 3px; }
.popup-event-icon.cours      { background: #4a9eff; }
.popup-event-icon.devoir     { background: #ff8c42; }
.popup-event-icon.tp         { background: #43c67a; }
.popup-event-icon.evaluation { background: #e05252; }
.popup-event-title  { font-weight: 700; font-size: 0.95rem; }
.popup-event-desc   { font-size: 0.82rem; color: var(--md-default-fg-color--light); margin-top: 2px; }
.popup-empty {
  color: var(--md-default-fg-color--light);
  font-style: italic;
  text-align: center;
  padding: 1rem;
}
</style>

<script>
// ════════════════════════════════════════════════════════════
// ⚙️  CONFIGURATION — modifiez cette section
// ════════════════════════════════════════════════════════════

// Liste des classes (modifiez selon vos groupes)
const CLASSES = ["TA", "TB"];

// Clé localStorage pour mémoriser le choix de l'élève
const STORAGE_KEY = "nsit_classe_choisie";

// ────────────────────────────────────────────────────────────
// 📅 ÉVÉNEMENTS
//
// "all"  → commun à toutes les classes
// "TA"   → spécifique à la classe TA (adapter selon CLASSES)
//
// Format de la date : "YYYY-MM-DD"
// Types : "cours" | "devoir" | "tp" | "evaluation"
// ────────────────────────────────────────────────────────────
const EVENTS = {
  "all": {
    "2026-09-08": [
      { type: "cours", title: "Introduction POO", description: "Rappels Python, notion de classe et objet" }
    ],
    "2026-09-15": [
      { type: "tp", title: "TP POO n°1", description: "Création d'une classe Point et Cercle" }
    ]
  },
  "TA": {
    // Ajoutez les événements spécifiques à TA ici
  },
  "TB": {
    // Ajoutez les événements spécifiques à TB ici
  }
};

// ════════════════════════════════════════════════════════════
// ⛔ NE PAS MODIFIER EN DESSOUS
// ════════════════════════════════════════════════════════════
const MONTHS_FR = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"];
const DAYS_FR   = ["Lun","Mar","Mer","Jeu","Ven","Sam","Dim"];

let currentYear  = new Date().getFullYear();
let currentMonth = new Date().getMonth();
let selectedClass = localStorage.getItem(STORAGE_KEY) || null;

function buildClassSelector() {
  const container = document.getElementById("class-buttons");
  container.innerHTML = "";
  CLASSES.forEach(cls => {
    const btn = document.createElement("button");
    btn.className = "class-btn" + (cls === selectedClass ? " active" : "");
    btn.textContent = cls;
    btn.addEventListener("click", () => {
      selectedClass = cls;
      localStorage.setItem(STORAGE_KEY, cls);
      buildClassSelector();
      render();
    });
    container.appendChild(btn);
  });
}

function getEventsForDate(dateStr) {
  const common   = (EVENTS["all"] && EVENTS["all"][dateStr]) || [];
  const specific = (selectedClass && EVENTS[selectedClass] && EVENTS[selectedClass][dateStr]) || [];
  return [...common, ...specific];
}

function render() {
  const title = document.getElementById("cal-title");
  const grid  = document.getElementById("cal-grid");
  title.textContent = MONTHS_FR[currentMonth] + " " + currentYear;
  grid.innerHTML = "";

  DAYS_FR.forEach(d => {
    const el = document.createElement("div");
    el.className = "cal-day-name";
    el.textContent = d;
    grid.appendChild(el);
  });

  const firstDay = new Date(currentYear, currentMonth, 1).getDay();
  const offset = (firstDay === 0) ? 6 : firstDay - 1;
  const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
  const today = new Date();

  for (let i = 0; i < offset; i++) {
    const el = document.createElement("div");
    el.className = "cal-day empty";
    grid.appendChild(el);
  }

  for (let d = 1; d <= daysInMonth; d++) {
    const dateStr = `${currentYear}-${String(currentMonth+1).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
    const el = document.createElement("div");
    el.className = "cal-day";
    if (d === today.getDate() && currentMonth === today.getMonth() && currentYear === today.getFullYear()) {
      el.classList.add("today");
    }
    const numEl = document.createElement("div");
    numEl.className = "day-num";
    numEl.textContent = d;
    el.appendChild(numEl);

    const evts = getEventsForDate(dateStr);
    if (evts.length > 0) {
      const chipsEl = document.createElement("div");
      chipsEl.className = "event-dots";
      evts.forEach(ev => {
        const chip = document.createElement("span");
        chip.className = "event-chip " + ev.type;
        chip.textContent = ev.title;
        chipsEl.appendChild(chip);
      });
      el.appendChild(chipsEl);
    }

    el.addEventListener("click", () => openPopup(dateStr, d));
    grid.appendChild(el);
  }
}

function openPopup(dateStr, d) {
  const popup   = document.getElementById("cal-popup");
  const dateEl  = document.getElementById("popup-date");
  const content = document.getElementById("popup-content");
  const date    = new Date(currentYear, currentMonth, d);
  dateEl.textContent = date.toLocaleDateString("fr-FR", { weekday:"long", day:"numeric", month:"long", year:"numeric" });

  const common   = (EVENTS["all"] && EVENTS["all"][dateStr]) || [];
  const specific = (selectedClass && EVENTS[selectedClass] && EVENTS[selectedClass][dateStr]) || [];

  if (common.length === 0 && specific.length === 0) {
    content.innerHTML = '<p class="popup-empty">Aucun événement prévu ce jour.</p>';
  } else {
    let html = "";
    if (common.length > 0) {
      html += `<div class="popup-section-title">📌 Toutes les classes</div>`;
      html += common.map(ev => eventCard(ev)).join("");
    }
    if (specific.length > 0) {
      html += `<div class="popup-section-title">🏫 Classe ${selectedClass}</div>`;
      html += specific.map(ev => eventCard(ev)).join("");
    }
    content.innerHTML = html;
  }
  popup.classList.add("active");
}

function eventCard(ev) {
  return `<div class="popup-event">
    <div class="popup-event-icon ${ev.type}"></div>
    <div>
      <div class="popup-event-title">${ev.title}</div>
      <div class="popup-event-desc">${ev.description}</div>
    </div>
  </div>`;
}

document.getElementById("prev-btn").addEventListener("click", () => {
  currentMonth--;
  if (currentMonth < 0) { currentMonth = 11; currentYear--; }
  render();
});
document.getElementById("next-btn").addEventListener("click", () => {
  currentMonth++;
  if (currentMonth > 11) { currentMonth = 0; currentYear++; }
  render();
});
document.getElementById("popup-close").addEventListener("click", () => {
  document.getElementById("cal-popup").classList.remove("active");
});
document.getElementById("cal-popup").addEventListener("click", e => {
  if (e.target === document.getElementById("cal-popup"))
    document.getElementById("cal-popup").classList.remove("active");
});

buildClassSelector();
render();
</script>

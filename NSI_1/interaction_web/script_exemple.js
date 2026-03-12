// Variable pour stocker la valeur du compteur
let compteur = 0;

// Récupérer les éléments HTML
const affichage = document.getElementById("affichage");
const btnIncrementer = document.getElementById("incrementer");
const btnDecrementer = document.getElementById("decrementer");
const btnReinitialiser = document.getElementById("reinitialiser");

// Fonction pour mettre à jour l'affichage
function mettreAJourAffichage() {
    affichage.textContent = compteur;

    // Changer la couleur selon la valeur
    if (compteur > 0) {
        affichage.style.color = "#27ae60"; // Vert
    } else if (compteur < 0) {
        affichage.style.color = "#e74c3c"; // Rouge
    } else {
        affichage.style.color = "#333"; // Gris foncé
    }
}

// Ajouter des écouteurs d'événements
btnIncrementer.addEventListener("click", function () {
    compteur++;
    mettreAJourAffichage();
});

btnDecrementer.addEventListener("click", function () {
    compteur--;
    mettreAJourAffichage();
});

btnReinitialiser.addEventListener("click", function () {
    compteur = 0;
    mettreAJourAffichage();
});

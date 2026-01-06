import csv
import tkinter as tk
from tkinter import messagebox
import os

# ==========================================================
# PARTIE CORRIGÉE (LOGIQUE MÉTIER)
# ==========================================================

def charger_pokemons(nom_fichier):
    """
    Charge les données du fichier CSV et retourne une liste de dictionnaires.
    """
    pokemons = []
    try:
        with open(nom_fichier, mode='r', encoding='utf-8') as fichier:
            lecteur = csv.DictReader(fichier)
            for ligne in lecteur:
                pokemon = {
                    "id": int(ligne["id"]),
                    "nom": ligne["nom"],
                    "type1": ligne["type1"],
                    "type2": ligne["type2"],
                    "pv": int(ligne["pv"]),
                    "attaque": int(ligne["attaque"]),
                    "defense": int(ligne["defense"]),
                    "vitesse": int(ligne["vitesse"]),
                    "special": int(ligne["special"])
                }
                pokemons.append(pokemon)
        return pokemons
    except Exception as e:
        print(f"Erreur chargement : {e}")
        return []

def rechercher_pokemon(nom_recherche, table):
    """
    Recherche un Pokémon par son nom dans la table.
    """
    for p in table:
        if p["nom"].lower() == nom_recherche.lower():
            return p
    return None

def calculer_moyenne_vitesse(table):
    if not table: return 0
    somme = 0
    for p in table:
        somme += p["vitesse"]
    return somme / len(table)

def filtrer_par_type(type_recherche, table):
    resultats = []
    for p in table:
        if p["type1"].lower() == type_recherche.lower() or p["type2"].lower() == type_recherche.lower():
            resultats.append(p["nom"])
    return resultats

# ==========================================================
# PARTIE INTERFACE (PROCÉDURALE)
# ==========================================================

base_de_donnees = []
labels_stats = {}
label_nom = None
label_types = None
label_image = None
photo_pokemon = None

def mettre_a_jour_affichage():
    nom_saisi = entree_nom.get().strip()
    if not nom_saisi: return

    global base_de_donnees, photo_pokemon
    if not base_de_donnees:
        dossier_actuel = os.path.dirname(os.path.abspath(__file__))
        chemin_csv = os.path.join(dossier_actuel, "pokemon.csv")
        base_de_donnees = charger_pokemons(chemin_csv)
        if not base_de_donnees:
            messagebox.showerror("Erreur", "Fichier pokemon.csv introuvable.")
            return

    pokemon = rechercher_pokemon(nom_saisi, base_de_donnees)

    if pokemon:
        label_nom.config(text=f"{pokemon['nom']} (#0{pokemon['id']})", fg="#e3350d")
        t2 = f" / {pokemon['type2']}" if pokemon['type2'] else ""
        label_types.config(text=f"Types : {pokemon['type1']}{t2}")
        for stat in ["pv", "attaque", "defense", "vitesse", "special"]:
            labels_stats[stat].config(text=str(pokemon[stat]))
            
        # Mise à jour du sprite (Dossier 'e' dans le même répertoire)
        try:
            dossier_actuel = os.path.dirname(os.path.abspath(__file__))
            chemin_image = os.path.join(dossier_actuel, "e", f"{pokemon['id']}.png")
            photo_pokemon = tk.PhotoImage(file=chemin_image)
            label_image.config(image=photo_pokemon, text="")
        except:
            label_image.config(image="", text="Image non trouvée")
    else:
        messagebox.showwarning("Inconnu", f"Le Pokémon '{nom_saisi}' n'existe pas.")

# Construction de l'interface
fenetre = tk.Tk()
fenetre.title("Correctif Pokédex NSI")
fenetre.geometry("450x450")
fenetre.configure(bg="#f4f4f4")

tk.Label(fenetre, text="🔴 Pokédex Kanto (Corrigé)", font=("Helvetica", 18, "bold"), bg="#f4f4f4", fg="#e3350d").pack(pady=15)

cadre_recherche = tk.Frame(fenetre, bg="#f4f4f4")
cadre_recherche.pack(pady=10)

tk.Label(cadre_recherche, text="Nom :", bg="#f4f4f4").pack(side="left")
entree_nom = tk.Entry(cadre_recherche)
entree_nom.pack(side="left", padx=5)
entree_nom.bind("<Return>", lambda e: mettre_a_jour_affichage())

btn = tk.Button(cadre_recherche, text="Chercher", command=mettre_a_jour_affichage, bg="#30a7d7", fg="white")
btn.pack(side="left", padx=5)

cadre_resultat = tk.LabelFrame(fenetre, text=" Informations ", bg="white", padx=20, pady=10)
cadre_resultat.pack(pady=10, padx=20, fill="both", expand=True)

label_image = tk.Label(cadre_resultat, bg="white")
label_image.pack(pady=5)

label_nom = tk.Label(cadre_resultat, text="---", font=("Helvetica", 12, "bold"), bg="white")
label_nom.pack()

label_types = tk.Label(cadre_resultat, text="Types : -", bg="white")
label_types.pack(pady=5)

cadre_stats = tk.Frame(cadre_resultat, bg="white")
cadre_stats.pack(pady=10)

noms_stats = [("PV", "pv"), ("Attaque", "attaque"), ("Défense", "defense"), ("Vitesse", "vitesse"), ("Spécial", "special")]
for i, (nom_affiche, cle_dict) in enumerate(noms_stats):
    tk.Label(cadre_stats, text=f"{nom_affiche} :", bg="white", font=("Arial", 9, "bold")).grid(row=i, column=0, sticky="e", padx=5)
    valeur_label = tk.Label(cadre_stats, text="0", bg="white")
    valeur_label.grid(row=i, column=1, sticky="w", padx=5)
    labels_stats[cle_dict] = valeur_label

cadre_bonus = tk.Frame(fenetre, bg="#f4f4f4")
cadre_bonus.pack(pady=5)

def afficher_bonus_moyenne():
    global base_de_donnees
    if not base_de_donnees: mettre_a_jour_affichage()
    moy = calculer_moyenne_vitesse(base_de_donnees)
    messagebox.showinfo("Bonus : Moyenne", f"La vitesse moyenne des Pokémon est de : {round(moy, 2)}")

def afficher_bonus_type():
    global base_de_donnees
    if not base_de_donnees: mettre_a_jour_affichage()
    type_saisi = entree_nom.get().strip()
    if not type_saisi: return
    liste = filtrer_par_type(type_saisi, base_de_donnees)
    res = "\n".join(liste[:15])
    messagebox.showinfo(f"Bonus : Type {type_saisi}", f"Pokémon trouvés ({len(liste)}) :\n{res}")

tk.Button(cadre_bonus, text="Vitesse moyenne", command=afficher_bonus_moyenne, bg="#4dad5b", fg="white", font=("Arial", 8)).pack(side="left", padx=5)
tk.Button(cadre_bonus, text="Filtrer par type", command=afficher_bonus_type, bg="#4dad5b", fg="white", font=("Arial", 8)).pack(side="left", padx=5)

if __name__ == "__main__":
    fenetre.mainloop()

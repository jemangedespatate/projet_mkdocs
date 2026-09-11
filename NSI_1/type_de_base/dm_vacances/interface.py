import tkinter as tk
from tkinter import messagebox, simpledialog

# On essaie d'importer le fichier logique.py
# Si ça plante, c'est que l'élève a mal nommé son fichier ou qu'il n'est pas dans le même dossier.
try:
    import logique
except ImportError:
    print("ERREUR CRITIQUE : Le fichier logique.py est introuvable !")
    print("Vérifie que interface.py et logique.py sont bien dans le même dossier.")
    exit()

class RPGInventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("🎒 Gestionnaire d'Inventaire RPG")
        self.geometry("450x600")
        self.config(bg="#f0f0f0")

        # Chargement de l'inventaire depuis le module logique
        try:
            self.inventaire = logique.creer_inventaire()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur dans creer_inventaire() : {e}")
            self.inventaire = {}

        self.creer_widgets()
        self.rafraichir_affichage()

    def creer_widgets(self):
        # Titre
        lbl_titre = tk.Label(self, text="⚔️ Mon Sac d'Aventurier 🛡️", 
                             font=("Segoe UI", 18, "bold"), bg="#f0f0f0", fg="#333")
        lbl_titre.pack(pady=20)

        # Liste (Listbox) pour afficher les objets
        frame_list = tk.Frame(self)
        frame_list.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.liste_box = tk.Listbox(frame_list, font=("Consolas", 12), bg="#fff", bd=2, relief="flat", selectbackground="#e1e1e1", selectforeground="black")
        self.liste_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame_list, orient="vertical", command=self.liste_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.liste_box.config(yscrollcommand=scrollbar.set)

        # Boutons
        frame_btn = tk.Frame(self, bg="#f0f0f0")
        frame_btn.pack(pady=20)

        btn_add = tk.Button(frame_btn, text="➕ Ajouter Objet", command=self.action_ajouter, bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"), padx=10, pady=5)
        btn_add.pack(side=tk.LEFT, padx=10)

        btn_remove = tk.Button(frame_btn, text="➖ Utiliser/Jeter", command=self.action_retirer, bg="#F44336", fg="white", font=("Segoe UI", 10, "bold"), padx=10, pady=5)
        btn_remove.pack(side=tk.LEFT, padx=10)

        btn_refresh = tk.Button(frame_btn, text="🔄 Rafraîchir", command=self.rafraichir_affichage, bg="#2196F3", fg="white", font=("Segoe UI", 10, "bold"), padx=10, pady=5)
        btn_refresh.pack(side=tk.LEFT, padx=10)

    def rafraichir_affichage(self):
        self.liste_box.delete(0, tk.END)
        
        # Appel de la fonction élève lister_objets
        try:
            items = logique.lister_objets(self.inventaire)
            
            if items is None:
                self.liste_box.insert(tk.END, "⚠️ Fonction lister_objets() renvoie None")
                self.liste_box.insert(tk.END, "   (Tu n'as pas encore codé cette fonction)")
                return

            if not isinstance(items, list):
                self.liste_box.insert(tk.END, "⚠️ Erreur : lister_objets doit renvoyer une LISTE")
                return

            if not items:
                self.liste_box.insert(tk.END, "(Sac vide)")
            
            for item in items:
                self.liste_box.insert(tk.END, f"• {item}")

        except Exception as e:
             self.liste_box.insert(tk.END, f"❌ Erreur Python : {e}")

    def action_ajouter(self):
        nom = simpledialog.askstring("Ajouter", "Nom de l'objet :")
        if not nom: return
        
        qte = simpledialog.askinteger("Ajouter", f"Combien de '{nom}' ajouter ?", minvalue=1)
        if not qte: return

        try:
            logique.ajouter_objet(self.inventaire, nom, qte)
            self.rafraichir_affichage()
        except Exception as e:
            messagebox.showerror("Bug dans ton code", f"Erreur dans ajouter_objet :\n{e}")

    def action_retirer(self):
        selection = self.liste_box.get(tk.ACTIVE)
        if not selection or "⚠️" in selection or "(Sac vide)" in selection:
            messagebox.showwarning("Attention", "Sélectionne un objet valide dans la liste.")
            return

        # On essaie de deviner le nom depuis l'affichage (suppose format "Nom : Qte" ou proche)
        # Pour être plus robuste, on demande le nom, ou on parse la string si l'élève respecte le format.
        # On va demander confirmation du nom pour simplifier la vie de l'élève au début.
        try:
            # Nettoyage basique : retire le "• " du début si présent
            texte_item = selection.replace("• ", "")
            # On prend la partie avant le " :"
            nom_suppose = texte_item.split(" :")[0]
        except:
            nom_suppose = ""

        nom = simpledialog.askstring("Retirer", "Nom de l'objet à retirer :", initialvalue=nom_suppose)
        if not nom: return

        qte = simpledialog.askinteger("Retirer", f"Combien de '{nom}' retirer ?", minvalue=1)
        if not qte: return

        try:
            logique.retirer_objet(self.inventaire, nom, qte)
            self.rafraichir_affichage()
        except Exception as e:
            messagebox.showerror("Bug dans ton code", f"Erreur dans retirer_objet :\n{e}")

if __name__ == "__main__":
    app = RPGInventoryApp()
    app.mainloop()

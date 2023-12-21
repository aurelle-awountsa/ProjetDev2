import tkinter as tk
from tkinter import ttk
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict

class GraphiquePreuves(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.bouton_afficher_graphique = ttk.Button(self, text="Afficher le graphique", command=self.afficher_graphique)
        self.bouton_afficher_graphique.pack(pady=10)

        self.graphique_frame = ttk.Frame(self)
        self.graphique_frame.pack(pady=10)

    def afficher_graphique(self):
        # Connexion à la base de données
        try:
            connexion = sqlite3.connect('database.db')
            curseur = connexion.cursor()

            # Exemple de requête SQL, ajustez-la en fonction de votre structure de base de données
            curseur.execute('SELECT enquId, type FROM Preuves')
            resultats = curseur.fetchall()

            # Fermez la connexion après avoir récupéré les données
            connexion.close()

            # Traitement des données et création du graphique
            data_dict = defaultdict(lambda: defaultdict(int))

            for resultat in resultats:
                enquId, type_preuve = resultat
                data_dict[enquId][type_preuve] += 1

            # Création du graphique à barres empilées
            figure = Figure(figsize=(8, 6), dpi=100)
            subplot = figure.add_subplot(111)

            enquIds = list(data_dict.keys())
            types = list(set(type_preuve for type_preuve in data_dict[enquIds[0]].keys()))  # Prend tous les types de preuves

            bottom = [0] * len(types)

            for enquId in enquIds:
                valeurs = [data_dict[enquId][type_preuve] for type_preuve in types]
                subplot.bar(types, valeurs, bottom=bottom, label=f"enquId {enquId}")
                bottom = [b + v for b, v in zip(bottom, valeurs)]

            subplot.set_xlabel('Type de Preuve')
            subplot.set_ylabel('Nombre de Preuves')
            subplot.legend()

            max_y = max(bottom)
            subplot.set_yticks(range(max_y + 1))

            canvas = FigureCanvasTkAgg(figure, master=self.graphique_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données depuis la base de données : {e}")

# Exemple d'utilisation de la classe dans l'application principale
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Graphique des Preuves par Type")
        self.geometry("800x600")

        self.graphique_preuves = GraphiquePreuves(self, self)
        self.graphique_preuves.pack()

# Lancement de l'application
app = Application()
app.mainloop()

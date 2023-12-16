# Importation des modules
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import sys

# Obtient le chemin vers l'interpréteur Python en cours d'exécution
py = sys.executable


# Création de la fenêtre principale en tant que classe héritant de Tk

class Enquete(Tk):

    """Cette classe est destinée à la manipulation d'enquête

    Author : Aurelle Awountsa
    Date : Decembre 2023
    Cette classe permet de gérer les opérations liées à une enquête

    """
    def __init__(self):
        super().__init__()  # appelle l'initialisateur de la classe Tk
        self.title('Ajouter une enquête')  # Définit le titre de la fenêtre

        # Obtient la résolution de l'écran principal
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.maxsize(screen_width, screen_height)
        self.minsize(500, 500)
        self.iconbitmap(r'icon.ico')
        matricule = StringVar()
        enqueteur = StringVar()
        debut = StringVar()
        fin = StringVar()
        status = StringVar()
        description = StringVar()

        def add_survey():
            """Ajoute une enquête à la base de données

        PRE : recueillir les informations relatives à une enquête via le formulaire
        POST : crée une nouvelle enquête et l'ajoute dans la base de données
        Raise: Exeption si len(matricule, enqueteur,debut, statut) = 0
        """
            matricule_value = matricule.get()
            enqueteur_value = enqueteur.get()
            debut_value = debut.get()
            fin_value = fin.get()
            status_value = status.get()
            description_value = description.get()


            if len(matricule.get()) == 0 or len(enqueteur.get()) == 0 or len(status.get()) == 0 or len(
                    debut.get()) == 0:
                messagebox.showerror("Error", "Veuillez renseigner les champs obligatoires")
            else:
                try:

                    self.conn = sqlite3.connect('database.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("insert into Enquetes values (?,?,?,?,?,?)",[matricule_value, debut_value, fin_value, enqueteur_value, status_value, description_value])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Ajouter avec succès')
                    ask = messagebox.askyesno("Confirm", "Voulez-vous ajouter une autre enquête?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'add_survey.py'))
                    else:
                        self.destroy()
                finally:
                    self.conn.close()

        # creation des labels
        Label(self, text='').pack()
        Label(self, text='Ajouter une enquête', fg='dark blue', font=('Arial', 25, 'bold')).pack()
        Label(self, text='').pack()
        Label(self, text='Matricule:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=130)
        Entry(self, textvariable=matricule, width=30).place(x=230, y=132)
        Label(self, text='Enqueteur:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=180)
        Entry(self, textvariable=enqueteur, width=30).place(x=230, y=182)
        Label(self, text='Date début:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=230)
        Entry(self, textvariable=debut, width=30).place(x=230, y=232)
        Label(self, text='Date fin:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=280)
        Entry(self, textvariable=fin, width=30).place(x=230, y=282)
        Label(self, text='Statut:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=330)
        Entry(self, textvariable=status, width=30).place(x=230, y=332)
        Label(self, text='Description:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=380)
        Entry(self, textvariable=description, width=30).place(x=230, y=382)
        Button(self, text="Submit", command=add_survey).place(x=270, y=480)
        def del_survey():
            """Suprimer une enquête à la base de données

            PRE : le matricule d'une enquête via le formulaire
            POST : supprime une enquête la base de données
            """

        def update_survey():
            """Mettre à jour une enquête
                la mise à jour d'une enquête consiste à modifier certains attributs comme dans ce cas le status, l'enqueteur en charge et la description de l'enquête
            PRE : le matricule d'une enquête via le formulaire
            POST : attributs d'une enquête modifiées la base de données
            """
            pass
        def search_survey():
            """chercher une enquête
                Une enquête est unique par son matricule
            PRE : le matricule d'une enquête via le formulaire
            POST : retourner les informations liées à une enquête
            """
            pass


# Création d'une instance de la classe Add_Survey et exécution de la boucle principale Tkinter
if __name__ == "__main__":
    Enquete().mainloop()

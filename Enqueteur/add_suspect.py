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

    """Cette classe est destinée à l'ajout de suspects à une enquête

    Author : Dimitri Meeus
    Date : Decembre 2023

    """
    def __init__(self):
        super().__init__()  # appelle l'initialisateur de la classe Tk
        self.title('Ajouter un suspect')  # Définit le titre de la fenêtre

        # Obtient la résolution de l'écran principal
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.maxsize(screen_width, screen_height)
        self.minsize(500, 500)
        self.iconbitmap(r'icon.ico')
        matricule = StringVar()
        nom = StringVar()
        prenom = StringVar()
        age = StringVar()
        addresse = StringVar()
        enquete = StringVar()

        def add_suspect():
            """Ajoute un suspect à la base de données

        PRE : recueillir les informations relatives d'un suspect via le formulaire
        POST : ajout d'un nouveau suspect dans la base de données
        Raise: Exeption si len(matricule, nom, prenom, age, addresse) = 0
        """
            matricule_value = matricule.get()
            nom_value = nom.get()
            prenom_value = prenom.get()
            age_value = age.get()
            addresse_value = addresse.get()
            enquete_value = enquete.get()


            if len(matricule.get()) == 0 or len(nom.get()) == 0 or len(prenom.get()) == 0 or len(
                    age.get()) == 0:
                messagebox.showerror("Error", "Veuillez renseigner les champs obligatoires")
            else:
                try:

                    self.conn = sqlite3.connect('database.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("insert into Suspect values (?,?,?,?,?,?)",[matricule_value, nom_value, prenom_value, age_value, addresse_value, enquete_value])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Ajouter avec succès')
                    ask = messagebox.askyesno("Confirm", "Voulez-vous ajouter une autre suspect?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'add_suspect.py'))
                    else:
                        self.destroy()
                finally:
                    self.conn.close()

        # creation des labels
        Label(self, text='').pack()
        Label(self, text='Ajouter un Suspect', fg='dark blue', font=('Arial', 25, 'bold')).pack()
        Label(self, text='').pack()
        Label(self, text='Matricule:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=130)
        Entry(self, textvariable=matricule, width=30).place(x=230, y=132)
        Label(self, text='Nom:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=180)
        Entry(self, textvariable=nom, width=30).place(x=230, y=182)
        Label(self, text='Prenom:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=230)
        Entry(self, textvariable=prenom, width=30).place(x=230, y=232)
        Label(self, text='Age:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=280)
        Entry(self, textvariable=age, width=30).place(x=230, y=282)
        Label(self, text='Addresse:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=330)
        Entry(self, textvariable=addresse, width=30).place(x=230, y=332)
        Label(self, text='Enquete:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=380)
        Entry(self, textvariable=enquete, width=30).place(x=230, y=382)
        Button(self, text="Submit", command=add_suspect).place(x=270, y=432)

# Création d'une instance de la classe Add_Survey et exécution de la boucle principale Tkinter
if __name__ == "__main__":
    Enquete().mainloop()

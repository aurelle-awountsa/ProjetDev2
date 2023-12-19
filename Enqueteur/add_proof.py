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

    """Cette classe est destinée à l'ajout de preuves à une enquête

    Author : Dimitri Meeus
    Date : Decembre 2023

    """
    def __init__(self):
        super().__init__()  # appelle l'initialisateur de la classe Tk
        self.title('Ajouter une preuve')  # Définit le titre de la fenêtre

        # Obtient la résolution de l'écran principal
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.maxsize(screen_width, screen_height)
        self.minsize(500, 450)
        self.iconbitmap(r'icon.ico')
        matricule = StringVar()
        description = StringVar()
        tipe = StringVar()
        date = StringVar()
        enquete = StringVar()

        def add_proof():
            """Ajoute une preuve à la base de données

        PRE : recueillir les informations relatives d'une preuve via le formulaire
        POST : ajout d'une nouvelle preuve dans la base de données
        Raise: Exeption si len(matricule, nom, prenom, age, addresse) = 0
        """
            matricule_value = matricule.get()
            description_value = description.get()
            tipe_value = tipe.get()
            date_value = date.get()
            enquete_value = enquete.get()


            if len(matricule.get()) == 0 or len(description.get()) == 0 or len(tipe.get()) == 0 or len(
                    date.get()) == 0 or len(enquete.get()) == 0:
                messagebox.showerror("Error", "Veuillez renseigner les champs obligatoires")
            else:
                try:

                    self.conn = sqlite3.connect('database.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("insert into Preuves values (?,?,?,?,?)",[matricule_value, description_value, tipe_value, date_value, enquete_value])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Ajouter avec succès')
                    ask = messagebox.askyesno("Confirm", "Voulez-vous ajouter une autre preuve?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'add_proof.py'))
                    else:
                        self.destroy()
                finally:
                    self.conn.close()

        # creation des labels
        Label(self, text='').pack()
        Label(self, text='Ajouter une Preuve', fg='dark blue', font=('Arial', 25, 'bold')).pack()
        Label(self, text='').pack()
        Label(self, text='Matricule:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=130)
        Entry(self, textvariable=matricule, width=30).place(x=230, y=132)
        Label(self, text='Description:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=180)
        Entry(self, textvariable=description, width=30).place(x=230, y=182)
        Label(self, text='Type:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=230)
        Entry(self, textvariable=tipe, width=30).place(x=230, y=232)
        Label(self, text='Date:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=280)
        Entry(self, textvariable=date, width=30).place(x=230, y=282)
        Label(self, text='Enquete:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=330)
        Entry(self, textvariable=enquete, width=30).place(x=230, y=332)
        Button(self, text="Submit", command=add_proof).place(x=270, y=380)

# Création d'une instance de la classe Add_Survey et exécution de la boucle principale Tkinter
if __name__ == "__main__":
    Enquete().mainloop()

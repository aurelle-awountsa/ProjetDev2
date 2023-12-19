# Importation des modules
import sqlite3
from tkinter import *
from tkinter import ttk
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
        self.maxsize(800, 600)
        self.minsize(800, 600)
        self.iconbitmap(r'icon.ico')
        description = StringVar()
        matricule = StringVar()
        status = StringVar()

        def update_survey():
            """mettre à jour une enquête
            Mettre à jour une enquête consiste à mettre à jour son status et/ou sa description
            PRE : le matricule, le status et la matricule d'une enquête via le formulaire
            POST : modifie ces éléments dans la db
            """
            status_value = status.get()
            matricule_value = matricule.get()
            description_value = description.get()

            if len(status_value) == 0 or len(description_value) == 0:
                messagebox.showerror("Error", "Veuillez renseigner les champs obligatoires")
            else:
                try:
                    self.conn = sqlite3.connect('database.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("UPDATE Enquetes SET status = ?, description = ? WHERE matricule = ?",
                                          (status_value, description_value, matricule_value))
                    self.conn.commit()
                    ask = messagebox.askyesno("Confirm", "Voulez-vous mettre à jour une autre enquête?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'update_survey.py'))
                    else:
                        self.destroy()
                finally:
                    self.conn.close()

        # creation des labels
        Label(self, text='').pack()
        Label(self, text='Mettre à jour une enquête', fg='dark blue', font=('Arial', 25, 'bold')).pack()
        Label(self, text='').pack()
        Label(self, text='Matricule:', font=('Comic Scan Ms', 14, 'bold')).place(x=150, y=250)
        Entry(self, textvariable=matricule, width=30).place(x=280, y=250)
        Label(self, text='Statut:', font=('Comic Scan Ms', 14, 'bold')).place(x=150, y=300)
        Entry(self, textvariable=status, width=30).place(x=280, y=300)
        Label(self, text='Description:', font=('Comic Scan Ms', 14, 'bold')).place(x=150, y=350)
        Entry(self, textvariable=description, width=30).place(x=280, y=350)
        Button(self, text="Submit", command=update_survey).place(x=380, y=450)


# Création d'une instance de la classe Enquete et exécution de la boucle principale Tkinter
if __name__ == "__main__":
    Enquete().mainloop()

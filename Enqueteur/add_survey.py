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

class Add_Survey(Tk):
    def __init__(self):
        super().__init__()  # appelle l'initialisateur de la classe Tk
        self.title('Ajouter une enquête')  # Définit le titre de la fenêtre

        # Obtient la résolution de l'écran principal
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.maxsize(screen_width, screen_height)
        self.minsize(500, 500)
        matricule = StringVar()
        enqueteur = StringVar()
        debut = StringVar()
        fin = StringVar()
        status = StringVar()
        description = StringVar()

        def submit():
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
        Label(self, text='Enquête', fg='dark blue', font=('Arial', 25, 'bold')).pack()
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
        Button(self, text="Submit", command=submit).place(x=270, y=480)


# Création d'une instance de la classe Add_Survey et exécution de la boucle principale Tkinter
if __name__ == "__main__":
    Add_Survey().mainloop()

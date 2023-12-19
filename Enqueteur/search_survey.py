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
        matricule = StringVar()

        def search_survey():
            """chercher une enquête
                Une enquête est unique par son matricule
            PRE : le matricule d'une enquête via le formulaire
            POST : retourner les informations liées à une enquête
            """
            matricule_value = matricule.get()

            if len(matricule.get()) == 0:
                messagebox.showerror("Error", "Veuillez renseigner les champs obligatoires")
            else:
                try:

                    self.conn = sqlite3.connect('database.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("select * from Enquetes WHERE matricule = ?", [matricule_value])
                    self.conn.commit()
                    self.pc = self.myCursor.fetchall()
                    if self.pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in self.pc:
                            self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4],row[5]))
                    else:
                        messagebox.showinfo("Error", "le matricule est incorrect")
                #self.destroy()
                finally:
                    self.conn.close()

        # creation des labels
        Label(self, text='').pack()
        Label(self, text='Chercher une enquête', fg='dark blue', font=('Arial', 25, 'bold')).pack()
        Label(self, text='').pack()
        Label(self, text='Matricule:', font=('Comic Scan Ms', 14, 'bold')).place(x=260, y=150)
        Entry(self, textvariable=matricule, width=30).place(x=400, y=155)


        self.listTree = ttk.Treeview(self,height=10,columns=('Debut','Fin','Enqueteur','Status','Description'))
        self.listTree.heading("#0",text='Matricule',anchor = 'center')
        self.listTree.column("#0",width=120,minwidth=120,anchor='center')
        self.listTree.heading('Debut', text='Date debut')
        self.listTree.column("Debut",width=120,minwidth=120,anchor='center')
        self.listTree.heading("Fin", text='Date fin')
        self.listTree.column("Fin", width=120,minwidth=120,anchor='center')
        self.listTree.heading("Enqueteur", text='Enqueteur')
        self.listTree.column("Enqueteur", width=120,minwidth=120,anchor='center')
        self.listTree.heading("Status", text='Status')
        self.listTree.column("Status", width=120, minwidth=120,anchor='center')
        self.listTree.heading("Description", text='Description')
        self.listTree.column("Description", width=120 , minwidth=120,anchor='center')

        self.listTree.place(x=40,y=280)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))
        Button(self, text="Chercher", font=('Arial', 13, 'bold'), command=search_survey).place(x=350, y=210)


# Création d'une instance de la classe Add_Survey et exécution de la boucle principale Tkinter
if __name__ == "__main__":
    Enquete().mainloop()

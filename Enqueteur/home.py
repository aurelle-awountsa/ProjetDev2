import sys
from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
from sqlite3 import Error
from tkinter import ttk
import os

py = sys.executable


# creating window
class Home(Tk):
    def __init__(self):
        super().__init__()
        self.matricule = StringVar()
        self.password = StringVar()
        self.maxsize(800, 600)
        self.minsize(800, 600)
        self.title("Login")
        self.state("zoomed")
        self.iconbitmap(r'icon.ico')
        self.canvas = Canvas(width=300, height=190)
        self.canvas.pack()
        self.photo = PhotoImage(file='bg.png')
        self.canvas.create_image(35, 10, image=self.photo, anchor=NW)
        self.title("Sherlockête")
        self.menubar = Menu(self)

        def add_survey():

            try:
                subprocess.Popen([py, 'add_survey.py'], shell=True)
                print("Fenêtre 'add_survey.py' ouverte avec succès.")
            except Exception as e:
                print(f"Erreur lors de l'ouverture de la fenêtre 'add_survey.py': {e}")
        def add_invest():

            try:
                subprocess.Popen([py, 'signup.py'], shell=True)
                print("Fenêtre 'signup.py' ouverte avec succès.")
            except Exception as e:
                print(f"Erreur lors de l'ouverture de la fenêtre 'signup.py': {e}")


        def display():
            """
                Cette methode permet d'afficher les éléments qui seront présents sur la page d'accueil

            """
            conn = sqlite3.connect('database.db')
            myCursor = conn.cursor()
            myCursor.execute("select * from Enquetes")
            self.pc = myCursor.fetchall()
            if self.pc:
                self.listTree.delete(*self.listTree.get_children())
                for row in self.pc:
                    self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4],row[5]))
            else:
                messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued on this ID")
            conn.commit()
            conn.close()
        Label(self, text='').pack()
        Label(self, text='Bienvenue dans Sherlockête  ', fg='black', font=('Arial', 25, 'bold')).place(x=170, y=140)
        Label(self, text='').pack()

        list1 = Menu(self)
        list1.add_command(label="Ajouter enquête", command=add_survey)
        list1.add_command(label="Supprimer enquête")
        list1.add_separator()
        list1.add_command(label="Chercher enquête")
        list1.add_command(label="Mettre à jour enquête")
        list1.add_separator()
        list1.add_command(label="Clôturer enquête")

        list2 = Menu(self)
        list2.add_command(label="Ajouter enqueteur", command=add_invest)
        list2.add_command(label="Supprimer enqueteur")

        list3 = Menu(self)
        list3.add_command(label="Ajouter suspect")
        list3.add_command(label="Supprimer suspect")

        list4 = Menu(self)
        list4.add_command(label="Ajouter témoin")
        list4.add_command(label="Supprimer témoin")

        list5 = Menu(self)
        list5.add_command(label="Rapport")
        list5.add_command(label="Preuves")

        self.menubar.add_cascade(label='Enquête', menu=list1)
        self.menubar.add_cascade(label='Enqueteur', menu=list2)
        self.menubar.add_cascade(label='Suspect', menu=list3)
        self.menubar.add_cascade(label='Témoins', menu=list4)
        self.menubar.add_cascade(label='Aurtres', menu=list5)
        self.config(menu=self.menubar)

        Button(self, text="Afficher toutes les enquête", command=display,font=('Arial', 13, 'bold')).place(x=265, y=250)
        self.listTree = ttk.Treeview(self,height=10,columns=('Debut','Fin','Enqueteur','Status','Description'))
        self.listTree.heading("#0",text='Matricule',anchor='center')
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
        self.listTree.place(x=40,y=320)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))



Home().mainloop()

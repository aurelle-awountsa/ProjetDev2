import sys
from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
py = sys.executable


#creating window
class Login(Tk):
    def __init__(self):
        super().__init__()
        self.matricule = StringVar()
        self.password = StringVar()
        self.maxsize(700, 600)
        self.minsize(700, 600)
        self.title("Login")


#verification des données
        def checkInput():
            if len(self.matricule.get()) == 0:
                messagebox.showinfo("Veuillez entrer votre matricule")
            elif len(self.password.get()) == 0:
                messagebox.showinfo("Veuillez entre votre mot de passe")
            else:
                try:
                    self.conn = sqlite3.connect('database.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Select * from enqueteur where matricule=? AND password =?",[self.matricule.get(),self.password.get()])
                    self.pc = self.myCursor.fetchall()
                    self.myCursor.close()
                    self.conn.close()
                    if self.pc:
                        self.destroy()
                        os.system(f'"{py}" home.py')
                    else:
                        messagebox.showinfo('Error', 'Matricule et ou mot de passe non reconnu')
                        self.matricule.delete(0, END)
                        self.password.delete(0, END)
                except Error:
                    messagebox.showinfo('Error',"Réessayez")

        def checkExist():
            try:
                conn = sqlite3.connect('database.db')
                mycursor = conn.cursor()
                mycursor.execute("Select * from enqueteur")
                x = mycursor.fetchone()
                mycursor.close()
                conn.close()
                if not x:
                    messagebox.showinfo("Error", "Cet utilisateur n'existe pas")
                    x = messagebox.askyesno("Confirm","Voulez vous enregistrer un nouvel enqueteur?")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'signup.py'))
                else:
                    Label(self, text='').pack()
                    Label(self, text='Connexion', fg='dark blue', font=('Arial', 25, 'bold')).pack()
                    Label(self, text='').pack()
                    Label(self, text="Matricule", font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=230)
                    Entry(self, textvariable=self.matricule, width=30).place(x=230, y=232)
                    Label(self, text="Password",font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=280)
                    Entry(self, show='*', textvariable=self.password, width=30).place(x=230, y=282)
                    Button(self, text="Connexion", font=10, width=15, command=checkInput).place(x=250, y=480)
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")

        checkExist()

Login().mainloop()

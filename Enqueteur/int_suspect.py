import sys
from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
from tkinter import ttk

py = sys.executable


# creation de la fenêtre
class Suspect(Tk):
    def __init__(self):
        super().__init__()
        self.matricule = StringVar()
        self.password = StringVar()
        self.maxsize(800, 600)
        self.minsize(800, 600)
        self.title("Login")
        self.state("zoomed")
        self.iconbitmap(r'icon.ico')
        self.title("Intérroger le suspect")
        self.menubar = Menu(self)
    d = Frame( width=650, height=400, bg="light blue").place(x=370, y=180)
    Label(d, text="Security Question", font=("Arial", 13, "bold"), bg="light blue").place(x=420, y=380)
    Label(d, text="Security Answer", font=("Arial", 13, "bold"), bg="light blue").place(x=420, y=420)

# Création d'une instance de la classe Add_Survey et exécution de la boucle principale Tkinter

if __name__ == "__main__":
    Suspect().mainloop()

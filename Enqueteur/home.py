import sys
from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
py = sys.executable


#creating window
class Home(Tk):
    def __init__(self):
        super().__init__()
        self.matricule = StringVar()
        self.password = StringVar()
        self.maxsize(700, 600)
        self.minsize(700, 600)
        self.title("Login")
Home().mainloop()

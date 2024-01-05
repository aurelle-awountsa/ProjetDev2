import os
import sys
from tkinter import *
from tkinter import messagebox

import add_survey
from logic_add_survey import LogicAddSurvey


py = sys.executable

class AddSurvey(Tk):
    def __init__(self):
        super().__init__()  # appelle l'initialisateur de la classe Tk
        self.title('Ajouter une enquête')  # Définit le titre de la fenêtre

        # Obtient la résolution de l'écran principal
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.maxsize(screen_width, screen_height)
        self.minsize(500, 500)
        self.iconbitmap(r'icon.ico')
        self.matricule = StringVar()
        self.enqueteur = StringVar()
        self.debut = StringVar()
        self.fin = StringVar()
        self.status = StringVar()
        self.description = StringVar()

        self.logic = LogicAddSurvey(self.matricule, self.debut, self.fin, self.enqueteur, self.status, self.description)
        self.add_survey_gui()

    def add_survey(self):
        success, message = self.logic.add_survey()

        if success:
            messagebox.showinfo("Info", message)
            ask = messagebox.askyesno("Confirm", "Voulez-vous ajouter une autre enquête?")
            if not ask:
                self.destroy()
        else:
            messagebox.showerror("Error", message)


    # creation des labels
    def add_survey_gui(self):
        Label(self, text='').pack()
        Label(self, text='Ajouter une enquête', fg='dark blue', font=('Arial', 25, 'bold')).pack()
        Label(self, text='').pack()
        Label(self, text='Matricule:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=130)
        Entry(self, textvariable=self.matricule, width=30).place(x=230, y=132)
        Label(self, text='Enqueteur:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=180)
        Entry(self, textvariable=self.enqueteur, width=30).place(x=230, y=182)
        Label(self, text='Date début:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=230)
        Entry(self, textvariable=self.debut, width=30).place(x=230, y=232)
        Label(self, text='Date fin:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=280)
        Entry(self, textvariable=self.fin, width=30).place(x=230, y=282)
        Label(self, text='Statut:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=330)
        Entry(self, textvariable=self.status, width=30).place(x=230, y=332)
        Label(self, text='Description:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=380)
        Entry(self, textvariable=self.description, width=30).place(x=230, y=382)
        Button(self, text="Submit", command= self.add_survey).place(x=270, y=480)

if __name__ == "__main__":
    AddSurvey().mainloop()

import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sys

# Obtient le chemin vers l'interpréteur Python en cour d'exécution
py = sys.executable
#Interface graphique
screen = Tk()

#variables
matricule = StringVar()
name = StringVar()
email = StringVar()
password = StringVar()
gender = StringVar()
# résolution de la fenêtre
screen.geometry("700x600")
screen.maxsize(width="700", height="600")
screen.minsize(width="700", height="600")
screen.title("Inscription")

def validation():
    if matricule.get() != "" and name.get() != "" and email.get() != "" and password.get() != "" and gender.get() != "":
        email_check = email_validation()
        password_check=password_validataion()
        if email_check:
            if password_check:
                insertion()
                messagebox.showinfo("information","envoyer avec succès")
                loginForm()
            else:
                messagebox.showerror("Error","Le mot de passe doit avoir (min 8 characteres ,majuscule et minuscule , chiffre et symbole)")

        else:
            messagebox.showerror("Error", 'Ce mail ne correspond pas au format recquis')
    else:
        messagebox.showerror("Error", "Tous les champs doivent être remplis")

def loginForm():
    screen.destroy()
    # import login


def insertion():
    
    matricule_value = matricule.get()
    name_value = name.get()
    email_value = email.get()
    password_value = password.get()
    gender_value = gender.get()
     
    if matricule_value != "" and name_value != "" and email_value != "" and password_value != "":
        try:
            conn = sqlite3.connect('database.db')
            myCursor = conn.cursor()
            myCursor.execute("INSERT INTO enqueteur VALUES (?,?,?,?,?)", [matricule_value, name_value, email_value, password_value, gender_value])
            conn.commit()
            messagebox.showinfo('Info', 'Enquêteur ajouté avec succès')
            ask = messagebox.askyesno("Confirm", "Voulez-vous ajouter un autre enquêteur?")
            if ask:
                conn.close()
                screen.destroy()
                os.system('%s %s' % (py, 'signup.py'))
            else:
                conn.close()
                screen.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Erreur lors de l'insertion dans la base de données: {e}")
    else:
        messagebox.showerror("Error", "Veuillez remplir tous les champs obligatoires")


def email_validation():
    userEmail = email.get()
    count = -1
    for i in userEmail:
        count += 1
        if i == "@":
            if userEmail[count:len(userEmail)] == "@gmail.com":
                return True
            else:
                return False
            
    else:
        return False

def password_validataion():
    userPass = password.get()
    if len(userPass)>=8:
        a,b,c,d=False,False,False,False
        #use multi varaible for checking pass_validatiom
        for i in userPass:
            x = ord(i)
            if x>=65 and x<=90:
                a=True
            elif x>=97 and x<=122:
                b=True
            elif x>=48 and x<=57:
                c=True
            else:
                d=True
        if a and b and c and d:
            return True
        else:
            return False
    else:
        return False

 # creation des labels
Label(screen, text='').pack()
Label(screen, text='Inscription', fg='dark blue', font=('Arial', 25, 'bold')).pack()
Label(screen, text='').pack()
Label(screen, text='Matricule:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=130)
Entry(screen, textvariable=matricule, width=30).place(x=230, y=132)
Label(screen, text='Nom:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=180)
Entry(screen, textvariable=name, width=30).place(x=230, y=182)
Label(screen, text='Email:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=230)
Entry(screen, textvariable=email, width=30).place(x=230, y=232)
Label(screen, text='Password:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=280)
Entry(screen, textvariable=password, width=30).place(x=230, y=282)

gender.set("Radio")
Label(screen, text="Genre", font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=330)

Radiobutton(screen, text="Homme", value="Male", width="5", variable=gender).place(x=190, y=330)
Radiobutton(screen, text="Femme", width="5", value="Female", variable=gender).place(x=260, y=330)
Radiobutton(screen, text="Autres",width="5", value="Others", variable=gender).place(x=340, y=330)
Button(screen, text="Inscription", command=validation).place(x=270, y=480)

screen.mainloop()

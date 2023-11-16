import sqlite3
from datetime import datetime
from tabulate import tabulate




class Enquetes:

    def __init__(self, matricule, debut, fin, enqueteur, status):
        """ cette fonction crée un objet enquête
             PRE: matricule de l'enquête  , date de debut de l'enquête ,date de fin de l'enquête,  enqueteur en charge de l'enquête, status de l'enquête
             POST: un objet enquête
        """

        self._matricule = matricule
        self._debut = debut
        self._fin = fin
        self._enqueteur = enqueteur
        self._status = status

        @property
        def matricule(self):
            return self._matricule

        @property
        def debut(self):
            return self._debut

        @property
        def fin(self):
            return self._fin

        @property
        def enqeteur(self):
            return self._enqueteur

        @property
        def status(self):
            return self._status

    def __str__(self):
        """cette fonction retourne le représentation d'une enquête

             PRE : recoit un objet enquête
             POST : retourne la représentation d'une enquête
         """
        return f' Matricule: {self.matricule}, debut: {self._debut}, fin: {self.fin}, enqueteur: {self.enqueteur}, status: {self.status}'

def main():
    while (True):
        welcomeMsg = '''\n ====== Gestionnaire d'enquête ======
       
         Veuillez choisir parmi les options suivantes:
         1. Ajouter une nouvelle enquête 
         2. Afficher toutes les enquêtes 
         3. Chercher une enquête
         4. supprimer une enquête
         5. Terminer
         '''
        print(welcomeMsg)
        a = int(input("Entrer votre choix: "))

        """====== Ajouter une nouvelle enquête ======"""
        if a == 1:
            matricule = input("Entrer le matricule de l'enquête ")
            debut = input("Entrer la date de debut de l'enquête au format AAAA-MM-JJ")
            fin = "vous venez de créer cette enquête"
            enqueteur = input("Entrer l'enqueteur en charge de cette enquête")
            status = "Ouverte"

            conn = sqlite3.connect('database.db')
            myCursor = conn.cursor()
            myCursor.execute("insert into Enquetes values (?,?,?,?,?)", [matricule, debut, fin, enqueteur, status])
            conn.commit()
            print('equête ajoutée avec succes')
            conn.close()

            """====== Afficher toutes les enquêtes ======"""

        elif a == 2:
            conn = sqlite3.connect('database.db')
            myCursor = conn.cursor()
            myCursor.execute("select * from Enquetes")
            rows = myCursor.fetchall()
            tabEnquete = [
                (matricule, debut, fin, enqueteur, status) for matricule, debut, fin, enqueteur, status in rows]
            print("Les enquêtes")
            headers = ["Matricule", "Date de debut", "Date de fin", "Enqueteur", "status"]
            print(tabulate(tabEnquete, headers=headers, tablefmt="grid"))

            conn.commit()
            conn.close()


            """====== Chercher une enquête ======"""

        elif a == 3:
            matricule = input(" Entrer le matricule de l'enquête que vous souhaitez retrouver")
            conn = sqlite3.connect('database.db')
            myCursor = conn.cursor()
            myCursor.execute(" select * from Enquetes WHERE matricule = ?", (matricule,))
            rows = myCursor.fetchall()
            table = [
                (matricule, debut, fin, enqueteur, status) for matricule, debut, fin, enqueteur, status in rows]
            print("Les enquêtes")
            headers = ["Matricule", "Date de debut", "Date de fin", "Enqueteur", "status"]
            print(tabulate(table, headers=headers, tablefmt="grid"))
            conn.commit()
            conn.close()

        elif a == 5:
            print("A tres bientot !")
            exit()

if __name__ == "__main__": 
    main()
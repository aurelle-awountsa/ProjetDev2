import sqlite3

class LogicAddSurvey:
    def __init__(self, matricule, debut, fin, enqueteur, status, description):
        """ cette fonction crée un objet enquête
             PRE: matricule de l'enquête  , date de debut de l'enquête ,date de fin de l'enquête,  enqueteur en charge de l'enquête, status de l'enquête
             POST: un objet enquête
        """
        self._matricule = matricule
        self._debut = debut
        self._fin = fin
        self._enqueteur = enqueteur
        self._status = status
        self._description = description


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
    @property
    def description(self):
        return self._description


    def add_survey(self):

        matricule_value = self._matricule.get()
        enqueteur_value = self._enqueteur.get()
        debut_value = self._debut.get()
        fin_value = self._fin.get()
        status_value = self._status.get()
        description_value = self._description.get()
        if len(matricule_value) == 0 or len(enqueteur_value) == 0 or len(status_value) == 0 or len(debut_value) == 0:
            return False, "Veuillez renseigner les champs obligatoires"
        try:
            conn = sqlite3.connect('database.db')
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO Enquetes VALUES (?,?,?,?,?,?)",
                                [matricule_value, debut_value, fin_value, enqueteur_value, status_value, description_value])
            conn.commit()
            conn.close()
            return True, "Ajouter avec succès"
        except Exception as e:
            return False, f"Erreur lors de l'ajout : {e}"
            print(e)



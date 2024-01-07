import sqlite3
import unittest

from logic_add_survey import LogicAddSurvey


class TestLogicAddSurvey(unittest.TestCase):
    def setUp(self):
        matricule = 'AEG'
        debut = '2023-10-31'
        fin = 'vous venez de créer cette enquête'
        enqueteur = 'Aurelle'
        status = 'en cours'
        description = 'meurtre'

        self.logic_add_survey = LogicAddSurvey(matricule, debut, fin, enqueteur, status, description)
    def test_insert_all_survey(self, ):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        matricule_value = self.logic_add_survey.matricule
        debut_value = self.logic_add_survey.debut
        fin_value = self.logic_add_survey.fin
        enqueteur_value = self.logic_add_survey.enqeteur
        status_value = self.logic_add_survey.status
        description_value = self.logic_add_survey.description

        cursor.execute("INSERT INTO Enquetes VALUES (?,?,?,?,?,?)", (matricule_value, debut_value, fin_value, enqueteur_value, status_value, description_value))
        conn.commit()

        cursor.execute("SELECT * FROM Enquetes WHERE matricule=?", (matricule_value,))

        result = cursor.fetchall()
        expected = [(matricule_value, debut_value, fin_value, enqueteur_value, status_value, description_value)]
        self.assertEqual(result, expected)
        cursor.execute('DELETE FROM Enquetes WHERE matricule=?', (matricule_value,))
        conn.commit()


        conn.close()




if __name__ == '__main__':
    unittest.main()

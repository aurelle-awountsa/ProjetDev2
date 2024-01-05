import unittest
from unittest.mock import patch
import tkinter as tk

from logic_add_survey import LogicAddSurvey


class TestLogicAddSurvey(unittest.TestCase):

    def setUp(self):
        # Créez une instance de la classe LogicAddSurvey pour chaque test
        self.survey = LogicAddSurvey("123", "2022-01-01", "2022-01-31", "Aurelle", "En Cours", "Description1")

    def tearDown(self):
        # Supprimez l'instance de la classe LogicAddSurvey après chaque test
        del self.survey

    def test_properties(self):
        self.assertEqual(self.survey.matricule, "123")
        self.assertEqual(self.survey.debut, "2022-01-01")
        self.assertEqual(self.survey.fin, "2022-01-31")
        self.assertEqual(self.survey.enqeteur, "Aurelle")
        self.assertEqual(self.survey.status, "En Cours")
        self.assertEqual(self.survey.description, "Description1")

    @patch("builtins.input", side_effect=["123", "Aurelle", "2022-01-01", "2022-01-31", "En Cours", "Description1"])
    def test_add_survey_success(self, mock_input):
        # Utilisez patch pour simuler l'entrée utilisateur dans la fonction add_survey
        result, message = self.survey.add_survey()
        self.assertTrue(result)
        self.assertEqual(message, "Ajouter avec succès")

    @patch("builtins.input", side_effect=["", "Aurelle", "2022-01-01", "2022-01-31", "En Cours", "Description1"])
    def test_add_survey_failure_empty_matricule(self, mock_input):
        result, message = self.survey.add_survey()
        self.assertFalse(result)
        self.assertEqual(message, "Veuillez renseigner les champs obligatoires")

    # Ajoutez d'autres tests en fonction de vos besoins

if __name__ == "__main__":
    unittest.main()

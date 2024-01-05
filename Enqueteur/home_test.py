import sqlite3
import unittest
from unittest.mock import MagicMock
from home_logic import LogicHome  # Remplacez 'your_module' par le nom réel de votre module

class TestLogicHome(unittest.TestCase):
    def setUp(self):
        self.logic_home = LogicHome()

    def test_select_all_survey(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Enquetes;")
        result = cursor.fetchall()
        expected = [('AZE', '2023-10-31', 'vous venez de créer cette enquête', 'Aurelle','en cours',  'meurtre')]
        self.assertEqual(result, expected)
        conn.close()




if __name__ == '__main__':
    unittest.main()

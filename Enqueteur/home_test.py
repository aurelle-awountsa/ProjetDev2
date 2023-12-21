import sys
import unittest
from unittest.mock import patch

from home import Home  # Assurez-vous de remplacer "your_script_file_name" par le nom réel de votre fichier


class TestHomeClass(unittest.TestCase):
    app: Home

    def setUp(self):
        self.app = Home()

    def tearDown(self):
        self.app.destroy()

    @patch("subprocess.Popen")
    def test_add_survey(self, mock_popen):
        self.app.add_survey()
        mock_popen.assert_called_once_with([sys.executable, 'add_survey.py'], shell=True)

    @patch("subprocess.Popen")
    def test_add_invest(self, mock_popen):
        self.app.add_invest()
        mock_popen.assert_called_once_with([sys.executable, 'signup.py'], shell=True)

    @patch("sqlite3.connect")
    @patch("sqlite3.Cursor")
    @patch("tkinter.messagebox.showinfo")
    def test_display_with_data(self, mock_showinfo, mock_cursor, mock_connect):
        mock_cursor.fetchall.return_value = [("1", "2022-01-01", "2022-02-01", "John Doe", "Open", "Description")]
        self.app.display()
        mock_connect.assert_called_once_with('database.db')
        mock_cursor.execute.assert_called_once_with("select * from Enquetes")
        mock_cursor.fetchall.assert_called_once()
        self.app.listTree.delete.assert_called_once_with(*self.app.listTree.get_children())
        self.app.listTree.insert.assert_called_once_with("", 'end', text="1", values=(
            "2022-01-01", "2022-02-01", "John Doe", "Open", "Description"))
        mock_showinfo.assert_not_called()

    @patch("sqlite3.connect")
    @patch("sqlite3.Cursor")
    @patch("tkinter.messagebox.showinfo")
    def test_display_without_data(self, mock_showinfo, mock_cursor, mock_connect):
        mock_cursor.fetchall.return_value = []
        self.app.display()
        mock_connect.assert_called_once_with('database.db')
        mock_cursor.execute.assert_called_once_with("select * from Enquetes")
        mock_cursor.fetchall.assert_called_once()
        self.app.listTree.delete.assert_not_called()
        self.app.listTree.insert.assert_not_called()
        mock_showinfo.assert_called_once_with("Error", "Matricule introuvable")


if __name__ == '__main__':
    unittest.main()

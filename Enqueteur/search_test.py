import unittest
from tkinter import Tk, StringVar
from unittest.mock import patch
from search_survey import Enquete

class TestEnquete(unittest.TestCase):
    def setUp(self):
        self.app = Enquete()
        self.app.withdraw()  # Pour éviter d'afficher la fenêtre pendant les tests

    def tearDown(self):
        self.app.destroy()

    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.messagebox.showinfo')
    @patch('tkinter.ttk.Treeview.delete')
    @patch('tkinter.ttk.Treeview.insert')
    @patch('tkinter.Entry.get')
    @patch('sqlite3.connect')
    def test_search_survey_valid(self, mock_connect, mock_entry_get, mock_tree_insert,
                                 mock_tree_delete, mock_showinfo, mock_showerror):
        mock_entry_get.return_value = 'valid_matricule'
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [(1, '2023-01-01', '2023-01-10', 'Enqueteur1', 'Status1', 'Description1')]

        self.app.search_survey()

        mock_connect.assert_called_once_with('database.db')
        mock_cursor.execute.assert_called_once_with("select * from Enquetes WHERE matricule = ?", ['valid_matricule'])
        mock_connect.return_value.commit.assert_called_once()
        mock_tree_delete.assert_called_once()
        mock_tree_insert.assert_called_once_with('', 'end', text=1,
                                                 values=('2023-01-01', '2023-01-10', 'Enqueteur1', 'Status1', 'Description1'))
        mock_showerror.assert_not_called()
        mock_showinfo.assert_not_called()

    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.messagebox.showinfo')
    @patch('tkinter.ttk.Treeview.delete')
    @patch('tkinter.ttk.Treeview.insert')
    @patch('tkinter.Entry.get')
    @patch('sqlite3.connect')
    def test_search_survey_invalid(self, mock_connect, mock_entry_get, mock_tree_insert,
                                   mock_tree_delete, mock_showinfo, mock_showerror):
        mock_entry_get.return_value = ''  # Empty matricule
        self.app.search_survey()

        mock_connect.assert_not_called()
        mock_entry_get.assert_called_once()
        mock_tree_delete.assert_not_called()
        mock_tree_insert.assert_not_called()
        mock_showinfo.assert_not_called()
        mock_showerror.assert_called_once_with("Error", "Veuillez renseigner les champs obligatoires")

if __name__ == '__main__':
    unittest.main()

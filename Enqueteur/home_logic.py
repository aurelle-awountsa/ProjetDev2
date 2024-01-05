import sqlite3

class LogicHome():
    def __init__(self):
        pass

    def display(self, home):
            """
                Cette methode permet d'afficher les éléments qui seront présents sur la page d'accueil

            """
            conn = sqlite3.connect('database.db')
            myCursor = conn.cursor()
            myCursor.execute("select * from Enquetes")
            self.pc = myCursor.fetchall()
            if self.pc:
                home.listTree.delete(*home.listTree.get_children())
                for row in self.pc:
                    home.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4],row[5]))
            else:
                print("Aucune enquête trouvée dans la base de données.")
            conn.commit()
            conn.close()


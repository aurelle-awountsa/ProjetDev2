import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Enquete(Tk):
    def __init__(self):
        super().__init__()
        self.title('Chercher enquête')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.maxsize(800, 600)
        self.minsize(800, 600)
        self.iconbitmap(r'icon.ico')
        matricule = StringVar()

        def search_survey():
            matricule_value = matricule.get()

            if len(matricule.get()) == 0:
                messagebox.showerror("Error", "Veuillez renseigner les champs obligatoires")
            else:
                try:
                    self.conn = sqlite3.connect('database.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("select * from Enquetes WHERE matricule = ?", [matricule_value])
                    self.conn.commit()
                    self.pc = self.myCursor.fetchall()
                    if self.pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in self.pc:
                            self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
                    else:
                        messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued on this ID")
                finally:
                    self.conn.close()

        def show_reports(event):
            selected_item = self.listTree.selection()
            if selected_item:
                matricule_enquete = self.listTree.item(selected_item, "text")

                try:
                    self.conn = sqlite3.connect('database.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("SELECT * FROM Rapport WHERE enquId = ?", [matricule_enquete])
                    self.conn.commit()
                    rapports = self.myCursor.fetchall()

                    if rapports:
                        report_window = Toplevel(self)
                        report_window.title(f"Rapports pour l'enquête {matricule_enquete}")

                        # Création d'une nouvelle Treeview pour afficher les rapports
                        report_tree = ttk.Treeview(report_window, height=10,
                                                   columns=('Fichier', 'Date', 'EnqueteurId'))
                        report_tree.heading("#0", text='Matricule', anchor='center')
                        report_tree.column("#0", width=120, minwidth=120, anchor='center')
                        report_tree.heading('Fichier', text='Fichier')
                        report_tree.column("Fichier", width=120, minwidth=120, anchor='center')
                        report_tree.heading("Date", text='Date')
                        report_tree.column("Date", width=120, minwidth=120, anchor='center')
                        report_tree.heading("EnqueteurId", text='EnqueteurId')
                        report_tree.column("EnqueteurId", width=120, minwidth=120, anchor='center')

                        report_tree.pack()

                        # Remplissage de la Treeview avec les rapports
                        for rapport in rapports:
                            # Utilisez seulement les colonnes définies dans la création de report_tree
                            report_tree.insert("", 'end',text=rapport[0], values=(rapport[1], rapport[2], rapport[3]))

                    else:
                        messagebox.showinfo("Information", f"Aucun rapport trouvé pour l'enquête {matricule_enquete}")

                finally:
                    self.conn.close()

        Label(self, text='').pack()
        Label(self, text='Chercher une enquête', fg='dark blue', font=('Arial', 25, 'bold')).pack()
        Label(self, text='').pack()
        Label(self, text='Matricule:', font=('Comic Scan Ms', 14, 'bold')).place(x=260, y=150)
        Entry(self, textvariable=matricule, width=30).place(x=400, y=155)

        self.listTree = ttk.Treeview(self, height=10, columns=('Debut', 'Fin', 'Enqueteur', 'Status', 'Description'))
        self.listTree.heading("#0", text='Matricule', anchor='center')
        self.listTree.column("#0", width=120, minwidth=120, anchor='center')
        self.listTree.heading('Debut', text='Date debut')
        self.listTree.column("Debut", width=120, minwidth=120, anchor='center')
        self.listTree.heading("Fin", text='Date fin')
        self.listTree.column("Fin", width=120, minwidth=120, anchor='center')
        self.listTree.heading("Enqueteur", text='Enqueteur')
        self.listTree.column("Enqueteur", width=120, minwidth=120, anchor='center')
        self.listTree.heading("Status", text='Status')
        self.listTree.column("Status", width=120, minwidth=120, anchor='center')
        self.listTree.heading("Description", text='Description')
        self.listTree.column("Description", width=120, minwidth=120, anchor='center')

        self.listTree.place(x=40, y=280)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))
        Button(self, text="Chercher", font=('Arial', 13, 'bold'), command=search_survey).place(x=350, y=210)

        # Ajout de l'événement de clic pour afficher les rapports
        self.listTree.bind("<ButtonRelease-1>", show_reports)

if __name__ == "__main__":
    Enquete().mainloop()

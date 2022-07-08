import tkinter as tk
from tkinter import ttk
import mysql.connector as mysql

class mainWindow:
    def __init__(self):
        self.cars_list = []
        self.root = tk.Tk()
        self.root.title("CMS Markosian")
        self.get_cars()
        self.gui()
        self.root.mainloop()

    def gui(self):
        # TreeView
        columns = ['RO', 'Make', 'Model', 'Year']
        self.data_tree = ttk.Treeview(self.root, columns=columns, show='headings')

        # Formatting columns to be centered.
        self.data_tree.column('RO', anchor='center')
        self.data_tree.heading('RO', text='RO')
        self.data_tree.column('Make', anchor='center')
        self.data_tree.heading('Make', text='Make')
        self.data_tree.column('Model', anchor='center')
        self.data_tree.heading('Model', text='Model')
        self.data_tree.column('Year', anchor='center')
        self.data_tree.heading('Year', text='Year')

        for car in self.cars_list:
            self.data_tree.insert('', tk.END, values=car)

        #self.data_tree.bind('<<TreeviewSelect>>', self.car_selected)

        self.data_tree.pack()

        self.select_button = tk.Button(self.root, text="Select", command=self.car_selected)
        self.select_button.pack(pady=25,padx=25)

    # Gets all cars from the cars table from Database.
    def get_cars(self):
        conn = mysql.connect(user='mcastre1', password='Mc255587!', host='mysql.migcas21.dreamhosters.com', database='cms_mark_db')
        cursor = conn.cursor()

        query = ("SELECT * FROM Cars")

        cursor.execute(query)

        for (RO, Make, Model, Year) in cursor:
            self.cars_list.append((RO, Make, Model, Year))

        cursor.close()
        conn.close()

    def car_selected(self):
        selected_item = self.data_tree.focus()
        print(f'RO: {self.data_tree.item(selected_item)["values"][0]}')

if __name__ == "__main__":
    mainWindow()

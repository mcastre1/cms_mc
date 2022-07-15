import tkinter as tk
from tkinter import ttk
import mysql.connector as mysql
from car_info import CarInfo
from create_car import CreateCar

class mainWindow:
    USER_NAME = 'mcastre1'
    PASSWORD = 'Mc255587!'
    HOST = 'mysql.migcas21.dreamhosters.com'
    DATABASE = 'cms_mark_db'

    def __init__(self):
        self.conn = None
        self.cars_list = [] # Keep track of cars in database
        self.root = tk.Tk() # Starts new window
        self.root.wm_state(newstate='zoomed')
        self.root.title("CMS Markosian") # Title of the above window
        self.gui() # Sets up all gui widgetsin the main window
        self.root.mainloop() # Listens to events and/or changes in the main window
        

    def gui(self):
        """Sets up the ui in main window"""
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

        # Populates items in TreeView
        self.populate_car_treeview()
        self.data_tree.pack()

        # Button used for selecting a car and opening the info window.
        self.select_button = tk.Button(self.root, text="Select", command=self.car_selected)
        self.select_button.pack(pady=25,padx=25)
        
        # Button used for opening the create car window.
        self.create_button = tk.Button(self.root, text="Add new car", command=self.create_car)
        self.create_button.pack(pady=25, padx=25)

    def get_cars(self):
        """Makes a connection to a remote database and retrieves all cars in it."""
        self.cars_list = []
        self.conn = mysql.connect(user=self.USER_NAME, password=self.PASSWORD, host=self.HOST, database=self.DATABASE)
        cursor = self.conn.cursor()

        query = ("SELECT * FROM Cars")

        cursor.execute(query)
        

        # For every found car in the database we add it to a list.
        for (RO, Make, Model, Year) in cursor:
            self.cars_list.append((RO, Make, Model, Year))

        cursor.close()
        #self.conn.close()

    def populate_car_treeview(self):
        """Populate the actual car tree view."""
        # Used to help make the database connection and retrieve all car rows.
        self.get_cars()

        # Clear off tree view, this serves as a way to later on be able to update the treeview.
        for item in self.data_tree.get_children():
            self.data_tree.delete(item)
        
        # Add all items in the car list to the tree view.
        for car in self.cars_list:
            self.data_tree.insert('', tk.END, values=car)

    def car_selected(self):
        selected_item = self.data_tree.focus()
        ro = self.data_tree.item(selected_item)["values"][0]

        CarInfo(ro, self.USER_NAME, self.PASSWORD, self.HOST, self.DATABASE, self.conn)

    def create_car(self):
        CreateCar(self.USER_NAME, self.PASSWORD, self.HOST, self.DATABASE, self.populate_car_treeview)

if __name__ == "__main__":
    mainWindow()

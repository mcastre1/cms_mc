import tkinter as tk
import mysql.connector as mysql

class CarInfo():
    def __init__(self, RO, USER_NAME, PASSWORD, HOST, DATABASE):
        self.USER_NAME = USER_NAME
        self.PASSWORD = PASSWORD
        self.HOST = HOST
        self.DATABASE = DATABASE
        self.RO = RO
        self.root = tk.Tk()
        self.make = ''
        self.model = ''
        self.year = ''
        self.get_car_info()
        self.init_gui()
    
    def init_gui(self):
        self.ro_label = tk.Label(self.root, text = self.RO)
        self.ro_label.pack(anchor='w', pady=5, padx=10)

        self.make_label = tk.Label(self.root, text=self.make)
        self.make_label.pack(anchor='w', pady=5, padx=10)

        self.model_label = tk.Label(self.root, text=self.model)
        self.model_label.pack(anchor="w", pady=5, padx=10)

        self.year_label = tk.Label(self.root, text=self.year)
        self.year_label.pack(anchor='w',pady=5, padx=10)
        
    def get_car_info(self):
        conn = mysql.connect(user=self.USER_NAME, password=self.PASSWORD, host=self.HOST, database=self.DATABASE)
        cursor = conn.cursor()

        query = (f"SELECT * FROM Cars WHERE RO={self.RO}")

        cursor.execute(query)

        for (RO, Make, Model, Year) in cursor:
            self.make = Make
            self.model = Model
            self.year = Year
            #print(f"{RO}, {Make}, {Model}, {Year}")

        cursor.close()
        conn.close()


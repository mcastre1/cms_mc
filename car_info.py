import tkinter as tk
import mysql.connector as mysql
from sqlalchemy import column
from tkinter import ttk
from parts_widget import PartsWidget
from inspection_widget import Inspection

class CarInfo():
    def __init__(self, RO, USER_NAME, PASSWORD, HOST, DATABASE):
        self.USER_NAME = USER_NAME
        self.PASSWORD = PASSWORD
        self.HOST = HOST
        self.DATABASE = DATABASE
        self.RO = RO
        self.root = tk.Toplevel()
        self.root.wm_state(newstate="zoomed")
        self.make = ''
        self.model = ''
        self.year = ''
        self.get_car_info()
        self.init_gui()
    
    def init_gui(self):
        self.carinfo_lf = tk.LabelFrame(self.root, text="Car Info: ")
        self.carinfo_lf.pack(fill='x')

        self.ro_label = tk.Label(self.carinfo_lf, text = f'RO: {self.RO}')
        self.ro_label.pack(anchor='w', pady=5, padx=10)

        self.make_label = tk.Label(self.carinfo_lf, text=f'Make: {self.make}')
        self.make_label.pack(anchor='w', pady=5, padx=10)

        self.model_label = tk.Label(self.carinfo_lf, text=f'Model: {self.model}')
        self.model_label.pack(anchor="w", pady=5, padx=10)

        self.year_label = tk.Label(self.carinfo_lf, text=f'Year: {self.year}')
        self.year_label.pack(anchor='w',pady=5, padx=10)

        self.tabs_lf = ttk.Notebook(self.root)
        self.tabs_lf.add(PartsWidget(self.tabs_lf), text="Parts")
        self.tabs_lf.add(Inspection(self.tabs_lf, self.USER_NAME, self.PASSWORD, self.HOST, self.DATABASE, self.RO), text="Inspection")

        self.tabs_lf.pack(fill='x')



    def get_car_info(self):
        conn = mysql.connect(user=self.USER_NAME, password=self.PASSWORD, host=self.HOST, database=self.DATABASE)
        cursor = conn.cursor()

        query = (f"SELECT * FROM Cars WHERE RO={self.RO}")

        cursor.execute(query)

        for (RO, Make, Model, Year) in cursor:
            self.make = Make
            self.model = Model
            self.year = Year

        cursor.close()
        conn.close()


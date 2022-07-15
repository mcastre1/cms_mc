import tkinter as tk
from turtle import position
import mysql.connector as mysql
class Inspection(tk.Frame):
    def __init__(self, parent, USER_NAME, PASSWORD, HOST, DATABASE, RO, CONN):
        tk.Frame.__init__(self, parent)

        self.conn = CONN
        self.USER_NAME = USER_NAME
        self.PASSWORD = PASSWORD
        self.HOST = HOST
        self.DATABASE = DATABASE
        self.RO = RO
        self.info = []

        self.get_info()
        self.populate_gui()

    def get_info(self):
        #conn = mysql.connect(user=self.USER_NAME, password=self.PASSWORD, host=self.HOST, database=self.DATABASE)
        cursor = self.conn.cursor()

        query = (f"SELECT * FROM Inspection WHERE RO = {self.RO}")

        cursor.execute(query)

        for item in cursor:
            self.info = list(item)

        cursor.close()
        self.conn.commit()
        #conn.close()

    def populate_gui(self):
        self.inspect_lf = tk.LabelFrame(self, text="Car Inspection: ")
        self.inspect_lf.pack(fill='x')

        self.stock_l = tk.Label(self.inspect_lf, text="Stock: ")
        self.stock_t = tk.Text(self.inspect_lf,height=1, width=15)
        self.stock_t.insert(tk.END, self.info[1])
        self.stock_l.grid(row=0, column=0, padx=5, pady=5)
        self.stock_t.grid(row=0, column=1, padx=5, pady=5)

        self.express_l = tk.Label(self.inspect_lf, text="Express: ")
        self.express_t = tk.Text(self.inspect_lf,height=1, width=15)
        self.express_t.insert(tk.END, self.info[2])
        self.express_l.grid(row=0, column=2, padx=5, pady=5)
        self.express_t.grid(row=0, column=3, padx=5, pady=5)

        self.Inspector_l = tk.Label(self.inspect_lf, text="Inspector: ")
        self.Inspector_t = tk.Text(self.inspect_lf,height=1, width=15)
        self.Inspector_t.insert(tk.END, self.info[3])
        self.Inspector_l.grid(row=0, column=4, padx=5, pady=5)
        self.Inspector_t.grid(row=0, column=5, padx=5, pady=5)

        self.GPSLocates_l = tk.Label(self.inspect_lf, text="GPS Locates: ")
        self.GPSLocates_t = tk.Text(self.inspect_lf,height=1, width=15)
        self.GPSLocates_t.insert(tk.END, self.info[4])
        self.GPSLocates_l.grid(row=1, column=0, padx=5, pady=5)
        self.GPSLocates_t.grid(row=1, column=1, padx=5, pady=5)

        self.body_work_l = tk.Label(self.inspect_lf, text="Body Work Needed: ")
        self.body_work_t = tk.Text(self.inspect_lf,height=1, width=15)
        self.body_work_t.insert(tk.END, self.info[5])
        self.body_work_l.grid(row=1, column=2, padx=5, pady=5)
        self.body_work_t.grid(row=1, column=3, padx=5, pady=5)

        self.working_keys_l = tk.Label(self.inspect_lf, text="Working Keys: ")
        self.working_keys_t = tk.Text(self.inspect_lf,height=1, width=15)
        self.working_keys_t.insert(tk.END, self.info[6])
        self.working_keys_l.grid(row=1, column=4, padx=5, pady=5)
        self.working_keys_t.grid(row=1, column=5, padx=5, pady=5)

        self.inspect_command_lf = tk.LabelFrame(self, text="Update/Save: ")
        self.inspect_command_lf.pack(fill='x')

        self.save_button = tk.Button(self.inspect_command_lf, text="Save", command=self.save)
        self.save_button.pack(side="right")

    def save(self):
        #conn = mysql.connect(user=self.USER_NAME, password=self.PASSWORD, host=self.HOST, database=self.DATABASE)
        cursor = self.conn.cursor()

        query = (f"UPDATE Inspection SET Express = '{self.express_t.get('1.0',tk.END)}',"+
                f"Stock = '{self.stock_t.get('1.0', tk.END)}',"+
                f"Inspector = '{self.Inspector_t.get('1.0',tk.END)}',"+
                f"GPS_Locates = '{self.GPSLocates_t.get('1.0', tk.END)}',"+
                f"Body_Work_Needed = '{self.body_work_t.get('1.0',tk.END)}',"+
                f"Working_Keys = '{self.working_keys_t.get('1.0',tk.END)}' "+
                f"WHERE RO = {self.RO}")

        cursor.execute(query)
        cursor.close()
        self.conn.commit()
        #conn.close()

    def update(self):
        pass
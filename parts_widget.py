import tkinter as tk
import mysql.connector as mysql
from create_part import CreatePart

class PartsWidget(tk.Frame):
    def __init__(self, parent, USER_NAME, PASSWORD, HOST, DATABASE, RO, CONN):
        tk.Frame.__init__(self, parent)

        self.conn = CONN
        self.USER_NAME = USER_NAME
        self.PASSWORD = PASSWORD
        self.HOST = HOST
        self.DATABASE = DATABASE
        self.RO = RO
        self.info = []

        self.RO = RO
        #self.get_info()
        #self.populate_gui()
        self.gui_init()
        self.populate_parts()
        
    def gui_init(self):
        self.parts_lf = tk.LabelFrame(self, text = "Parts: ")
        self.parts_lf.pack(fill='x')

        self.parts_command_lf = tk.LabelFrame(self, text="Update/Save: ")
        self.parts_command_lf.pack(fill='x')

        self.save_button = tk.Button(self.parts_command_lf, text="Save", command=self.save)
        self.save_button.pack(side="right")

    def populate_parts(self):
        #temp = Part(self.parts_lf, "Desc hi!", "location!")
        #temp.pack(fill='x')


        cursor = self.conn.cursor()
        query = (f"SELECT * FROM Parts WHERE RO = {self.RO}")

        cursor.execute(query)

        for item in cursor:
            temp = Part(self.parts_lf, item[1], item[2])
            temp.pack(fill='x')

        cursor.close()
        self.conn.commit()

        self.add_button = tk.Button(self.parts_command_lf, text="Add New", command=self.add_part)
        self.add_button.pack(side='right')

    def add_part(self):
        print(self.conn.is_connected())
        CreatePart(self.RO, self.conn, self.USER_NAME, self.PASSWORD, self.HOST, self.DATABASE, self.update_parts)
        
    def update_parts(self, desc, loc):
        temp = Part(self.parts_lf, desc, loc)
        temp.pack(fill='x')

    def get_info(self):
        #conn = mysql.connect(user=self.USER_NAME, password=self.PASSWORD, host=self.HOST, database=self.DATABASE)
        cursor = self.conn.cursor()

        query = (f"SELECT * FROM Parts WHERE RO = {self.RO}")

        cursor.execute(query)

        for item in cursor:
            self.info = list(item)
            print(item)

        cursor.close()
        self.conn.commit()
        #conn.close()

    def populate_gui(self):
        self.parts_lf = tk.LabelFrame(self, text="Parts: ")
        self.parts_lf.pack(fill='x')

        self.parts_l = tk.Label(self.parts_lf, text="Parts: ")
        self.parts_t = tk.Text(self.parts_lf,height=10, width=40)
        self.parts_t.insert(tk.END, self.info[1])
        self.parts_l.grid(row=0, column=0, padx=5, pady=5)
        self.parts_t.grid(row=0, column=1, padx=5, pady=5)

        self.special_parts_l = tk.Label(self.parts_lf, text="Special Parts: ")
        self.special_parts_t = tk.Text(self.parts_lf,height=10, width=40)
        self.special_parts_t.insert(tk.END, self.info[2])
        self.special_parts_l.grid(row=1, column=0, padx=5, pady=5)
        self.special_parts_t.grid(row=1, column=1, padx=5, pady=5)


        self.parts_command_lf = tk.LabelFrame(self, text="Update/Save: ")
        self.parts_command_lf.pack(fill='x')

        self.save_button = tk.Button(self.parts_command_lf, text="Save", command=self.save)
        self.save_button.pack(fill='x')

        self.add_button = tk.Button(self.parts_command_lf, text="Add New", command=self.add_part)
        self.add_button.pack(fill='x')


    def save(self):
        #conn = mysql.connect(user=self.USER_NAME, password=self.PASSWORD, host=self.HOST, database=self.DATABASE)
        cursor = self.conn.cursor()

        query = (f"UPDATE Parts SET Parts = '{self.parts_t.get('1.0',tk.END)}', Special_Parts = '{self.special_parts_t.get('1.0', tk.END)}' WHERE RO = {self.RO}")

        cursor.execute(query)
        cursor.close()
        self.conn.commit()
        #conn.close()

class Part(tk.Frame):
    def __init__(self, parent, desc, location):
        tk.Frame.__init__(self, parent)
        self.desc = desc
        self.location = location
        self.gui()


    def gui(self):
        self.desc_tb = tk.Text(self, height=1, width=30)
        self.desc_tb.insert(tk.END, self.desc)
        self.loc_tb = tk.Text(self, height=1, width=30)
        self.loc_tb.insert(tk.END, self.location)
        self.desc_tb.grid(row=0,column=0, padx=(0,20), pady=(0,20))
        self.loc_tb.grid(row=0,column=1, padx=(0,20), pady=(0,20))


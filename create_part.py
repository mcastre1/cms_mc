import tkinter as tk
import mysql.connector as mysql

class CreatePart():
    def __init__(self, RO, CONN, USERNAME, PASSWORD, HOST, DATABASE, callback_update_parts):
        self.RO = RO
        self.conn = CONN
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.HOST = HOST
        self.DATABASE = DATABASE
        self.callback_update_parts = callback_update_parts
        self.root = tk.Toplevel()

        print(self.conn.is_connected())

        self.gui_init()

    def gui_init(self):
        self.desc_label = tk.Label(self.root, text="Desc: ")
        self.desc_text = tk.Text(self.root, height=2)

        self.location_label = tk.Label(self.root, text="Location: ")
        self.location_text = tk.Text(self.root, height=2)

        self.add_btn = tk.Button(self.root, text='Add', command=self.add_part)

        self.desc_label.grid(row=0, column=0)
        self.desc_text.grid(row=0, column=1)

        self.location_label.grid(row=1, column=0)
        self.location_text.grid(row=1, column=1)

        self.add_btn.grid(row=2,column=0, columnspan=2)\

    def add_part(self):
        #conn = mysql.connect(user=self.USERNAME, password=self.PASSWORD, host=self.HOST, database=self.DATABASE)

        cursor = self.conn.cursor()

        desc = self.desc_text.get('1.0', tk.END)
        loc = self.location_text.get('1.0', tk.END)

        query = (f"INSERT INTO Parts(RO, Description, Location) VALUES ('{self.RO}', '{desc}', '{loc}')")
        #query = (f"SELECT * FROM Parts")
        cursor.execute(query)

        cursor.close()
        self.conn.commit()

        self.callback_update_parts(desc, loc)
        self.root.destroy()
        

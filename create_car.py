import tkinter as tk
import datetime as dt
from tkinter import ttk

class CreateCar():
    

    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("400x400")
        self.make_options = ['Acura', 'Toyota', 'Chevrolet', 'Subaru', 'GMC', 'Volvo']
        self.current_year = dt.datetime.today().year

        self.gui_init()

    def gui_init(self):
        self.make_option = tk.StringVar()   
        self.make_dropdown = ttk.Combobox(self.root, textvariable=self.make_option)
        self.make_dropdown['values'] = self.make_options
        self.make_dropdown['state'] = 'readonly'
        self.make_dropdown.grid(row=0, column=1, pady=5, padx=10)

        self.make_label = tk.Label(self.root, text="Make: ")
        self.make_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.model_label = tk.Label(self.root, text="Model: ")
        self.model_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.model_entry = tk.Entry(self.root)
        self.model_entry.grid(row=1, column=1, padx=5, pady=5)

        self.year_label = tk.Label(self.root, text="Year: ")
        self.year_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.year_option = tk.StringVar()
        self.year_dropdown = ttk.Combobox(self.root, textvariable=self.year_option)
        self.year_dropdown['values'] = [y for y in range(self.current_year + 1, self.current_year - 100, -1)]
        self.year_dropdown.grid(row=2, column=1, pady=5, padx=5)


if __name__ == "__main__":
    CreateCar()

import tkinter as tk
from turtle import position
class Inspection(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Inspection label!")
        self.label.pack(side="top")
import tkinter as tk

class PartsWidget(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Hi!!!!!!!!!!!!!!", anchor='w')
        self.label.pack(side="top")

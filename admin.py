import tkinter as tk

class Admin_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)

        self.page_name_label = tk.Label(self, text='Strona admina')
        self.page_name_label.grid(column=1, row=0, )
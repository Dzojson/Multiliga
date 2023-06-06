import tkinter as tk
from tkinter.messagebox import showinfo


class Set_New_Password_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)

        self.db = arg_db

        self.page_name_label = tk.Label(self, text='Strona ustawiania hasła')
        self.page_name_label.grid(column=0, row=0, columnspan=2, pady=5)

        #New password data
        self.new_password_label = tk.Label(self, text='Podaj nowe hasło')
        self.new_password_label.grid(column=0, row=1, )

        #New password entry
        self.new_password = tk.StringVar()
        self.new_password_entry = tk.Entry(self,show='*')
        self.new_password_entry.grid(column=1, row=1, pady=5)
        self.new_password_entry.focus()

        #code data
        self.code_label = tk.Label(self, text='Podaj kod z e-maila')
        self.code_label.grid(column=0, row=2, )

        #code entry
        self.code = tk.StringVar()
        self.code_entry = tk.Entry(self,textvariable=self.code)
        self.code_entry.grid(column=1, row=2)
        self.code_entry.focus()
        
        self.confirm_button = tk.Button(self, text='Zatwierdź', command=self.Set_Password)
        self.confirm_button.grid(row=3, column=1,sticky=tk.SE, pady=5)

    def Set_Password(self):
        if self.db.Change_Password(str(self.code_entry.get()), str(self.new_password_entry.get())):
            showinfo(title="Info", message='Hasło zostało zmienione')
            self.master.switch_frame(self.master.page_dic['Start_Page'])
        else:
            showinfo(title="Info", message='Zły kod')

import tkinter as tk
from tkinter.messagebox import showinfo


class Change_Password_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)
        self.user = arg_current_user
        self.db = arg_db

        self.page_name_label = tk.Label(self, text='Zmiana hasła')
        self.page_name_label.grid(column=1, row=0, )

        #Old password data
        self.old_password_label = tk.Label(self, text='Podaj stare hasło')
        self.old_password_label.grid(column=0, row=1, )

        #Old password entry
        self.old_password = tk.StringVar()
        self.old_password_entry = tk.Entry(self, show="*")
        self.old_password_entry.grid(column=1, row=1)
        self.old_password_entry.focus()

        #New password data
        self.new_password_label = tk.Label(self, text='Podaj nowe hasło')
        self.new_password_label.grid(column=0, row=2, )

        #New password entry
        self.new_password = tk.StringVar()
        self.new_password_entry = tk.Entry(self,show='*')
        self.new_password_entry.grid(column=1, row=2)
        self.new_password_entry.focus()

        self.return_button = tk.Button(self, text='Wróć', command=lambda: master.switch_frame(master.page_dic['User_Settings_Page']))
        self.return_button.grid(row=3,column=0)

        self.confirm_button = tk.Button(self, text='Zatwierdź', command=self.Change_Password)
        self.confirm_button.grid(row=3, column=1)

    def Change_Password(self):
        User_Credential = self.db.check_credentials(self.user[0], str(self.old_password_entry.get()))

        if User_Credential:
            self.db.Change_Password_DB(self.user[0],str(self.new_password_entry.get()))
            showinfo(title="Info", message='Zmieniono hasło')
            self.master.switch_frame(self.master.page_dic['User_Page'])
        else:
            showinfo(title="Info", message='Nie poprawne hasło')
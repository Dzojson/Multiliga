import tkinter as tk
from tkinter.messagebox import showinfo

class Delete_Account_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)

        self.db = arg_db
        self.user = arg_current_user

        #password data
        self.password_label = tk.Label(self, text='Podaj hasło')
        self.password_label.grid(column=0, row=1)

        #password entry
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(column=1, row=1,pady=5)
        self.password_entry.focus()

        #confirmation data
        self.confirmation_label = tk.Label(self, text='Wpisz "TAK"')
        self.confirmation_label.grid(column=0, row=2)

        #confirmation entry
        self.confirmation = tk.StringVar()
        self.confirmation_entry = tk.Entry(self,textvariable=self.confirmation)
        self.confirmation_entry.grid(column=1, row=2,pady=5)
        self.confirmation_entry.focus()

        self.confirm_button = tk.Button(self, text='Zatwierdź', command=self.Delete_User)
        self.confirm_button.grid(row=3, column=1,sticky=tk.E)

        self.cancelation_button = tk.Button(self, text='Anuluj', command=lambda: master.switch_frame(master.page_dic['User_Settings_Page']))
        self.cancelation_button.grid(row=3, column=0,sticky=tk.E)

    def Delete_User(self):
        User_Credential = self.db.check_credentials(self.user[0], str(self.password_entry.get()))        

        if User_Credential and str(self.confirmation_entry.get()) == "TAK":
            self.db.Delete_User_DB(self.user[0])
            showinfo(title="Info", message='usunięto konto')
            self.master.switch_frame(self.master.page_dic['Start_Page'])
        elif User_Credential == []:
            showinfo(title="Info", message='Nie poprawne hasło')
        elif str(self.confirmation_entry.get()) != "TAK":
            showinfo(title="Info", message='wpisz ponownie TAK')
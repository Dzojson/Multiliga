import tkinter as tk
from tkinter.messagebox import showinfo

class Start_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)
        
        self.db = arg_db

        self.user_name_label = tk.Label(self, text='Login')
        self.user_name_label.grid(column=0, row=0, )

        #Login entry
        self.user_name = tk.StringVar()
        self.user_name_entry = tk.Entry(self, textvariable=self.user_name)
        self.user_name_entry.grid(column=1, row=0)
        self.user_name_entry.focus()

        self.password_label = tk.Label(self, text='Hasło')
        self.password_label.grid(column=0, row=1, )

        #password entry
        self.password = tk.StringVar()
        self.password_entry =tk.Entry(self, show='*')
        self.password_entry.grid(column=1, row=1)
        self.password_entry.focus()

        self.login_button = tk.Button(self, text='Zaloguj', width= 28, height=2, command=self.login)
        self.login_button.grid(row=2,column=0,columnspan=2,pady=20)

        self.create_account_button = tk.Button(self, text='Stwórz konto', command=lambda: master.switch_frame(master.page_dic['Create_Account_Page']))
        self.create_account_button.grid(row=3,column=0)

        self.remainder_button = tk.Button(self, text='Zapomniałem hasła',width=16, command=lambda: master.switch_frame(master.page_dic['Password_Reminder_Page']))
        self.remainder_button.grid(row=3,column=1)

    def login(self):
        user_name = self.user_name.get()
        password = self.password_entry.get()

        user = self.db.check_credentials(user_name, password)

        if user and user[0][3] == 'zawodnik':
            self.master.current_user = user[0]
            self.master.switch_frame(self.master.page_dic['User_Page'])
        elif user and user[0][3] == 'admin':
            self.master.current_user = user[0]
            self.master.switch_frame(self.master.page_dic['Admin_Page'])
        elif user and (user[0][3] == 'league_menager' or user[0][3] == 'ksiegowa' or user[0][3] == 'event_menager'):
            showinfo(title="Info", message='Aplikacja jest w fazie rozwoju')
            self.master.current_user = user[0]
        else:
            showinfo(title="Info", message='Nie zalogowano')
import tkinter as tk
from tkinter.messagebox import showinfo

class User_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)

        self.db = arg_db
        self.user = arg_current_user

        self.page_name_label = tk.Label(self, text=f'Witaj {self.user[0]}!')
        self.page_name_label.grid(column=1, row=0,pady=30, sticky=tk.N)

        self.User_Games_Page_button = tk.Button(self, text='Moje rozgrywki',width=13,height=5, command=lambda: master.switch_frame(master.page_dic['User_Games_Page']))
        self.User_Games_Page_button.grid(row=1,column=0,padx=5)

        self.User_Settings_Page_button = tk.Button(self, text='Ustawienia konta',width=13,height=5, command=lambda: master.switch_frame(master.page_dic['User_Settings_Page']))
        self.User_Settings_Page_button.grid(row=1,column=1,padx=5)

        self.Start_Page_button = tk.Button(self, text='Wyloguj',width=13,height=5, command=self.Logout)
        self.Start_Page_button.grid(row=1,column=2,padx=5)

    def Logout(self):
        showinfo(title="Info", message='Wylogowano')
        self.master.current_user = None
        self.master.switch_frame(self.master.page_dic['Start_Page'])
        
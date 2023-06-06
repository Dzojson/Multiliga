import tkinter as tk
from tkinter.messagebox import showinfo
from random import randint
from datetime import datetime, timedelta

from mail import MailSender

class Password_Reminder_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)

        self.db = arg_db

        self.page_name_label = tk.Label(self, text='Strona przypominania hasła')
        self.page_name_label.grid(column=0, row=0, columnspan=2)

        #e-mail Data
        self.e_mail_label = tk.Label(self, text='Podaj adres e-mail')
        self.e_mail_label.grid(column=0, row=1, pady=5)

        #e-mail Data entry
        self.e_mail = tk.StringVar()
        self.e_mail_entry = tk.Entry(self, textvariable=self.e_mail)
        self.e_mail_entry.grid(column=1, row=1)
        self.e_mail_entry.focus()

        self.return_button = tk.Button(self, text='Wróć',width=8, command=lambda: master.switch_frame(master.page_dic['Start_Page']))
        self.return_button.grid(row=2,column=0,sticky=tk.E,pady=5)

        self.confirm_button = tk.Button(self, text='Zatwierdź', command=self.Send_Mail)
        self.confirm_button.grid(row=2, column=1, sticky=tk.E)

    def Send_Mail(self):
        if self.db.Get_User_by_Mail(str(self.e_mail_entry.get())):
            Code = randint(1000, 9999)

            self.db.Save_Code_and_Time(Code, datetime.now(), str(self.e_mail_entry.get()))

            ms = MailSender()
            ms.send(f"Subject: Recovery code for MultiligaApp.\n\nYour code is     {Code}.", str(self.e_mail_entry.get()))

            self.master.switch_frame(self.master.page_dic['Set_New_Password_Page'])
        else:
            showinfo(title="Info", message='Nie ma takiego maila')

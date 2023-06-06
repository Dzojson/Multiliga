import tkinter as tk
from tkinter.messagebox import showinfo

class Create_Account_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)

        self.db = arg_db

        #page description
        self.page_name_label = tk.Label(self, text='Strona tworzenia konta',anchor=tk.CENTER)
        self.page_name_label.grid(column=0, row=0, columnspan=2)

        #New user mail data
        self.new_mail_label = tk.Label(self, text='Podaj e-mail')
        self.new_mail_label.grid(column=0, row=1, sticky=tk.E)

        #User mail entry
        self.new_mail = tk.StringVar()
        self.new_mail_entry = tk.Entry(self, textvariable=self.new_mail)
        self.new_mail_entry.grid(column=1, row=1, pady=5)
        self.new_mail_entry.focus()

        #New user login data
        self.new_user_login_label = tk.Label(self, text='Podaj nazwę użytkownika')
        self.new_user_login_label.grid(column=0, row=2, sticky=tk.E)

        #User login entry
        self.new_user_login = tk.StringVar()
        self.new_user_login_entry = tk.Entry(self, textvariable=self.new_user_login)
        self.new_user_login_entry.grid(column=1, row=2, pady=5)
        self.new_user_login_entry.focus()

        #New Password name data
        self.Password_label = tk.Label(self, text='Podaj hasło')
        self.Password_label.grid(column=0, row=3, sticky=tk.E)

        #Password entry
        self.Password = tk.StringVar()   
        self.Password_label_entry = tk.Entry(self, show='*')
        self.Password_label_entry.grid(column=1, row=3, pady=5)
        self.Password_label_entry.focus()

        self.return_button = tk.Button(self, text='Wróć',width=8, command=lambda: master.switch_frame(master.page_dic['Start_Page']))
        self.return_button.grid(row=4,column=1, pady=5,sticky=tk.E)

        self.return_button = tk.Button(self, text='Zatwierdź', command=self.Create_account)
        self.return_button.grid(row=4,column=0, pady=5,sticky=tk.E)

    def Create_account(self):
        if str(self.new_user_login_entry.get()) and str(self.new_mail_entry.get()) and str(self.Password_label_entry.get()) and '@' in str(self.new_mail_entry.get()):
            self.db.Create_account_DB(str(self.new_user_login_entry.get()), str(self.new_mail_entry.get()), str(self.Password_label_entry.get()))
            showinfo(title="Info", message='Pamiętaj o uzupełnieniu informacji w zakładce edycja konta!')
            self.master.switch_frame(self.master.page_dic['Start_Page'])
        elif '@' not in str(self.new_mail_entry.get()):
            showinfo(title="Info", message='Nie poprawny e-mail')
        else:
            showinfo(title="Info", message='Uzupełnij dane')

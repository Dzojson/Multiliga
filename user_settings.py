import tkinter as tk

class User_Settings_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)

        self.page_name_label = tk.Label(self, text='')
        self.page_name_label.grid(row=0,column=0)
        self.Account_Edit_Page_button = tk.Button(self, text='Edytuj konto',height=5,width=13, command=lambda: master.switch_frame(master.page_dic['Account_Edit_Page']))
        self.Account_Edit_Page_button.grid(row=1,column=0,pady=30,padx=5)

        self.Change_Password_Page_button = tk.Button(self, text='Zmiana hasła',height=5,width=13, command=lambda: master.switch_frame(master.page_dic['Change_Password_Page']))
        self.Change_Password_Page_button.grid(row=1,column=1,padx=5)

        self.Delete_Account_Page_button = tk.Button(self, text='Usuń konto',height=5,width=13, command=lambda: master.switch_frame(master.page_dic['Delete_Account_Page']))
        self.Delete_Account_Page_button.grid(row=1,column=2,padx=5)

        self.User_Page_button = tk.Button(self, text='Wstecz',height=2,width=10, command=lambda: master.switch_frame(master.page_dic['User_Page']))
        self.User_Page_button.grid(row=2,column=2)
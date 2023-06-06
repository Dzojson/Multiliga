import tkinter as tk
from db import db_connection

from start import Start_Page
from account_edit import Account_Edit_Page
from change_password import Change_Password_Page
from create_account import Create_Account_Page
from delete_account import Delete_Account_Page
from password_reminder import Password_Reminder_Page
from set_new_password import Set_New_Password_Page
from user_games import User_Games_Page
from user_settings import User_Settings_Page
from user import User_Page

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.page_dic = {'Start_Page': Start_Page, 'Account_Edit_Page': Account_Edit_Page, 'Change_Password_Page': Change_Password_Page, 'Create_Account_Page': Create_Account_Page,
        'Delete_Account_Page': Delete_Account_Page, 'Password_Reminder_Page': Password_Reminder_Page, 'Set_New_Password_Page': Set_New_Password_Page, 'User_Games_Page': User_Games_Page,
        'User_Settings_Page': User_Settings_Page, 'User_Page': User_Page}

        self._frame = None
        self.title('Multiliga')
        self.geometry('640x360')
        self.resizable(False, False)
        
        self.db = db_connection("localhost", "root" ,"mysqlpassword", "ipr_projekt_multiliga")
        self.current_user = None

        self.switch_frame(Start_Page)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self, self.db, self.current_user )
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(width = 640, height=360)
        self._frame.pack(anchor=tk.CENTER)
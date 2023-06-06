import tkinter as tk
from tkinter.messagebox import showinfo

class Account_Edit_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)

        self.db = arg_db
        self.user = arg_current_user

        self.user_info = self.Load()

        #page description
        self.page_name_label = tk.Label(self, text='Edytuj konto')
        self.page_name_label.grid(column=0, row=0, columnspan=2, sticky=tk.N, pady=10)

        #New user name data
        self.new_user_name_label = tk.Label(self, text='Nowe imię użytkownika')
        self.new_user_name_label.grid(column=0, row=1, sticky=tk.E)

        #User name entry
        self.new_user_name = tk.StringVar()
        self.new_user_name_entry = tk.Entry(self, textvariable=self.new_user_name)
        self.new_user_name_entry.insert(0, self.user_info[1])
        self.new_user_name_entry.grid(column=1, row=1,pady=5)
        self.new_user_name_entry.focus()

        #New user surname data
        self.new_user_surname_label = tk.Label(self, text='Nowe nazwisko użytkownika')
        self.new_user_surname_label.grid(column=0, row=2, sticky=tk.E)

        #User surname entry
        self.new_user_surname = tk.StringVar()
        self.new_user_surname_entry = tk.Entry(self, textvariable=self.new_user_surname)
        self.new_user_surname_entry.insert(0, self.user_info[2])
        self.new_user_surname_entry.grid(column=1, row=2,pady=5)
        self.new_user_surname_entry.focus()

        #New weight name data
        self.user_weight_label = tk.Label(self, text='Nowa waga')
        self.user_weight_label.grid(column=0, row=3, sticky=tk.E)

        #Weight entry
        self.user_weight = tk.StringVar()
        self.user_weight_label_entry = tk.Entry(self, textvariable=self.user_weight)
        self.user_weight_label_entry.insert(0, self.user_info[4])
        self.user_weight_label_entry.grid(column=1, row=3,pady=5)
        self.user_weight_label_entry.focus()

        #New height name data
        self.user_height_label = tk.Label(self, text='Nowy wzrost')
        self.user_height_label.grid(column=0, row=4, sticky=tk.E)

        #Height entry
        self.user_height = tk.StringVar()
        self.user_height_entry = tk.Entry(self, textvariable=self.user_height)
        self.user_height_entry.insert(0, self.user_info[3])
        self.user_height_entry.grid(column=1, row=4,pady=5)
        self.user_height_entry.focus()

        #confirm button
        self.confirm_button = tk.Button(self, text='Zatwierdź', command= self.Change)
        self.confirm_button.grid(row=5,column=0)

        #return button
        self.return_button = tk.Button(self, text='Wróć',width=10, command=lambda: master.switch_frame(master.page_dic['User_Settings_Page']))
        self.return_button.grid(row=5,column=1, pady=10)

    def Load(self):
        User_from_db = self.db.get_User(self.user[0])
        User_from_db = User_from_db[0]
        User_from_db = list(User_from_db)
        for i in range(len(User_from_db)):
            if User_from_db[i] is None:
                User_from_db[i] = "uzupełnij tą informacje"
        return(User_from_db)


    def Change(self):
        tmp_height, tmp_weight, tmp_name, tmp_surname = None, None, None, None
        User_from_db = self.db.get_User(self.user[0])
        User_from_db = User_from_db[0]
        try:
            if str(self.user_height.get()) == '':
                tmp_height = User_from_db[3]
                showinfo(title="Info", message='Nie uzupełniłeś wszystkich pól')    
                return
            elif str(self.user_height.get()) and int(self.user_height.get()) > 0:
                tmp_height = str(self.user_height.get())
            elif int(self.user_height.get()) <= 0:
                tmp_height = User_from_db[3]
                showinfo(title="Info", message='Wysokość nie może być ujemna')    
                return
            else:
                tmp_height = User_from_db[3]
        except:
            showinfo(title="Info", message='Błędny format danych')    
            return

        try:
            if str(self.user_weight.get()) == '':
                tmp_height = User_from_db[3]
                showinfo(title="Info", message='Nie uzupełniłeś wszystkich pól')    
                return
            elif str(self.user_weight.get()) and int(self.user_weight.get()) > 0:
                tmp_weight = str(self.user_weight.get())
            elif int(self.user_weight.get()) <= 0:
                tmp_weight = User_from_db[4]
                showinfo(title="Info", message='Waga nie może być ujemna') 
                return  
            else:
                tmp_weight = User_from_db[4]
        except:
            showinfo(title="Info", message='Błędny format danych')    
            return


        if str(self.new_user_name.get()):
            tmp_name = str(self.new_user_name.get())
        else:
            tmp_name = User_from_db[1]

        if str(self.new_user_surname.get()):
            tmp_surname = str(self.new_user_surname.get())
        else:
            tmp_surname = User_from_db[2]


        self.db.Save_Changes(User_from_db[0], tmp_height, tmp_weight, tmp_name, tmp_surname)
        showinfo(title="Info", message='Zmieniono')       
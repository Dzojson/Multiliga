import tkinter as tk

class User_Games_Page(tk.Frame):
    def __init__(self, master, arg_db, arg_current_user):
        super().__init__(master)

        self.db = arg_db
        self.user = arg_current_user

        self.page_name_label = tk.Label(self, text='Moje ligi')
        self.page_name_label.grid(column=0, row=0, )

        self.games_list = tk.Listbox(self,width=50)
        self.games_list.grid(column=0, row=1)
        
        self.title_label = tk.Label(self, text='       Informacje o ligach')
        self.title_label.grid(column=2, row=0, )

        self.info_label = tk.Label(self, text='')
        self.info_label.grid(column=2, row=1,sticky=tk.E)

        self.Load_Info()

        self.games_list.bind("<<ListboxSelect>>", self.Select)
                
        self.User_Page_button = tk.Button(self, text='Wstecz',width=10,height=2, command=lambda: master.switch_frame(master.page_dic['User_Page']))
        self.User_Page_button.grid(row=2,column=2, pady=20, sticky=tk.E)

    def Select(self,event):
        self.info_label = tk.Label(self, text='                                                    \n                                                     \n                                                    \n                                                    \n                                                    ')
        self.info_label.grid(column=2, row=1, )

        selected_indices  = self.games_list.curselection()
        selected_langs = ",".join([self.games_list.get(i) for i in selected_indices])
        league = self.db.Get_League(selected_langs)

        if league[3]:
            msg = f'Dyscyplina: {league[0]}\nLokalozizacja: {league[1]}\nLiczba miejsc: {league[2]}\nCzy opłacone: Tak'
        else:
            msg = f'Dyscyplina: {league[0]}\nLokalozizacja: {league[1]}\nLiczba miejsc: {league[2]}\nCzy opłacone: Nie \nDo zapłaty {league[4]} złotych'
        
        self.info_label = tk.Label(self, text=msg)
        self.info_label.grid(column=2, row=1, sticky=tk.E)

    def Load_Info(self):
        Games = self.db.Load_Info_DB(self.user[0])
        for index, Game in enumerate(Games):
            self.games_list.insert(index, Game[0]) 
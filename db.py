import mysql.connector
from datetime import timedelta

class db_connection():
    def __init__(self, arg_host, arg_user, arg_password, arg_db_name):
        self.connection= mysql.connector.connect(
        port = 3306,
        host = arg_host,
        user = arg_user,
        passwd = arg_password,
        database = arg_db_name
        )
        self.cursor = self.connection.cursor()

    def execute_query(self,query):
        self.cursor.execute(query)
        rows=[]
        for row in self.cursor:
            rows.append(row)
        return(rows)

    def get_users(self):
        users=self.execute_query("select * from uzytkownicy")
        return(users)

    def check_credentials(self,username,password):
        self.cursor.execute("select Login,Imie,Nazwisko,TypUzytkownika from uzytkownicy where Login = %s and Password = %s ",(username,password))
        rows = []
        for row in self.cursor:
            rows.append(row)
        return(rows)

    def get_User(self, username):
        self.cursor.execute("""select u.Login, u.Imie, u.Nazwisko, z.wzrost, z.waga, z.dyscyplina from uzytkownicy u
                            left join zawodnik z on u.id = z.idUzytkownika where u.login = %s""",  (username,))
        rows = []
        for row in self.cursor:
            rows.append(row)
        return(rows)

    def Save_Changes(self, username, height, weight, name, surname):
        self.cursor.execute("UPDATE uzytkownicy SET Imie = %s, Nazwisko = %s WHERE (login = %s)", (name, surname, username))
        self.connection.commit()
        
        self.cursor.execute("select id from uzytkownicy  where Login = %s", (username,))
        userID = []
        for row in self.cursor:
            userID.append(row)
        userID = userID[0][0]
        self.cursor.execute("UPDATE zawodnik SET waga = %s, wzrost = %s WHERE (idUzytkownika = %s)", (weight, height, userID))
        self.connection.commit()

    def Change_Password_DB(self, username, password):
        self.cursor.execute("update uzytkownicy set password = %s WHERE (login = %s)", (password, username))
        self.connection.commit()
    
    def Delete_User_DB(self, username):
        self.cursor.execute("DELETE FROM uzytkownicy WHERE (login = %s);", (username,))
        self.connection.commit()

    def Get_User_by_Mail(self, mail):
        self.cursor.execute("select count(*) from uzytkownicy WHERE (email = %s);", (mail,))
        rows = []
        for row in self.cursor:
            rows.append(row)
        return(rows[0][0])

    def Save_Code_and_Time(self, code, time, mail):
        self.cursor.execute("INSERT INTO kody (kod, timestamp, mail) VALUES (%s, %s, %s)", (code, time, mail))
        self.connection.commit()
    
    def Change_Password(self, code, password):
        self.cursor.execute("select mail from kody where kod = %s and (now()-timestamp) < 600", (code,))

        rows = []
        for row in self.cursor:
            rows.append(row)

        if rows:
            self.cursor.execute("update uzytkownicy set password = %s WHERE (email = %s)", (password, rows[0][0]))
            self.connection.commit()
            return(True)
        else:
            return(False)

    def Load_Info_DB(self, username):
        self.cursor.execute("select id from uzytkownicy where (login = %s)", (username,))

        rows = []
        for row in self.cursor:
            rows.append(row)

        if rows:
            self.cursor.execute("""select  r.nazwa_ligi, r.wpisowe, r.liczba_miejsc from zawodnik z
                                 Left join zawodnikligi zr on z.idzawodnik = zr.idzawodnik 
                                 left join ligi r on zr.idligi = r.id_ligi where z.idUzytkownika = %s;""", (rows[0][0],))
            rows = []
            for row in self.cursor:
                rows.append(row)
            return(rows)
        else:
            return(False)
    
    def Get_League(self, name):
        self.cursor.execute("select l.dyscyplina, l.Lokalizacja, l.liczba_miejsc, zl.czyoplacone, l.wpisowe from ligi l join zawodnikligi zl on l.id_ligi = zl.idligi where (nazwa_ligi = %s);", (name,))
        rows = []
        for row in self.cursor:
            rows.append(row)
        return(rows[0])

    def Create_account_DB(self, username, email, password):
        self.cursor.execute("INSERT INTO uzytkownicy (TypUzytkownika, email, Login, Password) VALUES ('zawodnik', %s, %s, %s)", (email, username, password))
        self.connection.commit()
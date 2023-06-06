import smtplib

class MailSender():
    def __init__(self):
        self.user="mail.sender.pythonscript@gmail.com"
        self.password="avwrlrgxtggcxtov"
        self.message="Subject: This is a test email.\n\nThis is the body of the test email."
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.user, self.password)

    def send(self,message,receiver):
        self.server.sendmail(self.user, receiver, message)
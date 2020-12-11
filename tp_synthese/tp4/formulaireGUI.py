from tkinter import * 
import tkinter
from tkinter import messagebox
from formulaire import login as LL

class formulaireGUI:
    def __init__(self,conn):
        self.root = Tk()  
        self.__login = ""
        self.__password = ""
        self.connx = conn

    @property
    def login(self):
        return self.__login
    
    @property
    def password():
        return self.__password

    @login.setter
    def login(self,a):
        self.__login = a
    
    @password.setter
    def password(self,s):
        self.__password = s

    def lanceGUI(self):
        self.root.title("Formulaire de login")
        self.root.geometry("400x400")
        self.widget_first = Label(self.root, text="Hello user !!" )

        self.login_entry = tkinter.StringVar()
        self.widget_login = Entry(self.root, textvariable=self.login_entry )

        self.password_entry = tkinter.StringVar()
        self.widget_mpd = Entry(self.root, textvariable=self.password_entry )

        self.submitButton = Button(self.root, text="Submit", command=self.submit)    


        self.widget_first.pack()  
        self.widget_login.pack()  
        self.widget_mpd.pack()
        self.submitButton.pack()

    def submit(self):
        if LL(self.connx,self.login_entry,self.password_entry) is True:
            messagebox.showinfo("Coool !!","you are recognized in our DevOps DataBase")
        else:
            messagebox.showerror("Opps ::!", "You're not in our DevOps DataBase  !!")



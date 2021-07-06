# Thabo Setsubi Class 2
# Register new accounts page

from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

register = Tk()
register.geometry("650x650")
register.title("Register New Account")
register.config(bg="#222222")


class AddNewAccount:

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffffff")
        self.frame.place(x=10, y=10, height=500, width=500)
        # Labels
        self.head_lab1 = Label(self.frame, text="LCA / LCS Login: ", font="arial 25", bg="#ffffff")
        self.head_lab1.place(x=20, y=10)
        self.user_lab1 = Label(self.frame, text="Name: ")
        self.user_lab1.place(x=20, y=100)
        self.pass_lab1 = Label(self.frame, text="Password: ")
        self.pass_lab1.place(x=20, y=130)
        # Entries
        self.user_entry = Entry(self.frame)
        self.user_entry.place(x=80, y=100)
        self.pass_entry = Entry(self.frame)
        self.pass_entry.place(x=80, y=130)
        # Buttons
        self.login_btn = Button(self.frame, text="Login")
        self.login_btn.place(x=20, y=180)
        self.return_btn = Button(self.frame, text="Return To Main Page", command=self.return_to_main)
        self.return_btn.place(x=80, y=180)

    # Function Returning to the main page
    def return_to_main(self):
        register.destroy()
        import main


AddNewAccount(register)
register.mainloop()

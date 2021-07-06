# Thabo Setsubi Class 2
# Visitors Page

from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

visit = Tk()
visit.geometry("650x650")
visit.title("Visitors Login Page")
visit.config(bg="#222222")


class GuestLogin:

    def __init__(self, master):
        # Frames
        self.frame = Frame(master, bg="#ffffff")
        self.frame.place(x=10, y=10, height=500, width=500)
        # Labels
        self.head_lab1 = Label(self.frame, text="LC Guests Login: ", font="arial 25", bg="#ffffff")
        self.head_lab1.place(x=20, y=10)
        self.name_lab1 = Label(self.frame, text="Name: ")
        self.name_lab1.place(x=20, y=100)
        self.last_lab1 = Label(self.frame, text="Surname: ")
        self.last_lab1.place(x=20, y=130)
        self.id_label = Label(self.frame, text="ID Number: ")
        self.id_label.place(x=20, y=160)
        self.phone_lab1 = Label(self.frame, text="Phone Number: ")
        self.phone_lab1.place(x=20, y=190)
        self.next_kin_lab1 = LabelFrame(self.frame, text="Next of kin Details: ")
        self.next_kin_lab1.place(x=20, y=230, height=100, width=300)
        self.kinname_lab1 = Label(self.frame, text="Name: ")
        self.kinname_lab1.place(x=25, y=250)
        self.kinnumber_lab1 = Label(self.frame, text="Phone Number: ")
        self.kinnumber_lab1.place(x=25, y=280)
        # Entries
        self.name_entry = Entry(self.frame)
        self.name_entry.place(x=115, y=100)
        self.last_entry = Entry(self.frame)
        self.last_entry.place(x=115, y=130)
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=115, y=160)
        self.cell_entry = Entry(self.frame)
        self.cell_entry.place(x=115, y=190)
        self.kin_entry1 = Entry(self.frame)
        self.kin_entry1.place(x=115, y=250)
        self.kin_entry2 = Entry(self.frame)
        self.kin_entry2.place(x=115, y=280)
        # Buttons
        self.login_btn = Button(self.frame, text="Login")
        self.login_btn.place(x=20, y=350)
        self.return_btn = Button(self.frame, text="Return To Main Page", command=self.return_to_main)
        self.return_btn.place(x=80, y=350)

    # Function Returning to the main page
    def return_to_main(self):
        visit.destroy()
        import main


GuestLogin(visit)
visit.mainloop()

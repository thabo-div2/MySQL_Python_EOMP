# Main Page for admin to see and remove users
import mysql.connector as mysql
from tkinter import *
from tkinter import ttk

w = Tk()
w.title("Admin Page")
w.geometry("650x650")
w.config(bg="#222222")


class AdminControl:

    c = ["Id", "Name", "Department", "Date_entered", "Time_entered", "Time_exit"]

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffffff", bd=10, highlightbackground="aqua", highlightthickness=10)
        self.frame.place(x=10, y=10, height=500, width=500)
        # Labels
        self.admin_head = Label(master, text="Attendance: ", font="arial 20")
        self.admin_head.place(x=20, y=20)
        # Treeview
        self.admin_tv = ttk.Treeview(master)
        self.admin_tv['columns'] = self.c
        self.admin_tv.column("#0", width=0, stretch=NO)
        self.admin_tv.column("Id", anchor=CENTER, width=80)
        self.admin_tv.column("Name", anchor=CENTER, width=80)
        self.admin_tv.column("Department", anchor=CENTER, width=80)
        self.admin_tv.column("Date_entered", anchor=CENTER, width=80)
        self.admin_tv.column("Time_entered", anchor=CENTER, width=80)
        self.admin_tv.column("Time_exit", anchor=CENTER, width=80)
        self.admin_tv.heading("#0", text="", anchor=CENTER)
        self.admin_tv.heading("Id", text="ID", anchor=CENTER)
        self.admin_tv.heading("Name", text="Name", anchor=CENTER)
        self.admin_tv.heading("Department", text="Department", anchor=CENTER)
        self.admin_tv.heading("Date_entered", text="Date", anchor=CENTER)
        self.admin_tv.heading("Time_entered", text="Time In", anchor=CENTER)
        self.admin_tv.heading("Time_exit", text="Time Out", anchor=CENTER)
        self.db = mysql.connect(
            host="localhost",
            user="root",
            passwd="Grimmijow06",
            database="lifechoicesdb2"
        )

        self.cursor = self.db.cursor()
        self.query = "Select stud_id, name, title, date_entered, date_time_entered, time_exit FROM students"
        self.cursor.execute(self.query)

        self.rows = self.cursor.fetchall()

        for i in self.rows:
            self.admin_tv.insert("", "end", values=i)

        self.admin_tv.place(x=20, y=80)


AdminControl(w)
w.mainloop()

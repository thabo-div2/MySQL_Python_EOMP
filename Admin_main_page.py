# Main Page for admin to see and remove users
import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

w = Tk()
w.title("Admin Page")
w.geometry("650x650")
w.config(bg="#222222")


class AdminControl:

    c = ["Id", "Name", "Department", "Date_entered", "Time_entered", "Time_exit"]

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffffff", bd=10, highlightbackground="aqua", highlightthickness=10)
        self.frame.place(x=10, y=10, height=500, width=600)
        # Labels
        self.admin_head = Label(master, text="Attendance: ", font="arial 20")
        self.admin_head.place(x=20, y=20)
        # Buttons
        self.delete_user = Button(self.frame, text="Delete User", command=self.delete_user_func)
        self.delete_user.place(x=10, y=300)
        self.grant_btn = Button(self.frame, text="Grant Privileges")
        self.grant_btn.place(x=120, y=300)
        # Treeview
        self.admin_tv = ttk.Treeview(master, selectmode="browse")
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

        self.cursor = self.db.cursor(buffered=True)
        self.query = "Select stud_id, name, title, date_entered, date_time_entered, time_exit FROM students"
        self.cursor.execute(self.query)

        self.rows = self.cursor.fetchall()

        for i in self.rows:
            self.admin_tv.insert("", "end", values=i)

        self.cursor = self.db.cursor(buffered=True)
        self.query2 = "Select admin_id, name, title, date_entered, date_time_entered, time_exit FROM students"
        self.cursor.execute(self.query)

        self.rows2 = self.cursor.fetchall()

        for j in self.rows2:
            self.admin_tv.insert("", "end", values=j)

        self.admin_tv.place(x=20, y=80)
        # # Scrollbar
        # self.admin_sb = Scrollbar(self.frame, orient=VERTICAL)
        # self.admin_sb.pack(side=RIGHT, fill=Y)
        #
        # self.admin_tv.config(yscrollcommand=self.admin_sb.set)
        # self.admin_sb.config(command=self.admin_tv.yview)

    def delete_user_func(self):
        try:
            sql = "DELETE FROM students WHERE name = %s"
            choice = self.admin_tv.focus()
            temp = self.admin_tv.item(choice, "values")
            print(temp[2])
            self.cursor.executemany(sql, temp)
            self.db.commit()
            messagebox.showinfo("Status", "Successfully deleted")

        except mysql.Error as err:  # This except statement will catch all mysql errors
            messagebox.showerror("Error", "Something went wrong: " + str(err))


AdminControl(w)
w.mainloop()

# Main Page for admin to see and remove users
import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

w = Tk()
w.title("Admin Page")
w.geometry("650x650")
w.config(bg="#222222")


class AdminControl:

    c = ["Id", "Name", "Department", "Date_entered", "Time_entered", "Time_exit"]
    list = ["Id", "Name", "Surname", "Phone_num", "Kin_name", "Kin_num", "Date_entered", "ID_Card"]

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffffff", bd=10, highlightbackground="aqua", highlightthickness=10)
        self.frame.place(x=10, y=10, height=700, width=700)
        # Labels
        self.admin_head = Label(master, text="Attendance: ", font="arial 20")
        self.admin_head.place(x=20, y=20)
        self.count_lab1 = Label(self.frame, text="", bg="#ffffff")
        self.count_lab1.place(x=300, y=300)
        # Buttons
        self.delete_user = Button(self.frame, text="Delete User", command=self.delete_user_func)
        self.delete_user.place(x=10, y=300)
        self.grant_btn = Button(self.frame, text="Grant Privileges", command=self.grant_privileges)
        self.grant_btn.place(x=90, y=300)
        self.count_btn = Button(self.frame, text="Count", command=self.count_func)
        self.count_btn.place(x=190, y=300)
        self.leave_btn = Button(self.frame, text="Leave", command=w.destroy)
        self.leave_btn.place(x=240, y=300)
        # Treeview
        self.admin_tv = ttk.Treeview(master, selectmode="browse")
        self.admin_tv['columns'] = self.c
        self.admin_tv.column("#0", width=0, stretch=NO)
        self.admin_tv.column("Id", anchor=CENTER, width=80)
        self.admin_tv.column("Name", anchor=CENTER, width=80)
        self.admin_tv.column("Department", anchor=CENTER, width=80)
        self.admin_tv.column("Date_entered", anchor=CENTER, width=80)
        self.admin_tv.column("Time_entered", anchor=CENTER, width=180)
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
        self.query2 = "Select admin_id, name, title, date_entered, date_time_entered, time_exit FROM admin"
        self.cursor.execute(self.query2)

        self.rows2 = self.cursor.fetchall()

        for j in self.rows2:
            self.admin_tv.insert("", "end", values=j)

        self.admin_tv.place(x=20, y=80)

        self.guest_tv = ttk.Treeview(master, selectmode="browse")
        self.guest_tv['columns'] = self.list
        self.guest_tv.column("#0", width=0, stretch=NO)
        self.guest_tv.column("Id", anchor=CENTER, width=40)
        self.guest_tv.column("Name", anchor=CENTER, width=80)
        self.guest_tv.column("Surname", anchor=CENTER, width=80)
        self.guest_tv.column("Phone_num", anchor=CENTER, width=80)
        self.guest_tv.column("Kin_name", anchor=CENTER, width=80)
        self.guest_tv.column("Kin_num", anchor=CENTER, width=80)
        self.guest_tv.column("Date_entered", anchor=CENTER, width=80)
        self.guest_tv.column("ID_Card", anchor=CENTER, width=80)
        self.guest_tv.heading("#0", text="", anchor=CENTER)
        self.guest_tv.heading("Id", text="#GID", anchor=CENTER)
        self.guest_tv.heading("Name", text="Name", anchor=CENTER)
        self.guest_tv.heading("Surname", text="Surname", anchor=CENTER)
        self.guest_tv.heading("Phone_num", text="Phone Number", anchor=CENTER)
        self.guest_tv.heading("Kin_name", text="Next of Kin's Name", anchor=CENTER)
        self.guest_tv.heading("Kin_num", text="Next of Kin's Number", anchor=CENTER)
        self.guest_tv.heading("Date_entered", text="Date Entered", anchor=CENTER)
        self.guest_tv.heading("ID_Card", text="ID Number", anchor=CENTER)
        self.query3 = "Select id_num, name, surname, phone_num, kin_name, kin_num, date_entered, id_card FROM guest"
        self.cursor.execute(self.query3)

        self.rows3 = self.cursor.fetchall()

        for k in self.rows3:
            self.guest_tv.insert("", "end", values=k)

        self.guest_tv.place(x=20, y=400)

        # Scrollbar
        self.admin_sb = Scrollbar(self.frame, orient=VERTICAL)
        self.admin_sb.place(x=600, y=40, height=200)

        self.admin_tv.config(yscrollcommand=self.admin_sb.set)
        self.admin_sb.config(command=self.admin_tv.yview)

        self.guest_sb = Scrollbar(self.frame, orient=VERTICAL)
        self.guest_sb.place(x=600, y=400, height=200)

        self.guest_tv.config(yscrollcommand=self.guest_sb.set)
        self.guest_sb.config(command=self.guest_tv.yview)

    def delete_user_func(self):
        try:
            db = mysql.connect(
                host="localhost",
                user="root",
                passwd="Grimmijow06",
                database="lifechoicesdb2"
            )

            cursor = db.cursor(buffered=True)

            sql = "DELETE FROM students WHERE stud_id=%s"
            choice = self.admin_tv.selection()[0]
            temp = self.admin_tv.item(choice)["values"][0]
            cursor.execute(sql, (temp,))
            db.commit()
            self.admin_tv.delete(choice)
            messagebox.showinfo("Status", str(cursor.rowcount) + " row(s) deleted")
            messagebox.showinfo("Status", "Successfully deleted")

        except mysql.Error as err:  # This except statement will catch all mysql errors
            messagebox.showerror("Error", "Something went wrong: " + str(err))

    def grant_privileges(self):
        try:
            db = mysql.connect(
                host="localhost",
                user="root",
                passwd="Grimmijow06",
                database="lifechoicesdb2"
            )

            cursor = db.cursor(buffered=True)

            query = "INSERT INTO admin SELECT * FROM students WHERE stud_id=%s"
            query2 = "DELETE FROM students WHERE stud_id=%s"

            choice = self.admin_tv.selection()[0]
            temp = self.admin_tv.item(choice)["values"][0]
            n = self.admin_tv.item(choice)["values"][1]
            cursor.execute(query, (temp,))
            db.commit()
            cursor.execute(query2, (temp,))
            db.commit()
            messagebox.showinfo("STATUS", "You have been granted admin privileges " + n)

        except mysql.Error as err:  # This except statement will catch all mysql errors
            messagebox.showerror("Error", "Something went wrong: " + str(err))

    def count_func(self):
        try:
            db = mysql.connect(
                host="localhost",
                user="root",
                passwd="Grimmijow06",
                database="lifechoicesdb2"
            )

            cursor = db.cursor(buffered=True)

            dt = datetime.today()

            now = dt.strftime("%Y-%m-%d")

            sql2 = "SELECT COUNT(stud_ID) AS date_entered FROM students WHERE date_entered = %s"

            cursor.execute(sql2, (now,))

            r = cursor.fetchall()

            sql3 = "SELECT COUNT(admin_id) AS date_entered FROM admin WHERE date_entered = %s"

            cursor.execute(sql3, (now,))

            t = cursor.fetchall()

            sql4 = "SELECT COUNT(id_num) AS date_entered FROM guest WHERE date_entered = %s"

            cursor.execute(sql4, (now,))

            z = cursor.fetchall()

            ans = sum(r[0]) + sum(t[0]) + sum(z[0])

            s = "There is " + str(ans) + " person/people currently in the building"

            self.count_lab1.config(text=s, font="italics 13")

        except mysql.Error as err:  # This except statement will catch all mysql errors
            messagebox.showerror("Error", "Something went wrong: " + str(err))


AdminControl(w)
w.mainloop()

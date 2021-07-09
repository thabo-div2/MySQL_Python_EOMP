# Class 2 Thabo Setsubi
# Sign up page for LCS and LCA

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import mysql.connector as mysql

students = Tk()
students.geometry("650x650")
students.title("LCA/LCS Login Page")
students.config(bg="#222222")


def admin_func2(event):
    students.destroy()
    import admin_page


class StudentsLogin:

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffffff", highlightbackground="green", highlightthickness=10)
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
        self.pass_entry = Entry(self.frame, show="*")
        self.pass_entry.place(x=80, y=130)
        # Buttons
        self.login_btn = Button(self.frame, text="Login", command=self.login_func)
        self.login_btn.place(x=20, y=180)
        self.return_btn = Button(self.frame, text="Return To Main Page", command=self.return_to_main)
        self.return_btn.place(x=150, y=180)
        self.admin_btn = Button(self.frame, text="Admin Login", command=self.admin_func, bg="#ffffff", fg="#222222")
        self.admin_btn.place(x=65, y=180)
        # Combobox
        self.titles_cb = ttk.Combobox(self.frame)
        self.titles = ["Admin", "LCA", "LCS"]
        self.titles_cb['values'] = self.titles
        self.titles_cb['state'] = "readonly"
        self.titles_cb.set("Select Department")
        self.titles_cb.place(x=100, y=160)

    # Function to login the student/employee
    def login_func(self):
        try:
            db = mysql.connect(
                host="localhost",
                user="root",
                passwd="Grimmijow06",
                database="lifechoicesdb2"
            )

            cursor = db.cursor(buffered=True)
            cursor.execute("Select * from students")

            if self.user_entry.get() == "" or self.pass_entry.get() == "":
                messagebox.showerror("Error!", "Fill in all fields")
            for i in cursor:
                if self.user_entry.get() == i[1] and self.pass_entry.get() == i[2]:
                    messagebox.showinfo("STATUS", "Access Granted")
                    cursor.execute("UPDATE students SET date_entered = curdate()")
                    db.commit()
                    cursor.execute("UPDATE students SET date_time_entered = curtime()")
                    db.commit()
                    students.destroy()
                    import LC_Page2
            else:
                messagebox.showerror("ERROR", "Access Denied")

        except mysql.Error as err:  # This except statement will catch all mysql errors
            messagebox.showerror("Error", "Something went wrong: " + str(err))

        except TypeError:
            pass

    def admin_func(self):
        messagebox.showinfo("Status", "Do you know you can press Control + a to switch to admin page")
        students.destroy()
        import admin_page

    # Function Returning to the main page
    def return_to_main(self):
        students.destroy()
        import main


students.bind("<Control-a>", admin_func2)
StudentsLogin(students)
students.mainloop()

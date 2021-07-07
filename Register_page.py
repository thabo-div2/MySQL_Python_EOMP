# Thabo Setsubi Class 2
# Register new accounts page

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as mysql
from datetime import datetime

register = Tk()
register.geometry("650x650")
register.title("Register New Account")
register.config(bg="#222222")


def admin_func2(event):
    register.destroy()
    import admin_page


class AddNewAccount:

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffffff", bd=10, highlightbackground="aqua", highlightthickness=10)
        self.frame.place(x=10, y=10, height=500, width=500)
        # Labels
        self.head_lab1 = Label(self.frame, text="Add New User: ", font="arial 25", bg="#ffffff")
        self.head_lab1.place(x=20, y=10)
        self.name_lab1 = Label(self.frame, text="Name: ")
        self.name_lab1.place(x=20, y=100)
        self.pass_lab1 = Label(self.frame, text="Password: ")
        self.pass_lab1.place(x=20, y=130)
        self.titles_lab = Label(self.frame, text="Department: ")
        self.titles_lab.place(x=20, y=160)
        # Entries
        self.name_entry = Entry(self.frame)
        self.name_entry.place(x=80, y=100)
        self.pass_entry = Entry(self.frame, show="*")
        self.pass_entry.place(x=80, y=130)
        # Buttons
        self.login_btn = Button(self.frame, text="Add New User", command=self.register_func)
        self.login_btn.place(x=20, y=220)
        self.return_btn = Button(self.frame, text="Return To Main Page", command=self.return_to_main)
        self.return_btn.place(x=120, y=220)
        # Combobox
        self.titles_cb = ttk.Combobox(self.frame)
        self.titles = ["Admin", "LCA", "LCS"]
        self.titles_cb['values'] = self.titles
        self.titles_cb['state'] = "readonly"
        self.titles_cb.set("Select Department")
        self.titles_cb.place(x=100, y=160)

    # Function Adding new users
    def register_func(self):
        try:
            db = mysql.connect(
                host="localhost",
                user="root",
                passwd="Grimmijow06",
                database="lifechoicesdb2"
            )

            today = datetime.today()

            cursor = db.cursor()

            if self.titles_cb.get() == "LCA" or self.titles_cb.get() == "LCS":
                query = "INSERT INTO students (name, password, date, title) VALUES (%s, %s, %s, %s)"

                values = (self.name_entry.get(), self.pass_entry.get(), today, self.titles_cb.get())

                cursor.execute(query, values)
                db.commit()

                messagebox.showinfo("Status", "You have successfully registered a new account at Life Choices")

            elif self.titles_cb.get() == "Admin":  # Registering New admin
                query = "INSERT INTO admin (name, password, date, title) VALUES (%s, %s, %s, %s)"

                values = (self.name_entry.get(), self.pass_entry.get(), today, self.titles_cb.get())

                cursor.execute(query, values)
                db.commit()

                messagebox.showinfo("Status", "You have successfully registered a new admin account at Life Choices")

        except mysql.Error as err:  # This except statement will catch all mysql errors
            messagebox.showerror("Error", "Something went wrong: " + str(err))

    def admin_func(self):
        messagebox.showinfo("Status", "Do you know you can press Control + a to switch to admin page")
        register.destroy()
        import admin_page

    # Function Returning to the main page
    def return_to_main(self):
        register.destroy()
        import main


register.bind("<Control-a", admin_func2)
AddNewAccount(register)
register.mainloop()

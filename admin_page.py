# Thabo Setsubi Class 2
# Importing libraries
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

window = Tk()
window.geometry("650x650")
window.title("Admin Login")
window.config(bg="#222222")


class AdminPage:

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffffff", highlightbackground="#000000", highlightthickness=10)
        self.frame.place(x=10, y=10, height=500, width=500)
        # Labels
        self.head_lab1 = Label(self.frame, text="Admin Login: ", font="arial 25", bg="#ffffff")
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
        self.return_btn.place(x=160, y=180)
        self.register_btn = Button(self.frame, text="Register Admin", command=self.new_user)
        self.register_btn.place(x=65, y=180)

    def login_func(self):
        try:
            db = mysql.connect(
                host="localhost",
                user="root",
                passwd="Grimmijow06",
                database="lifechoicesdb2"
            )

            cursor = db.cursor()
            cursor.execute("Select * from admin")
            if self.user_entry.get() == "" or self.pass_entry.get() == "":
                messagebox.showerror("Error!", "Fill in all fields")
            for i in cursor:
                if self.user_entry.get() == i[1] and self.pass_entry.get() == i[2]:
                    messagebox.showinfo("STATUS", "Access Granted")
                    cursor.execute("UPDATE admin SET date_entered = curdate()")
                    db.commit()
                    cursor.execute("UPDATE admin SET date_time_entered = curtime()")
                    db.commit()
                    window.destroy()
                    import Admin_main_page
            else:
                messagebox.showerror("ERROR", "Access Denied")

        except mysql.Error as err:  # This except statement will catch all mysql errors
            messagebox.showerror("Error", "Something went wrong: " + str(err))

    def new_user(self):
        window.destroy()
        import admin_register_page

    # Function Returning to the main page
    def return_to_main(self):
        window.destroy()
        import main


AdminPage(window)
window.mainloop()

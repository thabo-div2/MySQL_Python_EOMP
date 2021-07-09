# Page just for signing out
import mysql.connector as mysql
from tkinter import *
from tkinter import messagebox

choice = Tk()
choice.title("LC Page")
choice.geometry("650x650")
choice.config(bg="#222222")


class LCSignOut:

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffffff")
        self.frame.place(x=10, y=10, width=500, height=500)
        # Label
        self.heading = Label(self.frame, text="Welcome! Logout Page", font="arial 20")
        self.heading.place(x=20, y=10)
        self.user_lab1 = Label(self.frame, text="Name: ")
        self.user_lab1.place(x=20, y=100)
        self.pass_lab1 = Label(self.frame, text="Password: ")
        self.pass_lab1.place(x=20, y=130)
        # Entries
        self.user_entry = Entry(self.frame)
        self.user_entry.place(x=80, y=100)
        self.pass_entry = Entry(self.frame, show="*")
        self.pass_entry.place(x=80, y=130)
        # Button
        self.sign_out = Button(self.frame, text="Sign Out!", command=self.signing_out)
        self.sign_out.place(x=20, y=200)

    def signing_out(self):
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
                    messagebox.showinfo("STATUS", "Bye!!! Enjoy Your Day")
                    cursor.execute("UPDATE students SET time_exit = CURTIME()")
                    db.commit()
                    choice.destroy()

        except mysql.Error as err:  # This except statement will catch all mysql errors
            messagebox.showerror("Error", "Something went wrong: " + str(err))

        except TypeError:
            pass


LCSignOut(choice)
choice.mainloop()

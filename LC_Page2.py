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
        self.heading = Label(self.frame, text="Welcome!", font="arial 20")
        self.heading.place(x=20, y=10)
        # Button
        self.sign_out = Button(self.frame, text="Sign Out!")
        self.sign_out.place(x=20, y=100)

    def signing_out(self):
        try:
            db = mysql.connect(
                host="localhost",
                user="root",
                passwd="Grimmijow06",
                database="lifechoicesdb2"
            )

            cursor = db.cursor(buffered=True)

        except mysql.Error as err:  # This except statement will catch all mysql errors
            messagebox.showerror("Error", "Something went wrong: " + str(err))


LCSignOut(choice)
choice.mainloop()

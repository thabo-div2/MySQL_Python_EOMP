# MySQL Project
# Thabo Setsubi Class 2

# Importing modules that will be needed
from tkinter import *


# Making a tkinter window

root = Tk()
root.title("LifeChoices Login Page")
root.geometry("650x650")
root.config(bg="#222222")


class LifeLogin:

    def __init__(self, master):
        # Frames
        self.frame = Frame(master, bg="#ffffff")
        self.frame.place(x=10, y=10, width=500, height=500)

        # Labels
        self.heading = Label(self.frame, text="Welcome to Life Choices", font="arial 25", bg="#ffffff")
        self.heading.place(x=20, y=10)

        # Buttons
        self.login_btn = Button(self.frame, text="LCA/LCS Login", command=self.login_func, bg="green", fg="#ffffff")
        self.login_btn.place(x=20, y=190)
        self.admin_btn = Button(self.frame, text="Admin Login", command=self.admin_func, bg="#ffffff", fg="#222222")
        self.admin_btn.place(x=115, y=190)
        self.visitors_btn = Button(self.frame, text="Guests Enter Here", command=self.visit_func, bg="#ffff00", fg="#000000")
        self.visitors_btn.place(x=200, y=190)

        self.exit_btn = Button(self.frame, text="Exit", command=self.exit_func, bg="#ed2d34", fg="#ffffff")
        self.exit_btn.place(x=370, y=190)

    def login_func(self):
        root.destroy()
        import LC_page

    def admin_func(self):
        root.destroy()
        import admin_page

    def visit_func(self):
        root.destroy()
        import guest_page


    def exit_func(self):
        return root.destroy()


LifeLogin(root)
root.mainloop()

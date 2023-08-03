'''
Task no. 3
language: Python

'''




from tkinter import *
from tkinter import messagebox
import random
import string


class PasswordGenerator:

    def __init__(self, window):
        self.window = window

        self.window.title("Password Generator")
        self.top_label=Label(self.window, text="Password Generator", height=2,
              font=" Ariel 20 bold", bg="wheat1")
        self.top_label.pack(pady=5, fill=X)

        self.username_label = Label(
            window, text="User Name:", font=" Ariel 15", bg="wheat1")
        self.username_label.pack(pady=5, fill=X)
        self.username_entry = Entry(window)
        self.username_entry.pack(pady=5)
        self.username_entry.focus()

        
        self.password_length_label = Label(
            window, text="Password Length:", font=" Ariel 15", bg="wheat1")
        self.password_length_label.pack(pady=5)
        self.password_length_entry = Entry(window)
        self.password_length_entry.pack(pady=5)

        
        self.password_display_label = Label(
            window, text="Generated Password:", font=" Ariel 15", bg="wheat1")
        self.password_display_label.pack(pady=5)
        self.password_display = Text(window, width=30, height=3)
        self.password_display.pack(pady=5)

        
        self.generate_button = Button(
            window, width=20, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.reset_button = Button(
            window, width=20, text="Reset", command=self.reset)
        self.reset_button.pack()
        window.bind("<Return>", lambda event: self.generate_button.invoke())
        window.bind("<BackSpace>", lambda event: self.reset_button.invoke())
        self.start_animation()

    def generate_password(self):
        try:
            length = int(self.password_length_entry.get())
            if length <= 0:
                messagebox.showerror(
                    "Error", "Please enter a positive integer for password length.")
            else:
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters)
                                   for _ in range(length))
                self.password_display.delete(
                    1.0, END) 
                self.password_display.insert(END, password)
        except ValueError:
            messagebox.showerror(
                "Error", "Invalid input. Please enter a valid positive integer for password length.")

    def reset(self):
        
        self.username_entry.delete(0, END)
        self.password_length_entry.delete(0, END)
        self.password_display.delete(1.0, END)

    def start_animation(self):
        current_bg_color = self.top_label.cget("background")
        next_bg_color = "red" if current_bg_color == "white" else "white"
        self.top_label.config(background=next_bg_color)
        self.window.after(500, self.start_animation)


if __name__ == "__main__":
    window = Tk()
    window.configure(bg='wheat1')
    window.iconbitmap("icon.ico")
    password_generator = PasswordGenerator(window)
    f1 = Frame(window)
    f1.pack(fill=X, pady=5)
    copyright_label = Label(f1, text="© 2023 CodSoft. All rights reserved.",
                            font=("Arial", 10), fg="gray")
    copyright_label.pack(side=BOTTOM, pady=1, fill=X)

    window.mainloop()

import tkinter as tk
from tkinter import messagebox
def login():
    username = entry_username.get()
    messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
window = tk.Tk()
window.geometry("400x200")
window.title("Login Window")
label_username = tk.Label(window, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack(pady=5)
label_password = tk.Label(window, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)
button_login = tk.Button(window, text="Login", command=login)
button_login.pack(pady=10)
window.mainloop()

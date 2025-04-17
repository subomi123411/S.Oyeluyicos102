import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk

def WelcomeMessage(username):
    # Create a Tkinter window
    Window = tk.Toplevel(root)
    Window.title("Admin Box")
    Window.geometry("500x200")

    label_1 = tk.Label(Window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(Window, text="This is Python GUI with Tkinter")
    label_2.pack()

# Fix the submit function
def submit():
    username = username_entry.get()  # Use the entry widget to get the username
    password = password_entry.get()  # Use the entry widget to get the password
    if username == "Mary" and password == "cos102":
        WelcomeMessage(username)  # Pass the correct variable
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the main event loop
root.mainloop()
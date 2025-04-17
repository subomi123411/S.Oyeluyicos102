import pandas as pd
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Sample data
data = {
    "Name": ["Subomi Oyeluyi", "Ada Nwosu", "James Obi", "Zainab Musa", "Chidi Okeke"],
    "Department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"]
}

# Save the data to a CSV file
df = pd.DataFrame(data)
df.to_csv("GIG-logistics.csv", index=False)

# Load data from the CSV file
data = pd.read_csv("GIG-logistics.csv")

def WelcomeMessage(username, department):
    # Create a Tkinter window
    Window = tk.Toplevel(root)
    Window.title("Admin Box")
    Window.geometry("500x300")

    label_1 = tk.Label(Window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(Window, text="You have successfully logged in!")
    label_2.pack()
    
    # Get other employees in the same department
    other_employees = data[data['Department'].str.lower() == department]['Name'].str.title().tolist()
    if username.title() in other_employees:
        other_employees.remove(username.title())  # Remove the logged-in user from the list if present

    if other_employees:
        label_3 = tk.Label(Window, text="Other employees in your department:")
        label_3.pack()
        for emp in other_employees:
            emp_label = tk.Label(Window, text=emp)
            emp_label.pack()
    else:
        label_3 = tk.Label(Window, text="No other employees in your department.")
        label_3.pack()

def submit():
    username = username_entry.get().strip().lower()  # Get the username from the entry widget and convert to lowercase
    department = password_entry.get().strip().lower()  # Get the department from the entry widget and convert to lowercase

    # Convert the data in the DataFrame to lowercase for comparison
    data_lower = data.copy()
    data_lower['Name'] = data_lower['Name'].str.lower()
    data_lower['Department'] = data_lower['Department'].str.lower()

    # Check if the username and department match any record in the data
    if ((data_lower['Name'] == username) & (data_lower['Department'] == department)).any():
        WelcomeMessage(username, department)  # Show welcome message and other employees
    else:
        messagebox.showerror("Login Failed", "Invalid username or department")  # Show error if they don't match

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create department label and entry
password_label = tk.Label(root, text="Department:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the main event loop
root.mainloop()
import tkinter as tk
from tkinter import messagebox as msgbox

# handling the button click event
def on_button_click():
    #print("Button clicked!")
    
    # Show an information message box
    msgbox.showinfo("Information", "Welcome to COS 102 GUI App!\n")
    
    # Ask for user confirmation
    result = msgbox.askyesno("Confirmation", "Do you want to continue?")
    
# create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

# Add a label widget
label = tk.Label(root, text="Hello friend \n")
label.pack()

# Add a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Styling the button widget
button.config(fg="Red", bg="Yellow")

# Start the event loop
root.mainloop()
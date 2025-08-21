import random
import customtkinter as ctk

current_password = "" # Created outside of function to ensure other functions can access

def password_generator(length, type_):
    chars = ""
    if type_ == "standard":
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    elif type_ == "advanced":
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    elif type_ == "numeric":
        chars = "0123456789"
    else:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    return "".join(random.choice(chars) for _ in range(length)) # Builds a string by picking random characters

def generate_password():
    try:
        global current_password
        length = int(entry.get()) # Grab text from the Entry box and convert it to an integer
        type_ = optionmenu.get() # Grab selected value from dropdown
        password = password_generator(length, type_)
        current_password = password # Grabbing the full password to store for comparison to the one in the label for copying
        output_label.configure(text=f"Password: {password}") # Set label to the result
    except ValueError: # Makes sure you are giving it numbers
        output_label.configure(text="Please enter a valid number!")

def copy_password():
    # Grab the text from output label
    password = output_label.cget("text").replace("Password: ", "")
    if password == current_password: # Making sure you aren't copying when clicking copy more than once "Password copied:" or a "Please enter a valid number!"
        app.clipboard_clear()
        app.clipboard_append(password)
        app.update()
        output_label.configure(text=f"Password copied: {password}")

# CTk Setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("350x250")
app.resizable(False, False)
app.title("Password Generator")

# Entry
entry = ctk.CTkEntry(app, placeholder_text="Enter password length...", width=200, height=35, font=("Helvetica", 14)) # Entry box for you to type in
entry.pack(pady=10)

# Dropdown for type
optionmenu = ctk.CTkOptionMenu(app, values=["standard", "advanced", "numeric"], width=200, height=35, font=("Helvetica", 14)) # Giving three options in the dropdown
optionmenu.pack(pady=10)

# Button
button = ctk.CTkButton(app, text="Generate Password", command=generate_password, width=200, height=35, font=("Helvetica", 14)) # Creates on button that when clicked runs generate_password()
button.pack(pady=10)

# Output
output_label = ctk.CTkLabel(app, text="Your password will appear here.", width=300, height=20, font=("Helvetica", 14)) # Label for password to show up in
output_label.pack(pady=10)

# Copy Button
copy_button = ctk.CTkButton(app, text="Copy", command=copy_password, width=25, height=25, font=("Helvetica", 8)) # Button to copy password
copy_button.pack(pady=10)

app.mainloop()

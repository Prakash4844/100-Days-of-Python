from tkinter import *
import tkinter.messagebox as tkmessagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    """
    Generates a password
    :return: none
    """
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entry():
    """
    Saves the entry to a file
    :return: none
    """
    website = website_entry.get().title()
    email = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password_text
        }
    }

    if len(website) == 0 or len(password_text) == 0:
        tkmessagebox.showwarning(title="MyPass", message="Please don't leave any fields empty!")
        return

    confirm = tkmessagebox.askokcancel(title="MyPass Confirmation", message="These are the entered details\n"
                                                                            f"Email/Username: {email}\n"
                                                                            f"Password: {password_text}\n"
                                                                            f"Website: {website}\n"
                                                                            "Save Entry?")
    if not confirm:
        return

    try:
        with open("password.json", "r") as data:
            # Reading old data
            json_data = json.load(data)
    except FileNotFoundError:
        with open("password.json", "w") as data:
            json.dump(new_data, data, indent=4)
    else:
        # Updating old data with new data
        json_data.update(new_data)

        with open("password.json", "w") as data:
            # Saving updated data
            json.dump(json_data, data, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    """
    Searches for the password
    :return: none
    """
    website = website_entry.get().title()
    try:
        with open("password.json", "r") as data:
            # Reading old data
            json_data = json.load(data)
    except FileNotFoundError:
        tkmessagebox.showwarning(title="MyPass", message="No Data File Found!")
    else:
        if website in json_data:
            email = json_data[website]["email"]
            password = json_data[website]["password"]
            tkmessagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            tkmessagebox.showwarning(title="MyPass", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

app = Tk()
app.title("MyPass")
app.config(padx=50, pady=50)

# logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=28)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "Zaphkiel@Kurumi.com")
password_entry = Entry(width=28)
password_entry.grid(column=1, row=3)

# buttons
search_button = Button(text="Search", width=8, command=search_password)
search_button.grid(column=2, row=1)
generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=37, command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)

app.mainloop()

from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=28)
password_entry.grid(column=1, row=3)

# buttons
generate_password_button = Button(text="Generate")
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=37)
add_button.grid(column=1, row=4, columnspan=2)

app.mainloop()

import tkinter


app = tkinter.Tk()
app.title("DUCKER")
# app.minsize(width=240, height=250)
app.geometry("300x300")

# Label
new_label = tkinter.Label(text="I am Sexy", font=("Park Tech CG", 25))
new_label.pack()
new_label.config(text="Girls are by default Sexy.")
new_label["text"] = "I am a Sexy."

# Button


def button_pressed():
    new_label["text"] = f"I am {my_entry.get()}"


new_button = tkinter.Button(text="Click Me", command=button_pressed)
new_button.pack()


# Entry
my_entry = tkinter.Entry(width=20)
my_entry.pack()


app.mainloop()

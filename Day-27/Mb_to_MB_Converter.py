import tkinter

app = tkinter.Tk()
app.title("Megabytes to Megabits Converter")
app.minsize(width=300, height=100)
app.config(padx=20, pady=20)


def convert():
    mb = float(mb_input.get())
    mb /= 8
    output.config(text=f"{mb}")


# Label
label = tkinter.Label(text="Megabits to Megabytes Converter", font=("Arial", 12))
label.grid(column=0, row=0, columnspan=2)

# Entry
mb_input = tkinter.Entry(width=10)
mb_input.insert(0, string="0")
mb_input.grid(column=0, row=1)

# Button
button = tkinter.Button(text="Convert", command=convert)
button.grid(column=1, row=1)

# Label
label = tkinter.Label(text="Megabytes", font=("Arial", 12))
label.grid(column=2, row=1)

# Label
output = tkinter.Label(text="0", font=("Arial", 12))
output.grid(column=0, row=2, columnspan=2)

# Label
label = tkinter.Label(text="Megabits", font=("Arial", 12))
label.grid(column=2, row=2)

app.mainloop()

import tkinter


app = tkinter.Tk()
app.title("DUCKER")
# app.geometry("500x300")
app.minsize(width=500, height=300)
app.config(padx=20, pady=20)

#### pack

# # Label
# new_label = tkinter.Label(text="I am Sexy", font=("Park Tech CG", 12))
# new_label.pack(side="left")
#
# # Button
# new_button = tkinter.Button(text="Click Me")
# new_button.pack(side="right")
#
# # Entry
# my_entry = tkinter.Entry(width=20)
# my_entry.pack(side="bottom")


##### place

# # Label
# new_label = tkinter.Label(text="I am Sexy", font=("Park Tech CG", 12))
# new_label.place(x=0, y=0)
#
# # Button
# new_button = tkinter.Button(text="Click Me")
# new_button.place(x=100, y=100)
#
# # Entry
# my_entry = tkinter.Entry(width=20)
# my_entry.place(x=200, y=200)


##### grid

# Label
new_label = tkinter.Label(text="I am Sexy", font=("Park Tech CG", 12))
new_label.grid(column=0, row=0)
new_label.config(padx=50, pady=50)

# Button
new_button = tkinter.Button(text="Click Me")
new_button.grid(column=1, row=1)

newer_button = tkinter.Button(text="Click Me")
newer_button.grid(column=2, row=0)

# Entry
my_entry = tkinter.Entry(width=20)
my_entry.grid(column=3, row=2)

# NOTE : grid is generally the best layout manager
# NOTE2: grid is the only layout manager that can be used with all widgets
# NOTE3: grid is incompatible with pack and place
# NOTE4: grid is the most complex layout manager

# Grid Divides the window into rows and columns like this:
# 0,0 | 0,1 | 0,2
# 1,0 | 1,1 | 1,2
# 2,0 | 2,1 | 2,2

app.mainloop()

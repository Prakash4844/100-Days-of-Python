import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_button.config(state="normal")
    app.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    start_button.config(state="disabled")
    if math.floor(count % 60) < 10:
        count_sec = f"0{math.floor(count % 60)}"
    else:
        count_sec = (count % 60)

    canvas.itemconfig(timer_text, text=f"{math.floor(count / 60)}:{count_sec}")
    if count > 0:
        global timer
        timer = app.after(1000, count_down, count - 1)
    else:
        # start_button.config(state="normal")
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


app = Tk()
app.title("Pomodoro")
app.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

exit_button = Button(text="Exit", highlightthickness=0, command=app.quit)
exit_button.grid(column=1, row=4)

app.mainloop()

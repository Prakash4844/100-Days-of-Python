from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
JP_WORD = "Data/Eng-Jp.csv"
HI_WORD = "Data/Eng-Hi.csv"
not_known = {}

# ---------------------------- Read CSV data ------------------------------- #

try:
    data = pandas.read_csv("Data/word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(HI_WORD)

to_learn_dict = data.to_dict(orient="records")
random_word, random_hindi_word = '', ''


# ---------------------------- Flip card ------------------------------- #


def flip_card():
    """
    Flip the card to show the English word
    :return: English word
    """
    canvas.itemconfig(card_front, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{random_word['English']}", fill="white")


# ---------------------------- Known word ------------------------------- #

def is_known():
    """
    Remove the known word from the CSV file
    :return: None
    """
    to_learn_dict.remove(random_word)
    data1 = pandas.DataFrame(to_learn_dict)
    data1.to_csv("Data/word_to_learn.csv", index=False)
    next_card()


# ---------------------------- Next card ------------------------------- #


def next_card():
    """
    Get random Hindi word from the CSV file
    :return: Random Hindi word
    """
    global random_word, random_hindi_word, flip_timer
    app.after_cancel(flip_timer)
    random_word = random.choice(to_learn_dict)
    random_hindi_word = random_word["Hindi"]
    canvas.itemconfig(card_front, image=card_front_img)
    canvas.itemconfig(language_text, text="Hindi", fill="black")
    canvas.itemconfig(word_text, text=f"{random_hindi_word}", fill="black")
    flip_timer = app.after(5000, flip_card)


# ---------------------------- UI ------------------------------- #
app = Tk()
app.title("Flashy Flash")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_front = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, width=98, height=98, highlightthickness=0,
                      borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, width=98, height=99, highlightthickness=0,
                      borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)
flip_timer = app.after(5000, flip_card)

next_card()

app.mainloop()

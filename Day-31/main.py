from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
JP_WORD = "Eng-Jp.csv"
HI_WORD = "Eng-Hi.csv"

# ---------------------------- Read CSV data ------------------------------- #

data = pandas.read_csv(HI_WORD)
to_learn_dict = data.to_dict(orient="records")
random_word = random.choice(to_learn_dict)
random_hindi_word = random_word["Hindi"]

# ---------------------------- Random Hindi word ------------------------------- #


def next_card():
    """
    Get random Hindi word from the CSV file
    :return: Random Hindi word
    """
    global random_word, random_hindi_word
    random_word = random.choice(to_learn_dict)
    random_hindi_word = random_word["Hindi"]
    canvas.itemconfig(card_front, image=card_front_img)
    canvas.itemconfig(language_text, text="Hindi", fill="black")
    canvas.itemconfig(word_text, text=f"{random_hindi_word}", fill="black")


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
                      borderwidth=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

app.mainloop()

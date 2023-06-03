import turtle
import pandas
from tkinter import messagebox

screen = turtle.Screen()
screen.title("INDIA States Game")
screen.setup(width=800, height=957)
# noinspection PyProtectedMember
screen.cv._rootwindow.resizable(False, False)

image = "India.gif"

screen.addshape(image)
turtle.shape(image)
guessed_state = []


def exit_game():
    Remaining_State = {
        "States": []
    }
    for state in states:
        if state not in guessed_state:
            Remaining_State["States"].append(state)
    rdf = pandas.DataFrame(Remaining_State)
    rdf.to_csv("Remaining States.csv", index=False)
    exit()


while True:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/31 Guessed States",
                                    prompt=f"You have guessed {len(guessed_state)}/31, What's another "
                                           f"state's "
                                           "name?").title()
    answer_state.title()

    data = pandas.read_csv("states_data.csv")
    states = data.state.to_list()

    if answer_state in states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        states.remove(answer_state)
        if len(states) == 0:
            messagebox.showinfo("Congrats", "Congratulations, You have guessed all states")
            break
    elif answer_state == "Exit":
        exit_game()
    else:
        messagebox.showerror("Wrong", "You have guessed wrong")

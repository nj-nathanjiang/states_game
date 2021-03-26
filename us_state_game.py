import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("state_coordinates.csv")
list_of_states = data.state.to_list()

num_states_guessed = 0
game_still_on = True
while game_still_on:
    answer = screen.textinput(title=f"{num_states_guessed}/50 States Correct", prompt="What's another state name?").title()
    if answer == "Exit":
        break
    if answer in list_of_states:
        num_states_guessed += 1
        list_of_states.remove(answer)
        answer_row = data[data.state == answer]
        answer_x = int(answer_row.x)
        answer_y = int(answer_row.y)
        for i in answer_row.name:
            the_name = i

        the_turtle = turtle.Turtle()
        the_turtle.penup()
        the_turtle.hideturtle()
        the_turtle.goto(answer_x, answer_y)
        the_turtle.write(f"{the_name}", align="center", font=("Courier", 10, "normal"))

    if num_states_guessed == 50:
        game_still_on = False

new_data = pandas.DataFrame(list_of_states)
new_data.to_csv("states_to_learn.csv")

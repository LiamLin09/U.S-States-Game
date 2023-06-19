import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt="What's another state's name?").title()
    print(answer_state)
    # check if the guess is among the 50 states
        # if they got it right:
            # create a turtle to write the state name at x and y corrdate
    if answer_state == 'Exit':
        missing_state = []
        for state in all_state:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv('state_to_learn.csv')
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
# write correct guesses onto the map
# use a loop to allow the user to keep guessing
# record the correct guesses in a list
# keep track of the score


screen.exitonclick()

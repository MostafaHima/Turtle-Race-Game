from turtle import Turtle, Screen
import random

# Setup the screen
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

# Get the user's bet on the turtle color
user_bet = screen.textinput(title="Make Your Bet", prompt="Choose a color you think will win.")

# Define turtle colors and starting positions
colors = ["red", "orange", "purple", "brown", "yellow", "green"]
starting_positions = [-100, -70, -40, -10, 20, 50]

# Create the turtles and position them
all_turtles = []
for index in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(-240, starting_positions[index])
    all_turtles.append(turtle)

# Start the race if the user has placed a bet
race_on = False
if user_bet:
    race_on = True

# Race loop
while race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 220:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You guessed right! The winner is {winning_color}.")
            else:
                print(f"You lost. The winner is {winning_color}.")

        # Move the turtle forward by a random distance
        turtle.forward(random.randint(0, 10))

screen.mainloop()

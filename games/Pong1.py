"""
Mark Porraz, 11/20/2023, Pong.py
Simple Pong in/Python 3 for beginners
Part 1: getting started
"""

import turtle
# The turtle module lets you use and expand graphics
# probably through vector use
wn = turtle.Screen()  # you have to create a window, using the module you just referenced, turtle
wn.title("Pong by @GamesDean")
wn.bgcolor("black")  # color of screen is black
wn.setup(width=800, height=600)  # dimensions of the screen
wn.tracer(0)  # this stops the window from updating
# this speeds up the bit rate of the game

# Scoring function
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # lowercase is the module, uppercase is the class name
paddle_a.speed(0)  # sets the paddle to the maximum speed for animation
paddle_a.shape("square")  # gives the module a square shape
paddle_a.color("white")  # gives the shape white color.
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # added to modify shape size. W/O would be square
# we then stretch the width of the object by 5 , and stretch the length by 1, which is default
paddle_a.penup()  # turtle draws a line while the object is moving, so we don't have to
paddle_a.goto(-350, 0)  # paddle A starts at -350 (x coordinate) and ends at 0 (y coordinate)
# minus 350 for the left hand side

# Paddle B
paddle_b = turtle.Turtle()  # lowercase is the module, uppercase is the class name
paddle_b.speed(0)  # sets the paddle to the maximum speed for animation
paddle_b.shape("square")  # gives the module a square shape
paddle_b.color("white")  # gives the shape white color.
paddle_b.shapesize(stretch_wid=5,stretch_len=1)  # added to modify shape size. W/O would be square
# we then stretch the width of the object by 5 , and stretch the length by 1, which is default
paddle_b.penup()  # turtle draws a line while the object is moving, so we don't have to
paddle_b.goto(350,0)  # paddle A starts at 350 (x coordinate) and ends at 0 (y coordinate)
# plus 350 for the right hand side


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

# Ball Movement
ball.dx = -0.1
ball.dy = -0.1

# Pen is used for the score board
pen = turtle.Turtle()
pen.speed(0)  # animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 PlayerB: 0", align="center", font=("Gothic", 24, "normal"))


# Function
# paddle A functions for up and down
def paddle_a_up():
     y = paddle_a.ycor()  # paddle, the object uses the .ycor (turtle) module which returns the Y coordinate
     y += 20  # add 20 pixels to the Y coordinate
     paddle_a.sety(y)  # set the coordinate for paddle A, set Y to the new Y


def paddle_a_down():
     y = paddle_a.ycor()  # paddle, the object uses the .ycor (turtle) module which returns the Y coordinate
     y -= 20  # subtracts 20 pixels to the Y coordinate
     paddle_a.sety(y)  # set the coordinate for paddle A, set Y to the new Y


# paddle B functions for up and down
def paddle_b_up():
     y = paddle_b.ycor()  # paddle, the object uses the .ycor (turtle) module which returns the Y coordinate
     y += 20  # add 20 pixels to the Y coordinate
     paddle_b.sety(y)  # set the coordinate for paddle B, set Y to the new Y


def paddle_b_down():
     y = paddle_b.ycor()  # paddle, the object uses the .ycor (turtle) module which returns the Y coordinate
     y -= 20  # subtracts 20 pixels to the Y coordinate
     paddle_b.sety(y)  # set the coordinate for paddle B, set Y to the new Y


# keyboard binding
# this section is for using the function that we just called
# For paddle A
wn.listen()  # tells it to listen for keyboard input
wn.onkeypress(paddle_a_up, "w")  # when the user presses 'w', call the function, paddle_a_up
wn.onkeypress(paddle_a_down, "s")  # when the user presses 'w', call the function, paddle_a_up

# For paddle B
wn.listen()  # tells it to listen for keyboard input
wn.onkeypress(paddle_b_up, "Up")  # when the user presses 'w', call the function, paddle_a_up
wn.onkeypress(paddle_b_down, "Down")  # when the user presses 'w', call the function, paddle_a_up


# Main game loop
while True:
     wn.update()  # everytime the code runs, the window updates

# move the ball
     ball.setx(ball.xcor() + ball.dx)  # the current x coordinate + ball.dx. meaning the first time you run loop it will
# move to the right two. Will continue two
     ball.sety(ball.ycor() + ball.dy)
# border checking - once we set the ball to a certain point, it should bounce
     if ball.ycor() > 290:
          ball.sety(290)
          ball.dy *= -1

     if ball.ycor() < -290:
          ball.sety(-290)
          ball.dy *= -1

     if ball.xcor() > 390:  # if the ball goes higher than 290, it is off-screen
          ball.goto(0,0) # if ball is off-screen, place it in the middle of screen
          ball.dx *= -1
          score_a += 1
          pen.clear()
          pen.write("Player A: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Gothic", 24, "normal"))


     if ball.xcor() < -390:
          ball.goto(0,0)
          ball.dx *= -1
          score_b += 1
          pen.clear()
          pen.write("Player A: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Gothic", 24, "normal"))

# Paddle and ball collisions
# Paddle B

     if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
          ball.setx(340)
          ball.dx *= -1


# Paddle and ball collisions
# Paddle A

     if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
          ball.setx(-340)
          ball.dx *= -1


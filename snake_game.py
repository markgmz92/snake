import turtle
import time

delay = 0.1

# Set up the screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "up"

# Functions


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)


# Main game loop
while True:
    wn.update()

    move()
    time.sleep(delay)

wn.mainloop()

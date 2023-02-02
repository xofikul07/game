import turtle
import random

wn = turtle.Screen()
wn.title("Bubble Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Create the bubbles
bubbles = []
for _ in range(5):
    bubble = turtle.Turtle()
    bubble.shape("circle")
    bubble.color("blue")
    bubble.speed(0)
    bubble.penup()
    bubble.goto(random.randint(-290, 290), random.randint(-290, 290))
    bubbles.append(bubble)

# Move the bubbles
while True:
    for bubble in bubbles:
        bubble.dx = random.uniform(-2, 2)
        bubble.dy = random.uniform(-2, 2)
        bubble.setx(bubble.xcor() + bubble.dx)
        bubble.sety(bubble.ycor() + bubble.dy)

wn.mainloop()

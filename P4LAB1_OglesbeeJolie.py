import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn right by 90 degrees

# Move to a new position for the triangle
t.penup()
t.goto(150, 0)
t.pendown()

# Draw an equilateral triangle
for _ in range(3):
    t.forward(100)  # Move forward by 100 units
    t.left(120)     # Turn left by 120 degrees

# Hide the turtle cursor
t.hideturtle()

# Keep the window open until manually closed
turtle.done()

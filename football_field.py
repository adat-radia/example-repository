
import turtle

#  the setup the screen , color, and pen size
turtle.setup(1224, 700)
turtle.bgcolor('green')
turtle.color('white')
turtle.pensize(4)
#  draw the outer square
turtle.penup()
turtle.goto(450, -250)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)
turtle.setheading(180)
turtle.forward(900)
turtle.setheading(270)
turtle.forward(500)
turtle.setheading(0)
turtle.forward(900)

#  draw the right side goal area
turtle.goto(450, -100)
turtle.setheading(180)
turtle.forward(100)
turtle.setheading(90)
turtle.forward(200)
turtle.setheading(0)
turtle.forward(100)

#  draw the left side goal area
turtle.penup()
turtle.goto(-450, -100)
turtle.pendown()
turtle.setheading(0)
turtle.forward(100)
turtle.setheading(90)
turtle.forward(200)
turtle.setheading(180)
turtle.forward(100)

#  draw the middle line
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)

#  draw the circle in the middle
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.circle(100)

turtle.hideturtle()
turtle.done()

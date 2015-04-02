import turtle
wn = turtle.Screen()
wn.bgcolor('white')

# turtle.speed(0)
# turtle.fillcolor("white")
# turtle.begin_fill()
# turtle.hideturtle()

for i in range(360):
	turtle.forward(1)
	turtle.left(1)
# turtle.end_fill()

#Shift right
turtle.penup()
turtle.forward(100)

#Square
turtle.pendown()
for i in range(4):
	turtle.forward(120)
	turtle.left(90)

#Shift right
turtle.penup()
turtle.forward(150)

#Triangle
turtle.pendown()
for i in range(3):
	turtle.forward(135)
	turtle.left(120)

#Shift next row
turtle.penup()
turtle.home()
turtle.right(90)
turtle.forward(100)

#Star
turtle.pendown()
turtle.left(90)
for i in range(5):
	turtle.forward(100)
	turtle.right(144)

wn.exitonclick()
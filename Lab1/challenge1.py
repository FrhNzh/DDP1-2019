import turtle

turtle.speed(20)

#drawing a circle
turtle.color('yellow')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()

turtle.forward(40)
turtle.left(90)
turtle.forward(120)
turtle.right(90)

#drawing two eyes
turtle.color('black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.left(180)
turtle.forward(80)
turtle.left(180)

turtle.color('black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()


#moving the pen
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(18)
turtle.right(90)

#drawing a smile
#source: 'How to Draw a Semicircle', stackoverflow.com
turtle.pensize(2)
turtle.pencolor('black')
turtle.pendown()
for x in range(90):
    turtle.forward(0.8)
    turtle.left(2)


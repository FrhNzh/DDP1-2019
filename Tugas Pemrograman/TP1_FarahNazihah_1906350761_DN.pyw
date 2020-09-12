# import modules
from turtle import *
import random

title('Rotating Colorful Square and Disks')
colormode(255)


# creating an input box
length = numinput('Rotataing Colorful Square and Disks',\
                    'Please enter the side length of the first square [20-60]',\
                    minval=(20), maxval=(60), default=(40))

pencolor('white')
speed(0)
shape('turtle')


# moving turtle to the left
penup()
left(180)
forward(110)
pendown()


# drawing rotating colorful square
for i in range(72):
    r = random.randint(150,255)
    g = random.randint(150,255)
    b = random.randint(150,250)

    fillcolor(r, g, b)
    begin_fill()
    for square in range(4):
        forward(length)
        right(90)
    end_fill()
    right(5)

    length += 2
    


#moving turtle to the right
penup()
setheading(0)
forward(300)
pendown()

 
# drawing rotating colorful disks
radius = 0.5*length

for i in range(36):
    r = random.randint(150,255)
    g = random.randint(150,255)
    b = random.randint(150,255)

    fillcolor(r, g, b)
    begin_fill()
    circle(radius)
    end_fill()
    left(10)

    radius -= 2

# writing the sentence
penup()
goto(0,-250)
color("black")
write('There are 72 Squares and 36 Disks', align='center',\
            font=("Arial",20, 'normal'))
hideturtle()

exitonclick()
mainloop()

from turtle import *


n = int(input('Masukan ketebalan labirin: '))
x = int(100/n)

# moving turtle to the left
penup()
goto(-100, -100)
pendown()

# drawing the maze
panjang = 200
forward(panjang)
left(90)
for i in range(n*2):
	forward(panjang)
	left(90)
	forward(panjang)
	panjang -= x
	left(90)


exitonclick()
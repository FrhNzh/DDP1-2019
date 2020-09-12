import turtle
import math

user = input('masukan nama pengguna: ').lower()

if user == 'pak chanek':
    turtle.circle(100)
else:
    #drawing an triangle
    turtle.forward(100)

    turtle.left(90)
    turtle.forward(100)

    turtle.left(180 - 45)
    turtle.forward(100 * math.sqrt(2))

turtle.exitonclick()
turtle.mainloop()

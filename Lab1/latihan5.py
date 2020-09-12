import turtle

print('Ada dua rasa donat, rasa Coklat dan rasa Stoberi.')
print('ketik \'stroberi\' jika ingin donat stroberi, \n dan ketik \'Cokelat\' jika ingin donat cokelat.')


rasa = input('masukan rasa donat: ').lower()

if rasa == 'cokelat':
    turtle.color('brown')
    turtle.begin_fill()
elif rasa == 'stroberi':
    turtle.color('red')
    turtle.begin_fill()
else:
    print('Maaf, kami hanya memiliki donat rasa Cokelat dan Stroberi.')
    turtle.pencolor('black')

turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.left(90)

#lingkaran besar
turtle.pendown()
turtle.circle(100)
turtle.end_fill()

#memindahkan pen
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.pendown()

if rasa == 'cokelat' or rasa == 'stroberi':
    turtle.color('white')
    turtle.color('white')
    turtle.begin_fill()
else:
    turtle.color('black')


#menggambar lingkaran kecil
turtle.circle(50)
turtle.end_fill()


turtle.exitonclick()
turtle.mainloop()

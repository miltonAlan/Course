import turtle
from random import randint

alto = 650
ancho = 1000
velocidad = 30
velocidad_y = 0.1
velocidad_x = 0.1
largo_paleta = 8
factor_aumento = 1.5


def posicion_inicial():
    return randint(alto, ancho)


wn = turtle.Screen()
wn.title('Pong by Milton')
wn.bgcolor('pink')
wn.setup(width=ancho, height=alto)
wn.tracer(0)


def supplies(speed, shape, color, x, y):
    paddle = turtle.Turtle()
    paddle.speed(speed)
    paddle.shape(shape)
    paddle.color(color)

    if shape != 'circle':
        paddle.shapesize(stretch_wid=largo_paleta, stretch_len=1)

    paddle.penup()
    paddle.goto(x, y)
    return paddle


def up_down(direction, paddle_x, speed):
    y = paddle_x.ycor()

    if direction == 'up' and (y + speed) < alto/2.5:
        paddle_x.sety(y + speed)

    if direction == 'down' and (y - speed) > (alto/2.5) * -1:
        paddle_x.sety(y - speed)


paddle_a = supplies(0, 'square', 'red', (ancho/2.2)*-1, 0)
paddle_b = supplies(0, 'square', 'blue', ancho/2.2, 0)
ball = supplies(0, 'circle', 'yellow', 0, 0)


wn.listen()
# paleta a
wn.onkeypress(lambda n=99999: up_down('up', paddle_a, velocidad), 'w')
wn.onkeypress(lambda n=99999: up_down('down', paddle_a, velocidad), 's')

# paleta b
wn.onkeypress(lambda n=99999: up_down('up', paddle_b, velocidad), 'Up')
wn.onkeypress(lambda n=99999: up_down('down', paddle_b, velocidad), 'Down')

temp = 100
# lazo
while True:
    wn.update()

    # choque contra las paletas
    # a
    if ball.xcor() < -ancho/2.2 and ball.ycor() < (paddle_a.ycor() + temp) and ball.ycor() > (paddle_a.ycor() - temp):
        ball.color(paddle_a.color()[0])
        velocidad_y *= factor_aumento
        velocidad_x *= factor_aumento
        ball.setx(ball.xcor() + velocidad_x + temp)

    # b
    if ball.xcor() > ancho/2.2 and ball.ycor() < (paddle_b.ycor() + temp) and ball.ycor() > (paddle_b.ycor() - temp):
        ball.color(paddle_b.color()[0])
        velocidad_y *= factor_aumento
        velocidad_x *= factor_aumento
        ball.setx(ball.xcor() + velocidad_x - temp)

    # movimiento de la bola
    ball.sety(ball.ycor() + velocidad_y)
    ball.setx(ball.xcor() + velocidad_x)

    if ball.ycor() > alto/2.2:
        velocidad_y *= -1
        ball.color('yellow')

    if ball.ycor() < -alto/2.2:
        velocidad_y *= -1
        ball.color('yellow')

    if ball.xcor() > ancho/2.2:
        velocidad_x *= -1
        ball.color('yellow')

    if ball.xcor() < -ancho/2.2:
        velocidad_x *= -1
        ball.color('yellow')

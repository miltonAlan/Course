import turtle
from random import randint

alto = 650
ancho = 1000
velocidad = 30
velocidad_y = 0.3
velocidad_x = 0.3
largo_paleta = 8
factor_aumento = 1.5

wn = turtle.Screen()
wn.title('Pong by Milton')
wn.bgcolor('black')
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
paddle_a.points = 0

paddle_b = supplies(0, 'square', 'blue', ancho/2.2, 0)
paddle_b.points = 0

ball = supplies(0, 'circle', 'yellow', 0, 0)


wn.listen()

# paleta a
wn.onkeypress(lambda n=99999: up_down('up', paddle_a, velocidad), 'w')
wn.onkeypress(lambda n=99999: up_down('down', paddle_a, velocidad), 's')

# paleta b
wn.onkeypress(lambda n=99999: up_down('up', paddle_b, velocidad), 'Up')
wn.onkeypress(lambda n=99999: up_down('down', paddle_b, velocidad), 'Down')

# puntuacion
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, round(alto/2.5))
pen.write('Jugador Izquierda: 0   Jugador Derecha: 0',
          align='center', font=('Courier', 24, 'normal'))


temp = 100
bandera_toca_si_no = False
# lazo
while True:
    wn.update()

    # choque contra las paletas
    # izquierda
    if ball.xcor() < -ancho/2.5 and ball.ycor() < (paddle_a.ycor() + temp) and ball.ycor() > (paddle_a.ycor() - temp):
        ball.color(paddle_a.color()[0])
        velocidad_y *= factor_aumento
        velocidad_x *= factor_aumento
        ball.setx(ball.xcor() + velocidad_x + temp)
        velocidad_x *= -1
        bandera_toca_si_no = True

    # derecha
    if ball.xcor() > ancho/2.5 and ball.ycor() < (paddle_b.ycor() + temp) and ball.ycor() > (paddle_b.ycor() - temp):
        ball.color(paddle_b.color()[0])
        velocidad_y *= factor_aumento
        velocidad_x *= factor_aumento
        ball.setx(ball.xcor() + velocidad_x - temp)
        velocidad_x *= -1
        bandera_toca_si_no = True

    # movimiento de la bola
    ball.sety(ball.ycor() + velocidad_y)
    ball.setx(ball.xcor() + velocidad_x)

    # choque contra los bordes
    if ball.ycor() > alto/2.2:
        velocidad_y *= -1
        ball.color('yellow')


    if ball.ycor() < -alto/2.2:
        velocidad_y *= -1
        ball.color('yellow')

    if ball.xcor() > ancho/2.2:
        velocidad_x *= -1
        ball.color('yellow')

        if bandera_toca_si_no == True:
            paddle_a.points += 1    

        pen.clear()
        pen.write('Jugador Izquierda: {}   Jugador Derecha: {}'.format(paddle_a.points, paddle_b.points), align='center', font=('Courier', 24, 'normal'))
        bandera_toca_si_no = False

        
    if ball.xcor() < -ancho/2.2:
        velocidad_x *= -1
        ball.color('yellow')

        if bandera_toca_si_no == True:
            paddle_b.points += 1    
            
        pen.clear()
        pen.write('Jugador Izquierda: {}   Jugador Derecha: {}'.format(paddle_a.points, paddle_b.points), align='center', font=('Courier', 24, 'normal'))
        bandera_toca_si_no = False

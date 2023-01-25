from turtle import Screen, Turtle
from paddle import Paddle
from bola import Ball
from pontuacao import Placar
import time

tela = Screen()
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.title("Pong")
tela.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
bolinha = Ball()
placar_ponto = Placar()

tela.listen()
tela.onkey(r_paddle.go_up, "Up")
tela.onkey(r_paddle.go_down, "Down")
tela.onkey(l_paddle.go_up, "w")
tela.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    tela.update()
    bolinha.move()

    #Detecta a colisão com a parede
    if bolinha.ycor() > 280 or bolinha.ycor() < -280:
        bolinha.bounce_y()

    #Detecta a colisão com o paddle
    if bolinha.distance(r_paddle) < 50 and bolinha.xcor() > 320 or bolinha.distance(l_paddle) < 50 and bolinha.xcor() < -320:
        bolinha.bounce_x()

    #Detecta a perca do lado direito
    if bolinha.xcor() > 380:
        bolinha.reset_position()
        placar_ponto.l_point()

    #Detecta a perca do lado esquerdo
    if bolinha.xcor() < -380:
        bolinha.reset_position()
        placar_ponto.r_point()

tela.exitonclick()
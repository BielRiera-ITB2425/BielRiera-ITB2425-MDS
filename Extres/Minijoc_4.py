import turtle
import time
import random

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Juego de la Serpiente")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Desactiva la actualización automática de la pantalla

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Funciones para mover la serpiente
def mover_arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def mover_abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def mover_izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def mover_derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def mover():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
wn.listen()
wn.onkey(mover_arriba, "w")
wn.onkey(mover_abajo, "s")
wn.onkey(mover_izquierda, "a")
wn.onkey(mover_derecha, "d")

# Bucle principal del juego
while True:
    wn.update()
    mover()
    time.sleep(0.1)

import turtle as t

# Variables globales de puntuación y movimiento de la pelota
player_a_score = 0
player_b_score = 0
ball_dx = 1.5
ball_dy = 1.5

# Funciones de movimiento de las paletas
def move_paddle_left_up(paddle_left):
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def move_paddle_left_down(paddle_left):
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def move_paddle_right_up(paddle_right):
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def move_paddle_right_down(paddle_right):
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

# Funciones de actualización de la puntuación
def update_score_display(pen):
    pen.clear()
    pen.write(f"Player A: {player_a_score}    Player B: {player_b_score}", align="center", font=('Monaco', 24, 'normal'))

# Función de inicialización del juego
def initialize_game():
    win = t.Screen()
    win.title("Ping-Pong Game")
    win.bgcolor('black')
    win.setup(width=800, height=600)
    win.tracer(0)

    paddle_left = t.Turtle()
    paddle_left.speed(0)
    paddle_left.shape('square')
    paddle_left.color('red')
    paddle_left.shapesize(stretch_wid=5, stretch_len=1)
    paddle_left.penup()
    paddle_left.goto(-350, 0)

    paddle_right = t.Turtle()
    paddle_right.speed(0)
    paddle_right.shape('square')
    paddle_right.shapesize(stretch_wid=5, stretch_len=1)
    paddle_right.color('red')
    paddle_right.penup()
    paddle_right.goto(350, 0)

    ball = t.Turtle()
    ball.speed(0)
    ball.shape('circle')
    ball.color('yellow')
    ball.penup()
    ball.goto(0, 0)

    pen = t.Turtle()
    pen.speed(0)
    pen.color('skyblue')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    update_score_display(pen)

    return win, paddle_left, paddle_right, ball, pen

# Función principal del bucle de juego
def game_loop(win, paddle_left, paddle_right, ball, pen):
    global ball_dx, ball_dy  # Declarar ball_dx y ball_dy como globales

    while True:
        win.update()

        # Mover la pelota
        ball.setx(ball.xcor() + ball_dx)
        ball.sety(ball.ycor() + ball_dy)

        # Rebotar la pelota en las paredes superior e inferior
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball_dy *= -1

        # Rebotar la pelota en las paletas izquierda y derecha
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 50 and ball.ycor() > paddle_right.ycor() - 50):
            ball.setx(340)
            ball_dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50):
            ball.setx(-340)
            ball_dx *= -1

        # Manejar las colisiones con los bordes laterales
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball_dx *= -1
            global player_a_score
            player_a_score += 1
            update_score_display(pen)

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball_dx *= -1
            global player_b_score
            player_b_score += 1
            update_score_display(pen)

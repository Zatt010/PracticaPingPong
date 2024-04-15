import unittest
from Game import paddle_left_up, paddle_left_down, paddle_right_up, paddle_right_down, paddle_left, paddle_right,ball, player_a_score, pen

class TestGame(unittest.TestCase):
    def setUp(self):
        ball.goto(0, 0)


    def test_paddle_left_up(self):
        initial_y = paddle_left.ycor()
        paddle_left_up()
        self.assertEqual(paddle_left.ycor(), initial_y + 15)

    def test_paddle_left_down(self):
        initial_y = paddle_left.ycor()
        paddle_left_down()
        self.assertEqual(paddle_left.ycor(), initial_y - 15)

    def test_paddle_right_up(self):
        initial_y = paddle_right.ycor()
        paddle_right_up()
        self.assertEqual(paddle_right.ycor(), initial_y + 15)

    def test_paddle_right_down(self):
        initial_y = paddle_right.ycor()
        paddle_right_down()
        self.assertEqual(paddle_right.ycor(), initial_y - 15)

    def test_ball_hits_left_border(self):
        ball.goto(-400, 0)
        initial_score = player_a_score
        self.assertEqual(player_a_score, initial_score + 1)

    def test_ball_hits_left_border_player_b_score(self):
        ball.goto(-400, 0)
        initial_player_b_score = player_b_score
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball_dx = -1.5
            player_b_score += 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                        align="center", font=('Monaco', 24, "normal"))
        self.assertEqual(player_b_score, initial_player_b_score + 1)

    def test_ball_hits_paddle_left(self):
        # Simular que la bola golpea la paleta izquierda
        ball.goto(-345, paddle_left.ycor())
        initial_ball_x = ball.xcor()
        initial_ball_dx = ball_dx

        if (-350 < ball.xcor() < -340) and (-40 < ball.ycor() - paddle_left.ycor() < 40):
            ball.setx(-340)
            ball_dx *= -1

        self.assertEqual(ball.xcor(), -340)
        self.assertEqual(ball_dx, -initial_ball_dx)

    def test_ball_hits_right_top_border(self):
        ball.goto(0, 300)
        initial_ball_y = ball.ycor()
        initial_ball_dy = ball_dy
        if ball.ycor() > 290:
            ball.sety(290)
            ball_dy *= -1

        self.assertEqual(ball.ycor(), 290)
        self.assertEqual(ball_dy, -initial_ball_dy)

    def test_ball_hits_right_width_border(self):
        ball.goto(400, 0)  # Posición de la bola sobre el borde derecho
        initial_ball_x = ball.xcor()
        initial_ball_dx = ball_dx
        initial_score_a = player_a_score

        # Simular el rebote en el borde derecho
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball_dx *= -1
            player_a_score += 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                        align="center", font=('Monaco', 24, "normal"))

        self.assertEqual(ball.xcor(), 0)
        self.assertEqual(ball_dx, -initial_ball_dx)
        self.assertEqual(player_a_score, initial_score_a + 1)

    def test_ball_hits_paddle_right(self):
        ball.goto(345, paddle_right.ycor())
        initial_ball_x = ball.xcor()
        initial_ball_dx = ball_dx
        if (340 < ball.xcor() < 350) and (paddle_right.ycor() - 40 < ball.ycor() < paddle_right.ycor() + 40):
            ball.setx(340)
            ball_dx *= -1

        self.assertEqual(ball.xcor(), 340)
        self.assertEqual(ball_dx, -initial_ball_dx)

if __name__ == '__main__':
    unittest.main()
import unittest
from Game import paddle_left_up, paddle_left_down, paddle_right_up, paddle_right_down, paddle_left, paddle_right

class TestGame(unittest.TestCase):
    def test_paddle_left_up(self):
        # Simular el movimiento hacia arriba de la paleta izquierda
        initial_y = paddle_left.ycor()
        paddle_left_up()
        self.assertEqual(paddle_left.ycor(), initial_y + 15)

    def test_paddle_left_down(self):
        # Simular el movimiento hacia abajo de la paleta izquierda
        initial_y = paddle_left.ycor()
        paddle_left_down()
        self.assertEqual(paddle_left.ycor(), initial_y - 15)

    def test_paddle_right_up(self):
        # Simular el movimiento hacia arriba de la paleta derecha
        initial_y = paddle_right.ycor()
        paddle_right_up()
        self.assertEqual(paddle_right.ycor(), initial_y + 15)

    def test_paddle_right_down(self):
        # Simular el movimiento hacia abajo de la paleta derecha
        initial_y = paddle_right.ycor()
        paddle_right_down()
        self.assertEqual(paddle_right.ycor(), initial_y - 15)

if __name__ == '__main__':
    unittest.main()

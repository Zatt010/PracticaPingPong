import unittest
from unittest.mock import MagicMock
import game_logic

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        # Configurar el entorno de prueba inicial
        self.win, self.paddle_left, self.paddle_right, self.ball, self.pen = game_logic.initialize_game()

    def test_move_paddle_right_up(self):
        # Simular movimiento hacia arriba de la paleta derecha
        initial_y = self.paddle_right.ycor()
        game_logic.move_paddle_right_up(self.paddle_right)
        self.assertEqual(self.paddle_right.ycor(), initial_y + 20)
    
    def test_move_paddle_left_up(self):
        # Simular movimiento hacia arriba de la paleta izquierda
        initial_y = self.paddle_left.ycor()
        game_logic.move_paddle_left_up(self.paddle_left)
        self.assertEqual(self.paddle_left.ycor(), initial_y + 20)

    def test_move_paddle_right_down(self):
        # Simular movimiento hacia abajo de la paleta derecha
        initial_y = self.paddle_right.ycor()
        game_logic.move_paddle_right_down(self.paddle_right)
        self.assertEqual(self.paddle_right.ycor(), initial_y - 20)

    def test_move_paddle_left_down(self):
        # Simular movimiento hacia abajo de la paleta izquierda
        initial_y = self.paddle_left.ycor()
        game_logic.move_paddle_left_down(self.paddle_left)
        self.assertEqual(self.paddle_left.ycor(), initial_y - 20)

    def test_ball_movement(self):
        # Simular movimiento de la pelota y verificar las nuevas coordenadas
        initial_x, initial_y = self.ball.xcor(), self.ball.ycor()
        game_logic.game_loop(self.win, self.paddle_left, self.paddle_right, self.ball, self.pen)
        self.assertNotEqual(self.ball.xcor(), initial_x)
        self.assertNotEqual(self.ball.ycor(), initial_y)

    def test_score_update(self):
        # Simular incremento de puntuación y verificar la actualización del marcador
        game_logic.player_a_score = 0
        game_logic.player_b_score = 0
        game_logic.game_loop(self.win, self.paddle_left, self.paddle_right, self.ball, self.pen)
        self.assertEqual(game_logic.player_a_score, 1)
        self.assertEqual(game_logic.player_b_score, 1)

    def tearDown(self):
        # Limpiar después de las pruebas
        self.win.bye()  # Cerrar la ventana de Turtle al finalizar las pruebas

if __name__ == '__main__':
    unittest.main()

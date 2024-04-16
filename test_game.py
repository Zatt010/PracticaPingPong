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

    def test_move_paddle_right_down(self):
        # Simular movimiento hacia abajo de la paleta derecha
        initial_y = self.paddle_right.ycor()
        game_logic.move_paddle_right_down(self.paddle_right)
        self.assertEqual(self.paddle_right.ycor(), initial_y - 20)

    def tearDown(self):
        # Limpiar después de las pruebas
        self.win.bye()  # Cerrar la ventana de Turtle al finalizar las pruebas

if __name__ == '__main__':
    unittest.main()

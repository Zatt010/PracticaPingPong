
import turtle as t
import game_logic  # Importar la lógica del juego

def main():
    win, paddle_left, paddle_right, ball, pen = game_logic.initialize_game()

    t.listen()
    t.onkeypress(lambda: game_logic.move_paddle_left_up(paddle_left), 'u')
    t.onkeypress(lambda: game_logic.move_paddle_left_down(paddle_left), 'e')
    t.onkeypress(lambda: game_logic.move_paddle_right_up(paddle_right), 'Up')
    t.onkeypress(lambda: game_logic.move_paddle_right_down(paddle_right), 'Down')

    game_logic.game_loop(win, paddle_left, paddle_right, ball, pen)

    t.mainloop()  # Ejecutar el bucle principal de Turtle

if __name__ == '__main__':
    main()
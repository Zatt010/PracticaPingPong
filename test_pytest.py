import pytest
from unittest.mock import MagicMock
import game_logic

@pytest.fixture
def game_setup():
    win, paddle_left, paddle_right, ball, pen = game_logic.initialize_game()
    return win, paddle_left, paddle_right, ball, pen

def test_move_paddle_left_up(game_setup):
    win, paddle_left, paddle_right, ball, pen = game_setup
    initial_y = paddle_left.ycor()
    game_logic.move_paddle_left_up(paddle_left)
    assert paddle_left.ycor() == initial_y + 20

def test_move_paddle_right_up(game_setup):
    win, paddle_left, paddle_right, ball, pen = game_setup
    initial_y = paddle_right.ycor()
    game_logic.move_paddle_right_up(paddle_right)
    assert paddle_right.ycor() == initial_y + 20

def test_move_paddle_right_down(game_setup):
    win, paddle_left, paddle_right, ball, pen = game_setup
    initial_y = paddle_right.ycor()
    game_logic.move_paddle_right_down(paddle_right)
    assert paddle_right.ycor() == initial_y - 20

def test_score_update(game_setup):
    win, paddle_left, paddle_right, ball, pen = game_setup
    game_logic.player_a_score = 0
    game_logic.player_b_score = 0
    game_logic.game_loop(win, paddle_left, paddle_right, ball, pen)
    assert game_logic.player_a_score == 1
    assert game_logic.player_b_score == 1


from BoardReader import BoardReader
from PIL import Image
import os
import numpy as np
import ImageInput

path_to_pic1 = os.path.join(os.getcwd(), "tests/pic_to_test1.png")
picture1 = ImageInput.convert_to_black_and_white(Image.open(path_to_pic1))
boardreader1 = BoardReader(picture1)
path_to_pic2 = os.path.join(os.getcwd(), "tests/pic_to_test2.png")
picture2 = ImageInput.convert_to_black_and_white(Image.open(path_to_pic2))
boardreader2 = BoardReader(picture2)


def test_board_size_getter():
    height, width = boardreader1.get_board_size()
    assert width == 5
    assert height == 5


def test_board_2_size_getter():
    height, width = boardreader2.get_board_size()
    assert width == 6
    assert height == 3


def test_board_creator():
    array = np.array([
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
    ])
    for x in range(5):
        for y in range(5):
            assert array[y, x] == boardreader1.get_pos_value(x, y)


def test_value_on_position_setter():
    boardreader1.set_value_on_pos(0, 0, 0)
    assert boardreader1.board[0, 0] == 0
    boardreader1.set_value_on_pos(0, 0, 0)
    assert boardreader1.board[0, 0] != 1
    boardreader1.set_value_on_pos(0, 0, 3)
    assert boardreader1.board[0, 0] == 0
    boardreader1.set_value_on_pos(0, 0, 1)
    assert boardreader1.board[0, 0] == 1


def test_position_value_getter():
    assert boardreader1.get_pos_value(0, 0) == 1
    assert boardreader1.get_pos_value(3, 3) == 0


def test_other_option():
    path_to_pic2 = os.path.join(os.getcwd(), "tests/pic_to_test2.png")
    picture2 = ImageInput.convert_to_black_and_white(Image.open(path_to_pic2))
    boardreader2 = BoardReader(picture2)
    array = np.array([
        [1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1],
    ])
    for x in range(6):
        for y in range(3):
            assert array[y, x] == boardreader2.get_pos_value(x, y)

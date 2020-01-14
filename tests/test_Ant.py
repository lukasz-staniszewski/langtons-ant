from Ant import Ant
from PIL import Image
from BoardReader import BoardReader
import os


def test_position_getter():
    ant = Ant((30, 20), "N")
    assert ant.position_x == 30
    assert ant.position_y == 20
    assert ant.position_x != "N"


def test_position_setter():
    ant = Ant((30, 20), "N")
    ant.set_position(5, 6)
    assert ant.position_x == 5
    assert ant.position_y == 6
    assert ant.position_x != 30
    assert ant.position_y != 20


def test_direction_getter():
    ant = Ant((30, 20), "N")
    assert ant.direction == "N"
    assert ant.direction != "South"


def test_direction_setter():
    ant = Ant((30, 20), "N")
    ant.set_direction("O")
    assert ant.direction != "O"
    assert ant.direction == "N"
    ant.set_direction("S")
    assert ant.direction != "N"
    assert ant.direction == "S"


def test_ant_going():
    ant = Ant((30, 20), "N")
    ant.go("E")
    assert ant.position_x == 31
    assert ant.position_y == 20
    assert ant.direction == "E"
    ant.go("D")
    assert ant.direction != "D"
    assert ant.position_x == 31
    assert ant.position_y == 20


def test_create_ant_position():
    path_pic = os.path.join(os.getcwd(), "tests/pic_to_test1.png")
    picture = Image.open(path_pic)
    board = BoardReader(picture)
    ant = Ant((30, 20), "N")
    pos_x, pos_y = ant.create_ant_position(board)
    assert pos_x == 2
    assert pos_y == 2

from Simulator import Simulator
from PIL import Image
import os
import ImageInput
import numpy as np


path_to_pic1 = os.path.join(os.getcwd(), "tests/pic_to_test1.png")
path_to_pic2 = os.path.join(os.getcwd(), "tests/pic_to_test2.png")
picture1 = ImageInput.convert_to_black_and_white(Image.open(path_to_pic1))
simulator1 = Simulator(100, picture1)
picture2 = ImageInput.convert_to_black_and_white(Image.open(path_to_pic2))
simulator2 = Simulator(100, picture2)


def test_creating_ant():
    ant = simulator1.create_ant(simulator1._ant_board)
    assert ant.position_x == 2
    assert ant.position_y == 2
    assert ant.direction == "N"


def test_steps_getter():
    assert simulator1.steps == 100


def test_board_getter():
    array = np.array([
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
    ])
    simulator_board = simulator1.board
    for x in range(5):
        for y in range(5):
            assert array[y, x] == simulator_board.get_pos_value(x, y)


def test_short_simulation_1():
    array = np.array([
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
    ])
    simulator1.take_step()
    array[2, 2] = 0
    assert array[2, 2] == simulator1.board.get_pos_value(2, 2)
    assert simulator1.ant.position_x == 3
    assert simulator1.ant.position_y == 2
    assert simulator1.ant.direction == "E"
    simulator1.take_step()
    array[2, 3] = 1
    assert array[2, 3] == simulator1.board.get_pos_value(3, 2)
    assert simulator1.ant.position_x == 3
    assert simulator1.ant.position_y == 1
    assert simulator1.ant.direction == "N"
    simulator1.take_step()
    array[1, 3] = 1
    assert array[1, 3] == simulator1.board.get_pos_value(3, 1)
    assert simulator1.ant.position_x == 2
    assert simulator1.ant.position_y == 1
    assert simulator1.ant.direction == "W"
    simulator1.take_step()
    array[1, 2] = 0
    assert array[1, 2] == simulator1.board.get_pos_value(2, 1)
    assert simulator1.ant.position_x == 2
    assert simulator1.ant.position_y == 0
    assert simulator1.ant.direction == "N"


def test_short_simulation_2():
    array = np.array([
        [1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1],
    ])
    assert simulator2.ant.position_x == 3
    assert simulator2.ant.position_y == 1
    simulator2.take_step()
    array[1, 3] = 1
    assert array[1, 3] == simulator2.board.get_pos_value(3, 1)
    assert simulator2.ant.position_x == 2
    assert simulator2.ant.position_y == 1
    assert simulator2.ant.direction == "W"
    simulator2.take_step()
    array[1, 2] = 1
    assert array[1, 2] == simulator2.board.get_pos_value(2, 1)
    assert simulator2.ant.position_x == 2
    assert simulator2.ant.position_y == 2
    assert simulator2.ant.direction == "S"
    simulator2.take_step()
    array[2, 2] = 0
    assert array[2, 2] == simulator2.board.get_pos_value(2, 2)
    assert simulator2.ant.position_x == 1
    assert simulator2.ant.position_y == 2
    assert simulator2.ant.direction == "W"
    simulator2.take_step()
    array[2, 1] = 1
    assert array[2, 1] == simulator2.board.get_pos_value(1, 2)
    assert simulator2.ant.position_y != 3


def test_blank_picture():
    picture = ImageInput.create_white_picture(5, 5)
    simulator = Simulator(10, picture)
    array = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ])
    for x in range(5):
        for y in range(5):
            assert array[y, x] == simulator.board.get_pos_value(x, y)
    simulator.take_step()
    array[2, 2] = 1
    assert simulator.board.get_pos_value(2, 2) == array[2, 2]
    assert simulator.ant.position_x == 1
    assert simulator.ant.position_y == 2
    assert simulator.ant.direction == "W"
    simulator.take_step()
    array[2, 1] = 1
    assert simulator.board.get_pos_value(1, 2) == array[2, 1]
    assert simulator.ant.position_x == 1
    assert simulator.ant.position_y == 3
    assert simulator.ant.direction == "S"
    simulator.take_step()
    array[3, 1] = 1
    assert simulator.board.get_pos_value(1, 3) == array[3, 1]
    assert simulator.ant.position_x == 2
    assert simulator.ant.position_y == 3
    assert simulator.ant.direction == "E"
    simulator.take_step()
    array[3, 2] = 1
    assert simulator.board.get_pos_value(2, 3) == array[3, 2]
    assert simulator.ant.position_x == 2
    assert simulator.ant.position_y == 2
    assert simulator.ant.direction == "N"
    simulator.take_step()
    array[2, 2] = 0
    assert simulator.board.get_pos_value(2, 2) == array[2, 2]
    assert simulator.ant.position_x == 3
    assert simulator.ant.position_y == 2
    assert simulator.ant.direction == "E"
    simulator.take_step()
    array[2, 3] = 1
    assert simulator.board.get_pos_value(3, 2) == array[2, 3]
    assert simulator.ant.position_x == 3
    assert simulator.ant.position_y == 1
    assert simulator.ant.direction == "N"
    simulator.take_step()
    array[1, 3] = 1
    assert simulator.board.get_pos_value(2, 2) == array[2, 2]
    assert simulator.ant.position_x == 2
    assert simulator.ant.position_y == 1
    assert simulator.ant.direction == "W"
    simulator.take_step()
    array[1, 2] = 1
    assert simulator.board.get_pos_value(2, 1) == array[1, 2]
    assert simulator.ant.position_x == 2
    assert simulator.ant.position_y == 2
    assert simulator.ant.direction == "S"
    simulator.take_step()
    array[2, 2] = 1
    assert simulator.board.get_pos_value(2, 2) == array[2, 2]
    assert simulator.ant.position_x == 3
    assert simulator.ant.position_y == 2
    assert simulator.ant.direction == "E"
    simulator.take_step()
    array[2, 3] = 0
    assert simulator.board.get_pos_value(3, 2) == array[2, 3]
    assert simulator.ant.position_x == 3
    assert simulator.ant.position_y == 3
    assert simulator.ant.direction == "S"

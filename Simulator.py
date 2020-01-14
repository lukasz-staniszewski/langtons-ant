from BoardReader import BoardReader
from Ant import Ant
import ImageOutput as ImgOut
import random


class Simulator:
    """
    ~ Class Simulator represents simulator.
    Arguments:
    :param steps: steps to do by ant
    :type steps: int

    :param picture: picture on which ant starts walking
    :type picture: pil.Image
    """
    def __init__(self, steps, picture):
        """
        ~ Class Simulator constructor.
        """
        ant_board = BoardReader(picture)
        self._ant_board = ant_board
        self._ant = self.create_ant(ant_board)
        self._steps = steps

    def create_ant(self, board):
        """
        ~ Method helps class Simulator constructor
            with creating ant.
        """
        new_pos = Ant((0, 0), "N").create_ant_position(board)
        return Ant(new_pos, "N")

    @property
    def ant(self):
        """
        ~ Property Simulator.ant getter.
        """
        return self._ant

    @property
    def board(self):
        """
        ~ Property board getter.
        """
        return self._ant_board

    @property
    def steps(self):
        """
        ~ Property steps getter.
        """
        return self._steps

    def simulate(self):
        """
        ~ Method's functionality is to start simulation with object from
            class Simulator. In loop ant moves and method saves actual
                boardstate to .jpg file in "Steps" folder.
        """
        fold_path = ImgOut.create_folder_and_return_path("Steps")
        for step in range(1, self.steps + 1):
            self.take_step()
            ImgOut.save_to_picture_file(self.board, fold_path, step)

    def take_step(self):
        """
        ~ Method is simulating single step, taking by ant
            on board from Simulator object.


        Algorithm:
            1) If ant take "0" place on board, changes it to "1" and moves
                90 degrees left
            2) Otherwise if ant take "1" place on board, changes it to "0"
                and moves 90 degrees right
        """
        ant_dir = self.ant.direction
        ant_pos_x = self.ant.position_x
        ant_pos_y = self.ant.position_y
        if self.board.get_pos_value(ant_pos_x, ant_pos_y) == 1:
            self.board.set_value_on_pos(ant_pos_x, ant_pos_y, 0)
            if ant_dir == "N":
                self.move_ant_to_east()
            elif ant_dir == "S":
                self.move_ant_to_west()
            elif ant_dir == "W":
                self.move_ant_to_north()
            elif ant_dir == "E":
                self.move_ant_to_south()
        else:
            self.board.set_value_on_pos(ant_pos_x, ant_pos_y, 1)
            if ant_dir == "N":
                self.move_ant_to_west()
            elif ant_dir == "S":
                self.move_ant_to_east()
            elif ant_dir == "W":
                self.move_ant_to_south()
            elif ant_dir == "E":
                self.move_ant_to_north()

    def pick_random_direction_and_go(self, list_of_directions):
        """
        ~ Method picks one of  the given in list direction and
            moves ant in that direction
        Atributes:
        :param list_of_directions: list with directions to go
        :type list_of_directions: list of strings
        """
        random_direction = random.choice(list_of_directions)
        self.ant.go(random_direction)

    def move_ant_to_north(self):
        """
        ~ Function moves ant to NORTH on board.
            If ant's position is on board's edge,
                then it moves ant one of the possible directions to go.
        """
        board_width = self.board.get_board_size()[1]
        pos_y = self.ant.position_y
        pos_x = self.ant.position_x
        if pos_y == 0 and pos_x == 0:
            self.pick_random_direction_and_go(["E", "S"])
        elif pos_y == 0 and pos_x == board_width - 1:
            self.pick_random_direction_and_go(["W", "S"])
        elif pos_y == 0:
            self.pick_random_direction_and_go(["E", "W", "S"])
        else:
            self.ant.go("N")

    def move_ant_to_south(self):
        """
        ~ Function moves ant to SOUTH on board.
            If ant's position is on board's edge,
                then it moves ant one of the possible directions to go.
        """
        board_height, board_width = self.board.get_board_size()
        pos_y = self.ant.position_y
        pos_x = self.ant.position_x
        if pos_y == board_height - 1 and pos_x == 0:
            self.pick_random_direction_and_go(["E", "N"])
        elif pos_y == board_height - 1 and pos_x == board_width - 1:
            self.pick_random_direction_and_go(["W", "N"])
        elif pos_y == board_height - 1:
            self.pick_random_direction_and_go(["E", "W", "N"])
        else:
            self.ant.go("S")

    def move_ant_to_east(self):
        """
        ~ Function moves ant to EAST on board.
            If ant's position is on board's edge,
                then it moves ant one of the possible directions to go.
        """
        board_height, board_width = self.board.get_board_size()
        pos_y = self.ant.position_y
        pos_x = self.ant.position_x
        if pos_x == board_width - 1 and pos_y == 0:
            self.pick_random_direction_and_go(["W", "S"])
        elif pos_x == board_width - 1 and pos_y == board_height - 1:
            self.pick_random_direction_and_go(["W", "N"])
        elif pos_x == board_width - 1:
            self.pick_random_direction_and_go(["W", "S", "N"])
        else:
            self.ant.go("E")

    def move_ant_to_west(self):
        """
        ~ Function moves ant to WEST on board.
            If ant's position is on board's edge,
                then it moves ant one of the possible directions to go.
        """
        board_height = self.board.get_board_size()[0]
        pos_y = self.ant.position_y
        pos_x = self.ant.position_x
        if pos_x == 0 and pos_y == 0:
            self.pick_random_direction_and_go(["E", "S"])
        elif pos_x == 0 and pos_y == board_height - 1:
            self.pick_random_direction_and_go(["E", "N"])
        elif pos_x == 0:
            self.pick_random_direction_and_go(["E", "S", "N"])
        else:
            self.ant.go("W")

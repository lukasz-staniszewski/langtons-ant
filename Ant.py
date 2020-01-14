class Ant:
    """
    Class Ant. Contains atributes:

    :param directions: directions the ant is moving in
    :type directions: set

    :param _position_x: position x of ant
    :type _position_x: int

    :param _position_y: position y of ant
    :type _position_y: int
    """
    directions = {"N", "S", "E", "W"}

    def __init__(self, position, direction):
        """
        ~ Class Ant constructor.
        Atributes:
        :param position: tuple containing of (position_x, position_y)
        :type position: tuple of ints

        :param direction: direction to go of ant, must be "N"/"S"/"E"/"W"
        :type direction: string
        """
        self._position_x = position[0]
        self._position_y = position[1]
        self._direction = direction

    @property
    def position_x(self):
        """
        ~ Ant._position_x getter.
        """
        return self._position_x

    @property
    def position_y(self):
        """
        ~ Ant._position_y getter.
        """
        return self._position_y

    @property
    def direction(self):
        """
        ~ Ant._direction getter.
        """
        return self._direction

    def set_direction(self, where_to_move):
        """
        ~ Ant._direction setter.
        """
        if where_to_move in self.directions:
            self._direction = where_to_move

    def set_position(self, new_x, new_y):
        """
        ~ Ant._position setter.
        Arguments:
        :param new_x: new _position_x of Ant
        :type new_x: int

        :param new_y: new _position_y of Ant
        :type new_y: int
        """
        self._position_x = new_x
        self._position_y = new_y

    def create_ant_position(self, board):
        """
        ~ Function returns tulpe, which contains ant's  starting
            position_x and position_y on board (middle of board).


        Arguments:
        :arg ant_board: board on which ant is
        :type ant_board: np.array
        """
        board_height, board_width = board.get_board_size()
        return board_width // 2, board_height // 2

    def go(self, direction):
        """
        ~ Method of class Ant which moves Ant to given direction.
        Atributes:

        :atr direction: direction in which Ant will move [N/S/E/W]
        :type direction: string
        """
        if direction in self.directions:
            if direction == "N":
                self.set_position(self.position_x, self.position_y - 1)
            elif direction == "S":
                self.set_position(self.position_x, self.position_y + 1)
            elif direction == "E":
                self.set_position(self.position_x + 1, self.position_y)
            else:
                self.set_position(self.position_x - 1, self.position_y)
            self.set_direction(direction)

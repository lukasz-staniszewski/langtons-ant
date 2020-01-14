import numpy as np


class BoardReader:
    """
    ~ Class BoardReader represents single board reader from picture.
    Arguments:
    :param picture: picture from which board will be created
    :type picture: pil.Image
    """
    def __init__(self, picture):
        """
        ~ Class BoardReader constructor.
        """
        self.board = self.create_board_from_picture(picture)

    def get_board_size(self):
        """
        ~ Function returns size of board.
        """
        return self.board.shape

    def set_value_on_pos(self, posx, posy, value):
        """
        ~ Method sets value 1 or 0 on board on given positionX and
            given position Y.
        Parameteres:
        :param posx: position X on board
        :type posx: int

        :param posy: position Y on board
        :type posy: int

        :param value: number 1 or 0, which will be on board
        :type value: int
        """
        b_height, b_width = self.get_board_size()
        if value in {0, 1} and 0 <= posx < b_width and 0 <= posy < b_height:
            self.board[posy, posx] = value

    def get_pos_value(self, posx, posy):
        """
        ~ Method returns value of board on given positionX and
            given positionY.
        """
        return self.board[posy, posx]

    def create_board_from_picture(self, picture):
        """
        ~ Function creates and returns board for ant (numpy array)
            from given black and white picture.
        Algorithm:
            1) if pixel on (x, y) is white =>
                    array value on (x, y) position is 0 (int)
            2) otherwise if pixel on (x, y) is black =>
                    array value on (x, y) is 1 (int)
        Arguments:
        :arg picture: picture from which function creates board
        :type picture: PIP.Image
        """
        width, height = picture.size
        # creating new numpy array
        board = np.empty((height, width), dtype=int)
        for pix_col in range(width):
            for pix_row in range(height):
                if picture.getpixel((pix_col, pix_row)) == 0:
                    board[pix_row, pix_col] = 1
                else:
                    board[pix_row, pix_col] = 0
        return board

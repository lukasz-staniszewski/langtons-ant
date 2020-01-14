"""
File ImageOutput is responsible for connecting with system.
I.a. it creates pictures and folders, saves pictures, converts them.
"""

import os
from PIL import Image
import pygame as pg


def save_to_picture_file(board, path_to_fold, step):
    """
    ~ Function saves given board to file to given path(path_to_fold)
        with name "step_{step}" as .jpg file. Additionaly picture, before
            saving, will be erased 4 times for better visibility. Moreover
                it resizes picture to 400x400 and returns it in order to
                    display it on screen.
    Arguments:
    :arg board: ant's board which will be saved to file
    :type board: np.array

    :arg path_to_fold: path to which new image will be saved
    :type path_to_fold: os.path

    :arg step: number of steps to take by ant
    :type step: int
    """
    # creating picture, path to picture
    picture = create_picture_from_board(board)
    file_name = f"step_{step}.jpg"
    full_path = os.path.join(path_to_fold, file_name)
    # erasing picture 4 times to better visability and saving
    picture_erased = erase_picture_4_times(picture)
    picture_erased.save(full_path)
    # resizing picture to 400x400 in order to working on gui
    picture_resized = resize_picture(picture, (400, 400))
    return convert_pill_pic_to_pygame_surf(picture_resized)


def create_picture_from_board(board):
    """
    ~ Function creates picture from given board
        and returns it.
    Arguments:
    :arg board: array from which picture will be created
    :type board: np.array
    """
    # Getting width, height and creating white pil.image
    pic_height, pic_width = board.get_board_size()
    picture = Image.new("1", (pic_width, pic_height), (1))
    # Algorithm: 1 on positon (x, y) = black pixel on image on pos(x, y)
    for pix_col in range(pic_width):
        for pix_row in range(pic_height):
            if board.get_pos_value(pix_col, pix_row) == 1:
                picture.putpixel((pix_col, pix_row), (0))
            else:
                picture.putpixel((pix_col, pix_row), (1))
    return picture


def erase_picture_4_times(picture):
    """
    ~ Function creates new picture which is erased 4 times from
        given picture and returns it.


    Arguments:
    :arg picture: picture which will be 4 times erased
    :type picture: PIL.image
    """
    pic_w, pic_h = picture.size
    big_pic = Image.new("1", (pic_w * 4, pic_h * 4), (1))
    for p_col in range(pic_w):
        for p_row in range(pic_h):
            if picture.getpixel((p_col, p_row)) == (0):
                for x in range(4):
                    for y in range(4):
                        big_pic.putpixel((p_col * 4 + x, p_row * 4 + y), (0))
    return big_pic


def resize_picture(picture, new_size):
    """
    ~ Function changes size of given picture to
        new size and returns it.
    """
    resized_picture = picture.resize(new_size)
    return resized_picture


def convert_pill_pic_to_pygame_surf(image):
    """
    ~ Funtion is needed to create and return image for pygame library
        from pillow library.
    """
    image = image.convert("RGB")
    return pg.image.fromstring(image.tobytes(), image.size, image.mode)


def create_folder_and_return_path(folder_name):
    """
    ~ Function creates folder in program's path with given name
        (if there is no folder with that name in program path)
            and returns path to that folder.


    Arguments:
    :arg name: name of folder that will be created
    :type name: string
    """
    current_path = os.getcwd()
    full_path = os.path.join(current_path, folder_name)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    return full_path

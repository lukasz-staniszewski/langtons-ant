"""
File ImageInput is responsible for starting phase of project.
I.e. it takes data from user and converts it to program data.
"""
import ConsoleExceptions as cexc
from PIL import Image
import random
from Simulator import Simulator
import LangtonGui
import GuiExceptions as gexc


MAX_STEPS = 30000


def start(number):
    """
    ~ Function starts program in gui if given number is 1.
        Else if number is 2, function starts program in console.
    """
    if number not in {1, 2}:
        number = 1
    if number == 1:
        start_with_gui()
    else:
        start_with_console()


def start_with_console():
    """
    ~ FUNCTION IS RESPONSIBLE FOR STARTING PROGRAM
        IN CONSOLE.
    """
    print_welcome()
    option = input("Choose a number [1/2/3]: ")
    cexc.check_start_exceptions(option)
    if option == "1":
        picture = create_white_picture_with_inputs()
    elif option == "2":
        picture = load_picture_with_inputs()
    elif option == "3":
        picture = create_probability_picture_with_inputs()
    steps = get_steps(input("Give a number of steps to do (max=30000): "))
    print_big_number_announcement(steps)
    Simulator(steps, picture).simulate()


def create_white_picture_with_inputs():
    """
    FOR CONSOLE VERSION!
    ~ Function communicates with user. Takes necessary data from him:
        1) width of picture to create
        2) height of picture to create
      Also it checks correctness of given data.
      If everything is all right, function returns pil.image.
    """
    pic_width = input("Give picture width: ")
    cexc.check_creating_picture_exceptions(pic_width)
    pic_height = input("Give picture height: ")
    cexc.check_creating_picture_exceptions(pic_height)
    return create_white_picture(int(pic_width), int(pic_height))


def load_picture_with_inputs():
    """
    FOR CONSOLE VERSION!
    ~ Function communicates with user. Takes necessary data from him:
        1) path to file, which he wants to load
      Also it checks whether given path exists and if so, returns picture.
    """
    path = input("Give file path, name, and extension [ex. path/pic.jpg]: ")
    cexc.check_load_picture_exceptions(path)
    return load_picture(path)


def create_probability_picture_with_inputs():
    """
    FOR CONSOLE VERSION!
    ~ Function communicates with user. Takes necessary data from him:
        1) probability of occurance of black pixel on white picture
      Also it checks correctness of given data.
      If everything is all right, function returns pil.image.
    """
    probability = input("Give probability [0-1): ")
    cexc.check_probability_exceptions(probability)
    wh_picture = create_white_picture_with_inputs()
    return create_probability_picture(wh_picture, float(probability))


def print_welcome():
    """
    FOR CONSOLE VERSION!
    ~ Function prints welcome message.
    """
    print("Welcome to Langton's ant simulator! Choose option: ")
    print("1 -> Create white blank picture")
    print("2 -> Load file")
    print("3 -> Generate picture with given probability")


def print_big_number_announcement(steps):
    """
    FOR CONSOLE VERSION!
    ~ Function prints announcement if given steps
        are bigger than 5000.
    """
    if steps > 5000:
        print("It will take a while...")


def start_with_gui():
    """
    ~ FUNCTION IS RESPONSIBLE FOR STARTING PROGRAM
        IN GUI.
    """
    try:
        gui = LangtonGui.LangtonGui()
        gui.play_starting_loop()
    except gexc.QuitButtonError:
        print("USER  QUITTED!")


def create_white_picture(pic_width, pic_height):
    """
    ~ Function creates white picture with given width and height
        and returns it.
    """
    white_picture = Image.new("1", (pic_width, pic_height), (1))
    return white_picture


def create_probability_picture(wh_picture, probability):
    """
    ~ Function creates black and white picture by given probability
        from given wh_picture and and returns it.
    """
    picture = convert_picture_with_probability(wh_picture, float(probability))
    return picture


def convert_picture_with_probability(picture, probability):
    """
    ~ Function converts given white picture to new picture with given
        probability of occurence of black pixel on picture and returns it.
    Arguments:
    :arg picture: white picture to convert
    :type picture: PIL.Image

    :arg probability: probability of occurence of black pixel on image
                      [number between 0 and 1]
    :type probability: float
    """
    pic_width, pic_height = picture.size
    for pix_col in range(pic_width):
        for pix_row in range(pic_height):
            if random.random() <= probability:
                picture.putpixel((pix_col, pix_row), (0))
    return picture


def load_picture(path):
    """
    ~ Function loads picture from given path, converts it to
        black and white and returns that picture as PIL.Image.
    """
    picture = Image.open(path)
    picture_black_and_white = convert_to_black_and_white(picture)
    return picture_black_and_white


def convert_to_black_and_white(picture):
    """
    ~ Function returns given picture but converted to
        black and white form.
    Arguments:
    :arg picture: picture to convert
    :type picture: PIL.Image
    """
    picture_black_white = picture.convert('1')
    return picture_black_white


def get_steps(steps):
    """
    ~ Function convert given steps to number.
        If number of steps is bigger than MAX_STEPS,
            function return MAX_STEPS.
    Arguments:
    :arg steps: number of steps to take by ant
    :type steps: string
    """
    cexc.step_exceptions(steps)
    steps_int = int(steps)
    if steps_int > MAX_STEPS:
        steps_int = MAX_STEPS
    return steps_int

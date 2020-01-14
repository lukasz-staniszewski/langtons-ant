import os
from PIL import Image

MAX_ATR = 300
MAX_STEPS = 30000


class QuitButtonError(Exception):
    """
    ~ Raised when user click on quit button.
    """
    pass


class WidthException(Exception):
    """
    ~ Raised when width data error occure.
    """
    pass


class HeightException(Exception):
    """
    ~ Raised when height data error occure.
    """
    pass


class StepsException(Exception):
    """
    ~ Raised when steps data error occure.
    """
    pass


class ProbabilityException(Exception):
    """
    ~ Raised when probability data error occure.
    """
    pass


class PathNotFoundException(Exception):
    """
    ~ Raised when path to file doesnt exist
    """
    pass


class NonPictureFileException(Exception):
    """
    ~ Raised when given file is not picture.
    """
    pass


class TooBigPictureException(Exception):
    """
    ~ Raised when given picture has too big width or height.
    """
    pass


def check_creating_data(width, height, steps, probability=None):
    """
    Function checks correctness of given data in creating picture phase.
    If argument probability is given -> function checks also its correctness.
    """
    # checking whether width is int between 0 and MAX_ATR
    try:
        int_width = int(width)
        if not (0 < int_width <= MAX_ATR):
            raise WidthException
    except (TypeError, ValueError):
        raise WidthException
    # checking whether height is int between 0 and MAX_ATR
    try:
        int_height = int(height)
        if not (0 < int_height <= MAX_ATR):
            raise HeightException
    except (TypeError, ValueError):
        raise HeightException
    # checking whether steps is int between 0 and MAX_STEPS
    try:
        int_steps = int(steps)
        if not (0 < int_steps <= MAX_STEPS):
            raise StepsException
    except (TypeError, ValueError):
        raise StepsException
    if probability is not None:
        # checking whether probability is float between 0 and 1
        try:
            float_probability = float(probability)
            if not (0 <= float_probability < 1):
                raise ProbabilityException
        except (TypeError, ValueError):
            raise ProbabilityException
    # returning data if they  are correct
    if probability:
        return int_width, int_height, int_steps, float_probability
    else:
        return int_width, int_height, int_steps


def check_loading_picture_exceptions(steps, path):
    """
    ~ Function checks correctnes of given data in loading picture phase.
    """
    # checking whether steps is int between 0 and MAX_STEPS
    try:
        int_steps = int(steps)
        if not (0 < int_steps <= MAX_STEPS):
            raise StepsException
    except (TypeError, ValueError):
        raise StepsException
    # checking path corectness
    try:
        actual_path = os.getcwd()
        full_path = os.path.join(actual_path, path)
        # checking whether path exists
        if not os.path.exists(full_path):
            raise PathNotFoundException
        # checking whether given file is .jpg/.png
        ext = os.path.splitext(full_path)[1]
        if ext not in {'.jpg', '.png'}:
            raise NonPictureFileException
        # checking whether height and width of picture arent more than MAX_ATR
        image = Image.open(full_path)
        if image.size[0] > MAX_ATR or image.size[1] > MAX_ATR:
            raise TooBigPictureException
    except NonPictureFileException:
        raise NonPictureFileException
    except TooBigPictureException:
        raise TooBigPictureException
    except Exception:
        raise PathNotFoundException
    # returning correct steps value
    return steps

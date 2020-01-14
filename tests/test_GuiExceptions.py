import GuiExceptions as gexc
import pytest
import os


def test_width_exception():
    with pytest.raises(gexc.WidthException):
        gexc.check_creating_data("bad", 100, 100, 0.23)
    with pytest.raises(gexc.WidthException):
        gexc.check_creating_data(400, 100, 100)


def test_height_exception():
    with pytest.raises(gexc.HeightException):
        gexc.check_creating_data(100, "bad", 100, 0.13)
    with pytest.raises(gexc.HeightException):
        gexc.check_creating_data(100, 0, 100)


def test_steps_exception():
    with pytest.raises(gexc.StepsException):
        gexc.check_creating_data(100, 100, "bad")
    with pytest.raises(gexc.StepsException):
        gexc.check_creating_data(100, 100, 400000)


def test_probability_exception():
    with pytest.raises(gexc.ProbabilityException):
        gexc.check_creating_data(100, 100, 100, "bad")
    with pytest.raises(gexc.ProbabilityException):
        gexc.check_creating_data(100, 100, 100, 3)


def test_PathNotFound_exception():
    actual_path = os.getcwd()
    wrong_name = "tests/wrong_file.png"
    path = os.path.join(actual_path, wrong_name)
    with pytest.raises(gexc.PathNotFoundException):
        gexc.check_loading_picture_exceptions(100, "bad")
    with pytest.raises(gexc.PathNotFoundException):
        gexc.check_loading_picture_exceptions(100, path)


def test_TooBigPicture_exception():
    path = os.path.join(os.getcwd(), "tests/large.png")
    with pytest.raises(gexc.TooBigPictureException):
        gexc.check_loading_picture_exceptions(100, path)


def test_NonPictureFile_exception():
    path = os.path.join(os.getcwd(), "tests/text.txt")
    with pytest.raises(gexc.NonPictureFileException):
        gexc.check_loading_picture_exceptions(100, path)

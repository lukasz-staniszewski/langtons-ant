from Simulator import Simulator
from InputBox import InputBox
import pygame as pg
import ImageOutput as ImgOut
import ImageInput as ImgInp
import GuiExceptions as gexc
import time
import math
pg.init()


class LangtonGui:
    """
    Class LangtonGui is responsible for Gui in simulator.
    Atributes:
    :param window_size: size of gui window. (width, height)
    :type window_size: tulpe of ints

    :param icon: path to icon for gui
    :type icon: string

    :param caption: name of program on bar
    :type caption: string

    :param title: path to picture with name of program on gui display
    :type title: string

    :param author: path to picture with name of author
    :type author: string

    :param frame: path to picture containg frame in which
                  ant is taking steps
    :type frame: string
    """

    def __init__(self, window_size=(1280, 720), icon="gui_files/ant.png",
                 caption="Langton's ant simulator", title="gui_files/logo.png",
                 author="gui_files/author.png", frame="gui_files/frame.png"):
        self.screen = pg.display.set_mode(window_size)
        self.set_window_atributes(icon, caption)
        self.title = pg.image.load(title)
        self.author = pg.image.load(author)
        self.frame_for_ant = pg.image.load(frame)
        self.font = pg.font.Font('freesansbold.ttf', 32)

    def set_window_atributes(self, icon, caption):
        """
        ~ Method sets icon of program and its name
        Atributes:
        :param icon: path to icon for gui
        :type icon: string

        :param caption: name of program on bar
        :type caption: string
        """
        pg.display.set_caption(caption)
        pg.display.set_icon(pg.image.load(icon))

    def play_starting_loop(self):
        """
        ~ Method is responsible for launching phase of program.
        """
        while True:
            self.screen.fill((255, 255, 255))
            # Displaying author and title on the screen
            self.display_title()
            self.display_author()
            # When users exits program
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise gexc.QuitButtonError()
                    pg.quit()
            # Welcoming User
            self.display_starting_screen("gui_files/welcome_text.png")
            # Displaying starting buttons
            self.display_starting_options()
            pg.display.update()

    def display_title(self):
        """
        ~ Method is responsible for displaying title on screen.
        """
        self.screen.blit(self.title, (0, 0))

    def display_author(self):
        """
        ~ Method is responsible for displaying author on screen.
        """
        self.screen.blit(self.author, (0, 620))

    def display_frame_for_ant(self):
        """
        ~ Method is responsible for displaying frame in which
            ant is taking steps.
        """
        self.screen.blit(self.frame_for_ant, (439, 199))

    def display_step_counter_text(self):
        """
        ~ Method is responsible for displaying "ACTUAL STEP"
            text on the screen.
        """
        black = (0, 0, 0)
        text = self.font.render("ACTUAL STEP:", True, black)
        self.screen.blit(text, (450, 160))

    def display_counter(self, number):
        """
        ~ Method is responsible for displaying actual number of
            steps on the screen.
        """
        black = (0, 0, 0)
        text = self.font.render(str(number), True, black)
        self.screen.blit(text, (700, 160))

    def cover_box(self, x, y, width, height):
        """
        ~ Metog is needed to cover something on the screen by white rectangle.
        Atributes:
        :param x: positon x of rectangle
        :type x: int

        :param y: position y of rectangle
        :type y: int

        :param width: width of rectangle
        :type width: int

        :param height: height of rectangle
        :type height: int
        """
        pg.draw.rect(self.screen, (255, 255, 255), (x, y, width, height))

    def display_text(self, msg, pos_x, pos_y):
        """
        ~ Method displays single text on screen.
        Atriburtes:
        :param msg: text to display
        :typem msg: string

        :param pos_x: position x of text
        :type pos_x: int

        :param pos_y: position y of text
        :type pos_y: int
        """
        text = self.font.render(msg, True, (0, 0, 0))
        self.screen.blit(text, (pos_x, pos_y))

    def display_error(self, exception_name):
        # showing errors with given by user data
        path = f"gui_files/exception/{exception_name}.png"
        exc_im = pg.image.load(path)
        self.cover_box(0, 150, 1280, 500)
        self.screen.blit(exc_im, (0, 150))
        pg.display.update()
        time.sleep(3)
        self.screen.fill((255, 255, 255))

    def display_button(self, msg, font_size, x, y, width, height,
                       original_color, hover_color, function):
        """
        ~ Method represents single button functionality in gui.
        Atributes:
        :param msg: text displayed on the button
        :type msg: string

        :param font_size: size of font of text on the button
        :type font_size: int

        :param x: position x of button
        :type x: int

        :param y: position y of button
        :type y: int

        :param width: width of button
        :type width: int

        :param height: height of button
        :type height: int

        :param original_color: color of button when mouse cursor isnt on it
        :type original_color: tulpe of ints

        :param hover_color: color of button when mouse cursos is on it
        :type hover_color: tulpe of ints

        :param function: function which will be called when button is clicked
        :type function: function name
        """
        # Necessary colors, mouse position variable
        col_black = (0, 0, 0)
        col_white = (255, 255, 255)
        mouse_pos = pg.mouse.get_pos()
        # Variable left_click equals 1 if left mouse button is clicked
        left_click = pg.mouse.get_pressed()[0]
        # Font and text on buttons
        buttons_font = pg.font.Font('freesansbold.ttf', font_size)
        button_text = buttons_font.render(msg, True, col_black)
        button_text_hover = buttons_font.render(msg, True, col_white)
        # Nedeed to get text in button center
        button_text_rect = button_text.get_rect()
        button_text_rect.center = (x + (width / 2), y + (height / 2))
        # When cursor is on button
        if x + width > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
            pg.draw.rect(self.screen, hover_color, (x, y, width, height))
            self.screen.blit(button_text_hover, button_text_rect)
            # If left button on mouse is clicked
            if left_click == 1:
                # Calling function
                function()
        # When cursor isnt on button
        else:
            pg.draw.rect(self.screen, original_color, (x, y, width, height))
            self.screen.blit(button_text, button_text_rect)

    def display_starting_screen(self, path):
        """
        ~ Method is responsible for displaying welcoming text
            on screen.
        Atributes:
        :param path: path to picture containg welcome message
        :type path: string
        """
        welcome_text = pg.image.load(path)
        self.screen.blit(welcome_text, (320, 175))

    def display_starting_options(self):
        """
        ~ Function is responsible for displaying buttons on start.
        """
        # Necessary colors
        red_color = (204, 0, 0)
        hover_color = (255, 102, 102)
        self.display_button("Create white picture", 18, 120, 350, 200, 100,
                            red_color, hover_color, self.create_picture_gui)
        self.display_button("Load picture", 24, 540, 350, 200, 100,
                            red_color, hover_color, self.load_picture_gui)
        self.display_button("Create picture with probability", 12, 960, 350,
                            200, 100, red_color, hover_color,
                            self.probability_picture_gui)

    def create_picture_gui(self):
        """
        ~ Function is responsible for displaying gui when user chooses to
            create new_picture.
        """
        self.screen.fill((255, 255, 255))  # asd
        self.display_author()
        self.display_title()
        # Getting width, height and steps from input boxes.
        w, h, s, _ = self.display_creating_picture_boxes()
        # Checking data validate
        try:
            width, height, steps = gexc.check_creating_data(w, h, s)
        # Checks whether width is int
        except gexc.WidthException:
            self.display_error("width")
            self.create_picture_gui()
        # Checks whether height is int
        except gexc.HeightException:
            self.display_error("height")
            self.create_picture_gui()
        # Checks whether steps is int
        except gexc.StepsException:
            self.display_error("steps")
            self.create_picture_gui()
        # Creating white picture from user's data
        white_picture = ImgInp.create_white_picture(width, height)
        # Makes a simulation
        self.make_simulation(steps, white_picture)

    def display_info_creating_pictures(self, with_probability=False):
        """
        ~ Method displays info for creating new picture input boxes.
            If argument of function is True -> additionaly displays info
                for probability input box.
        Atributes:
        :param with_probability: True if users want to create picture with
                                 probability of occurance of black pixel
        :type with_probability: bool
        """
        text = "PLEASE TYPE NECESSARY DATA AND PRESS ENTER!"
        self.display_text(text, 190, 160)
        text = "ENTER WIDTH [NUMBER]:"
        self.display_text(text, 50, 250)
        text = "ENTER HEIGHT [NUMBER]:"
        self.display_text(text, 50, 350)
        text = "ENTER STEPS TO DO [NUMBER]:"
        self.display_text(text, 50, 450)
        if with_probability:
            text = "ENTER PROBABILITY [NUMBER (0-1)]:"
            self.display_text(text, 50, 550)
        pg.display.update()

    def display_creating_picture_boxes(self, with_probability=False):
        """
        ~ Method is responsible for creating input boxes if user choose
            creating new picture option. If argument with_probability is
                True, method creates input box for probability.
                    Method returns data from input boxes.
        Arguments:
        :param with_probability: True if user want to create new picture with
                                 probability of occurence of black pixel on it
        :type with_probability: bool
        """
        # needed colors and input boxes
        red_color = (204, 0, 0)
        hov_color = (255, 102, 102)
        width_box = InputBox(700, 245, 200, 40, red_color, hov_color)
        height_box = InputBox(700, 345, 200, 40, red_color, hov_color)
        steps_box = InputBox(700, 445, 200, 40, red_color, hov_color)
        probability_box = None
        if with_probability:
            probability_box = InputBox(700, 545, 200, 40,
                                       red_color, hov_color)
        # displaying info of input boxes on screen
        self.display_info_creating_pictures(with_probability)
        return self.run_creating_picture_boxes(width_box, height_box,
                                               steps_box, probability_box)

    def run_creating_picture_boxes(self, w_box, h_box, s_box, p_box=None):
        """
        ~ Method is responsible for functionality of input boxes in creating
            new white picture option. If p_box isnt None, method is also
                responsible for probability input box functionality. Method
                    returns data in all input boxes.
        Arguments:
        :param w_box: width input box
        :type w_box: InputBox.InputBox

        :param h_box: height input box
        :type h_box: InputBox.InputBox

        :param s_box: steps input box
        :type s_box: InputBox.InputBox

        :param p_box: probability input box
        :type p_box: InputBox.InputBox
        """
        input_boxes = [w_box, h_box, s_box]
        if p_box is not None:
            input_boxes.append(p_box)
        # variables necessary for re-typing data in input box
        new_width = new_height = new_steps = new_probability = None
        while True:
            # mouse position and quit button exception
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise gexc.QuitButtonError()
                    pg.quit()
                # getting width data
                width = w_box.click_on_box(event, mouse_pos)
                if width is not None:
                    # displaying "OK!" if enter is typed
                    self.display_text("OK!", 950, 250)
                    new_width = width
                # getting height data
                height = h_box.click_on_box(event, mouse_pos)
                if height is not None:
                    # displaying "OK!" if enter is typed
                    self.display_text("OK!", 950, 350)
                    new_height = height
                # getting steps data
                steps = s_box.click_on_box(event, mouse_pos)
                if steps is not None:
                    # displaying "OK!" if enter is typed
                    self.display_text("OK!", 950, 450)
                    new_steps = steps
                # getting probability data
                if p_box is not None:
                    probability = p_box.click_on_box(event, mouse_pos)
                    if probability is not None:
                        # displaying "OK!" if enter is typed
                        self.display_text("OK!", 950, 550)
                        new_probability = probability
            # covering all boxes for backspace
            self.cover_box(700, 250, 200, 40)
            self.cover_box(700, 350, 200, 40)
            self.cover_box(700, 450, 200, 40)
            if p_box is not None:
                self.cover_box(700, 550, 200, 40)
            # showing all boxes
            for input_box in input_boxes:
                input_box.display_box(self.screen)
            pg.display.update()
            # if all input boxes were entered function returns data from them
            if new_width and new_height and new_steps:
                if p_box is None or new_probability:
                    return new_width, new_height, new_steps, new_probability

    def probability_picture_gui(self):
        """
        ~ Method is responsible for displaying gui if user choose creating
            new white picture with probability of occurance of black pixel.
        """
        self.screen.fill((255, 255, 255))
        self.display_author()
        self.display_title()
        # getting width, height, steps and probablity
        w, h, s, p = self.display_creating_picture_boxes(True)
        # checking whether data is correct
        try:
            # converts input data to necessary types
            wid, height, steps, prob = gexc.check_creating_data(w, h, s, p)
        # correct width
        except gexc.WidthException:
            self.display_error("width")
            self.probability_picture_gui()
        # correct height
        except gexc.HeightException:
            self.display_error("height")
            self.probability_picture_gui()
        # correct steps
        except gexc.StepsException:
            self.display_error("steps")
            self.probability_picture_gui()
        # correct probablity
        except gexc.ProbabilityException:
            self.display_error("probability")
            self.probability_picture_gui()
        # creating white picture, converting it to picture with probability
        white_picture = ImgInp.create_white_picture(wid, height)
        prob_picture = ImgInp.create_probability_picture(white_picture, prob)
        # making a simulation
        self.make_simulation(steps, prob_picture)

    def load_picture_gui(self):
        """
        ~ Method takes responsible for creating gui look when users choose
            to load his own picture.
        """
        # Displaying information about author and title of program
        self.screen.fill((255, 255, 255))
        self.display_author()
        self.display_title()
        # Getting necessary data to process
        path, steps = self.display_loading_picture_boxes()
        # Checking correctness of given path and steps
        try:
            steps = gexc.check_loading_picture_exceptions(steps, path)
        except gexc.StepsException:
            self.display_error("steps")
            self.load_picture_gui()
        except gexc.NonPictureFileException:
            self.display_error("non-picture")
            self.load_picture_gui()
        except gexc.TooBigPictureException:
            self.display_error("too_big_image")
            self.load_picture_gui()
        except gexc.PathNotFoundException:
            self.display_error("path_not_found")
            self.load_picture_gui()
        # Creating pil.image variable
        loaded_picture = ImgInp.load_picture(path)
        # Simulating
        self.make_simulation(int(steps), loaded_picture)

    def display_info_loading_pictures(self):
        """
        ~ Method display info for loading picture gui.
        """
        text = "PLEASE TYPE NECESSARY DATA AND PRESS ENTER!"
        self.display_text(text, 190, 160)
        text = "ENTER PATH TO FILE:"
        self.display_text(text, 50, 250)
        text = "ENTER STEPS TO DO [NUMBER]:"
        self.display_text(text, 50, 350)
        pg.display.update()

    def display_loading_picture_boxes(self):
        """
        ~ Method displays input boxes for Loading Picture
            option and returns data typed in them.
        """
        # Necessary collors in rgb
        red_color = (204, 0, 0)
        hov_color = (255, 102, 102)
        # Creating input boxes
        path_input_box = InputBox(700, 245, 400, 40, red_color, hov_color)
        steps_input_box = InputBox(700, 345, 200, 40, red_color, hov_color)
        # Displaying info on screen
        self.display_info_loading_pictures()
        # Gets data from input boxes and returns it
        return self.run_loading_picture_boxes(path_input_box, steps_input_box)

    def run_loading_picture_boxes(self, path_box, steps_box):
        """
        ~ Method is responsible for functionality of input boxes in loading
            picture option. Method returns data from all input boxes.
        Arguments:
        :param path_box: path input box
        :type path_box: InputBox.InputBox

        :param steps_box: steps input box
        :type steps_box: InputBox.InputBox
        """
        input_boxes = [path_box, steps_box]
        # variables necessary to re-typing data in input boxes
        new_path = new_steps = None
        while True:
            # mouse position, quit button exception
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise gexc.QuitButtonError()
                    pg.quit()
                # getting path from input
                path = path_box.click_on_box(event, mouse_pos)
                if path is not None:
                    self.display_text("OK!", 1150, 250)
                    new_path = path
                # getting steps from input
                steps = steps_box.click_on_box(event, mouse_pos)
                if steps is not None:
                    self.display_text("OK!", 950, 350)
                    new_steps = steps
            # covering input boxes for backspace functionality
            self.cover_box(700, 245, 400, 40)
            self.cover_box(700, 345, 200, 40)
            # displaying input boxes
            for input_box in input_boxes:
                input_box.display_box(self.screen)
            pg.display.update()
            # if all data is entered, returns it
            if new_path and new_steps:
                return new_path, new_steps

    def make_simulation(self, steps, picture):
        """
        ~ Method takes responsible for creating loop where
            on given picture ant takes given steps.ArithmeticError
        Atributes:
        :param steps: steps to do
        :type steps: int

        :param picture: picture from which board for ant is being created
        :type picture: pil.image
        """
        # Initializing Simulator
        self.simulator = Simulator(steps, picture)
        # Necessary to show ant depending on whether button was clicked
        self.is_showing_ant = False
        step = 1
        # Creating folder where will be all .jpg files
        fold_path = ImgOut.create_folder_and_return_path("Steps")
        while True:
            self.screen.fill((255, 255, 255))
            self.display_title()
            self.display_author()
            # User clicking exit
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise gexc.QuitButtonError()
                    pg.quit()
            self.display_frame_for_ant()
            self.display_step_counter_text()
            # Algorithm
            if step <= steps:
                self.simulator.take_step()
                # Saving actual board to .jpg file by erasing it 4 times
                pic_res = ImgOut.save_to_picture_file(self.simulator.board,
                                                      fold_path, step)
                # Showing actual board on gui screen
                self.screen.blit(pic_res, (440, 200))
                # Displaying ant depending on clicking button
                self.show_ant(picture, pic_res)
                # Showing actual step
                self.display_counter(step)
                if step == steps:
                    self.display_counting_finished()
                step += 1
            pg.display.update()

    def show_ant(self, old_picture, res_picture):
        """
        ~ Method creates and displays on screen a button, which
            function is to show ant on screen. Method will display
                ant on screen, depending on whether button was clicked.
        Atributes:
        :param old_picture: original picture with ant's pathway
        :type picture: PIL.Image

        :param res_picture: resized picture with ant's pathway
        :type res_picture: pg.surf
        """
        org_color = (255, 128, 0)
        hov_color = (255, 166, 77)
        # displaying button
        self.display_button("SHOW ANT", 15, 1000, 350, 100, 100, org_color,
                            hov_color, self.change_showing_ant)
        # if button was clicked, ant is being displayed on screen
        if self.is_showing_ant:
            self.display_ant(old_picture.size, res_picture.get_size())

    def change_showing_ant(self):
        """
        ~ Method necessary to displaying ant on screen. Method's functionality
            is to negate actual value of LangtonGui.is_showing_ant
        """
        self.is_showing_ant = not self.is_showing_ant
        time.sleep(0.5)

    def display_ant(self, old_size, new_size):
        """
        ~ Method shows ant on screen by displaying on screen pixels.
            Method is taking sizes of pictures and depending on it,
                creates small rectangle, which is ant.
        Atributes:
        :param old_size: size of original picture [width, height]
        :type old_size: tulpe of ints

        :param new_size: size of resized picture [width, height]
        :type new_size: tulpe of ints
        """
        image = pg.image.load("gui_files/screen_ant.png")
        # Necessary formula to display correctly  ant on screen
        x_diff = new_size[0] / old_size[0]
        y_diff = new_size[1] / old_size[1]
        # 440 -> position x of displayed board on screen
        pos_x = math.floor(440 + self.simulator.ant.position_x * x_diff)
        # 200 -> position y of displayed board on screen
        pos_y = math.floor(200 + self.simulator.ant.position_y * y_diff)
        for x in range(math.floor(x_diff)):
            for y in range(math.floor(y_diff)):
                self.screen.blit(image, (pos_x + x, pos_y + y))
        pg.display.update()

    def display_counting_finished(self):
        """
        ~ Simple method, displays in infinity loop information
            that all picture has been saved
        """
        white = (255, 255, 255)
        # to make displayed information flashing
        number = 0
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise gexc.QuitButtonError()
                    pg.quit()
            if number % 2 == 0:
                self.display_text("FINISHED", 565, 610)
            else:
                pg.draw.rect(self.screen, white, (565, 610, 200, 50))
            number += 1
            pg.display.update()
            time.sleep(0.5)

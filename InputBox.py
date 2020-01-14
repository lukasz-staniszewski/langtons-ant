import pygame as pg


class InputBox:
    """
    ~ Class InputBox represents input box necessary to Gui working.
    Atributes:
    :param x: position x of input box
    :type x: int

    :param y: position y of input box
    :type y: int

    :param width: width of input box
    :type width: int

    :param height: height of input box
    :type height: int

    :param color_active: color of box when user type data to it
    :type color_active: tuple of ints

    :param color_inactive: color of box when user doesnt type data to it
    :type color_inactive: tuple of ints
    """
    def __init__(self, x, y, width, height,
                 color_active, color_inactive):
        self.x = x
        self.y = y
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.actual_color = color_inactive
        self.surface = pg.Rect(x, y, width, height)
        self.text = ""
        self.font = pg.font.Font("freesansbold.ttf", 32)
        self.text_surface = self.font.render(self.text, True,
                                             self.actual_color)
        self.is_active = False
        self.width = width
        self.height = height

    def display_box(self, screen):
        """
        ~ Method displays input box on gui screen.
        Atributes:
        :param screen: screen on which box will be displayed
        :type screen: LangtonGui.screen
        """
        screen.blit(self.text_surface, (self.surface.x+5, self.surface.y+5))
        pg.draw.rect(screen, self.actual_color, self.surface, 2)

    def click_on_box(self, event, mouse_pos):
        """
        ~ Method do action with input box according to position of mouse and
            mouse button click.
        Atributes:
        :param event: button which is pressed
        :type event: pg.event

        :param mouse_pos: position of mouse
        :type mouse: tulpe of ints
        """
        # Action when input box is clicked
        if event.type == pg.MOUSEBUTTONDOWN:
            # Changing whether input box is active or not
            if (self.x + self.width > mouse_pos[0] > self.x and
               self.y + self.height > mouse_pos[1] > self.y):
                self.is_active = not self.is_active
            else:
                self.is_active = False
            # Changing input box color
            if self.is_active:
                self.actual_color = self.color_active
            else:
                self.actual_color = self.color_inactive
        # Action when input box is active
        if event.type == pg.KEYDOWN:
            if self.is_active:
                # Entering data
                if event.key == pg.K_RETURN:
                    self.is_active = False
                    self.actual_color = self.color_inactive
                    return self.text
                # Deleting last letter
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                # Adding letters
                else:
                    if self.text_surface.get_width() <= self.width - 20:
                        self.text += event.unicode
                self.text_surface = self.font.render(self.text, True,
                                                     self.actual_color)

from src.interface.button import Button
from src.properties.interface import BTN_SIZE, WIDTH


class Menu:
    SPACE = 20

    def __init__(self):
        self._buttons = {}

    @property
    def buttons(self):
        return self._buttons

    @property
    def _pos_x(self):
        return self.SPACE + (BTN_SIZE[0] + self.SPACE) * len(self._buttons)

    @property
    def _pos_y(self):
        return WIDTH + self.SPACE

    def add_button(self, name, text):
        self._buttons[name] = Button(text, (self._pos_x, self._pos_y))

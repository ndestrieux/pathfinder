import pygame

from utils.properties import BTN_SIZE, COLORS


class Button:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.size = BTN_SIZE
        self._bg = COLORS["GREY"]
        self._active = False

    @property
    def active(self):
        return self._active

    @property
    def rect(self):
        return self.pos + self.size

    @active.setter
    def active(self, status):
        if status:
            self._bg = COLORS["GREEN"]
        else:
            self._bg = COLORS["GREY"]
        self._active = status

    def show(self, win):
        pygame.draw.rect(win, self._bg, self.rect)
        text_surf, text_rect = self._text_object()
        text_rect.center = self._btn_center()
        win.blit(text_surf, text_rect)

    def _text_object(self):
        font = pygame.font.Font("freesansbold.ttf", 20)
        text_surface = font.render(self.text, True, COLORS["BLACK"])
        return text_surface, text_surface.get_rect()

    def _btn_center(self):
        return self.pos[0] + (120 / 2), self.pos[1] + (50 / 2)

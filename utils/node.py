import pygame

from utils.properties import COLORS


class Node:
    def __init__(self, position, width, *, parent=None):
        self.parent = parent
        self.position = position
        self.width = width
        self.color = COLORS["WHITE"]
        self.g = 0
        self.h = 0
        self.f = 0

    @property
    def x(self):
        return self.position[0] * self.width

    @property
    def y(self):
        return self.position[1] * self.width

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x - 1, self.y - 1, self.width - 1, self.width - 1)
        )

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return f"Node, position: {self.position}"

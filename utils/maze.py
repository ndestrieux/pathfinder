import pygame

from utils.node import Node
from utils.properties import COLORS


class Maze:
    def __init__(self, width, rows):
        self.width = width
        self.rows = rows
        self._grid = []

    @property
    def grid(self):
        return self._grid

    @property
    def gap(self):
        return self.width // self.rows

    def create_grid(self):
        for i in range(self.rows):
            self._grid.append([])
            for j in range(self.rows):
                node = Node((i, j), self.gap)
                self._grid[i].append(node)

    def _draw_grid(self, win):
        for row in self.grid:
            for node in row:
                node.draw(win)

    def draw(self, win):
        win.fill(COLORS["GREY"], (0, 0, win.get_width(), win.get_width()))
        self._draw_grid(win)
        pygame.display.update()

    def _get_click_position(self, m):
        y, x = m
        row = y // self.gap
        col = x // self.gap
        return row, col

    def get_selected_node(self, m):
        row, col = self._get_click_position(m)
        return self.grid[row][col]

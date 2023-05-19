import pygame

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
                self._grid[i].append(0)

    def draw_grid(self, win):
        for i in range(self.rows):
            pygame.draw.line(win, COLORS["GREY"], (0, i * self.gap), (self.width, i * self.gap))
            for j in range(self.rows):
                pygame.draw.line(win, COLORS["GREY"], (j * self.gap, 0), (j * self.gap, self.width))

    def draw(self, win):
        win.fill(COLORS["WHITE"])
        gap = self.width // self.rows
        for x, row in enumerate(self.grid):
            for y in range(len(row)):
                pygame.draw.rect(win, COLORS["WHITE"], (x, y, gap, gap))
        self.draw_grid(win)
        pygame.display.update()


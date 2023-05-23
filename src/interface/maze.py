from src.pathfinder.node import Node
from src.properties.interface import COLORS


class Maze:
    def __init__(self, width, rows, pathfinder):
        self.width = width
        self.rows = rows
        self._grid = []
        self._pathfinder = pathfinder

    @property
    def grid(self):
        return self._grid

    @property
    def pathfinder(self):
        return self._pathfinder

    @property
    def gap(self):
        return self.width // self.rows

    def create_grid(self):
        for i in range(self.rows):
            self._grid.append([])
            for j in range(self.rows):
                node = Node((i, j), self)
                self._grid[i].append(node)

    def _draw_grid(self, win):
        for row in self.grid:
            for node in row:
                node.draw(win)

    def draw(self, win):
        win.fill(COLORS["GREY"], (0, 0, win.get_width(), win.get_width()))
        self._draw_grid(win)

    def _get_click_position(self, m):
        y, x = m
        row = y // self.gap
        col = x // self.gap
        return row, col

    def get_selected_node(self, m):
        row, col = self._get_click_position(m)
        return self.grid[row][col]

import pygame

from src.pathfinder.node_neighbors import NodeNeighbors
from src.properties.node import NODE_COLORS


class Node:
    TYPE_DICT = {
        "start": NODE_COLORS["GREEN"],
        "end": NODE_COLORS["RED"],
        "wall": NODE_COLORS["BLACK"],
    }

    def __init__(self, position, maze, *, parent=None):
        self.parent = parent
        self.position = position
        self.width = maze.gap
        self.color = NODE_COLORS["WHITE"]
        self.wall = False
        self.neighbors = NodeNeighbors(self, maze)
        self.g = 0
        self.h = 0
        self.f = 0

    @property
    def x(self):
        return self.position[0] * self.width

    @property
    def y(self):
        return self.position[1] * self.width

    def action(self):
        return {
            "start": self.make_start,
            "end": self.make_end,
            "wall": self.make_wall,
        }

    def make_start(self, pathfinder):
        pathfinder.start_node = self

    def make_end(self, pathfinder):
        pathfinder.end_node = self

    def make_wall(self, *args):
        self.color = NODE_COLORS["BLACK"]
        self.wall = True

    def remove_wall(self):
        if self.wall:
            self.color = NODE_COLORS["WHITE"]
            self.wall = False

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x - 1, self.y - 1, self.width - 1, self.width - 1)
        )

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return f"Node, position: {self.position}"

import pygame

from src.interface.maze import Maze
from src.interface.menu import Menu
from src.pathfinder.pathfinder import AStar
from src.properties.interface import (COLORS, MENU_BTNS, MENU_POS, MENU_SIZE,
                                      ROWS, WIDTH)


class Game:
    def __init__(self):
        self._maze = self._create_maze()
        self._menus = self._build_menus()

    @property
    def maze(self):
        return self._maze

    @property
    def current_menu(self):
        return self._menus[0]

    @staticmethod
    def _create_maze():
        pathfinder = AStar()
        new_maze = Maze(WIDTH, ROWS, pathfinder)
        new_maze.create_grid()
        return new_maze

    @staticmethod
    def _build_menus():
        menu_list = []
        for k, buttons in MENU_BTNS:
            menu = Menu()
            for name, text in buttons:
                menu.add_button(name, text)
            menu_list.append(menu)
        return menu_list

    def click_button(self, mouse):
        for btn in self.current_menu.buttons.values():
            if btn == self.current_menu.buttons.get("find", False) and not (
                self._maze.pathfinder.start_node and self._maze.pathfinder.end_node
            ):
                continue
            if (
                btn.pos[0] < mouse[0] < btn.pos[0] + btn.size[0]
                and btn.pos[1] < mouse[1] < btn.pos[1] + btn.size[1]
            ):
                btn.active = not btn.active
            else:
                btn.active = False

    def next_menu(self, win):
        self._menus.pop(0)
        pygame.draw.rect(win, COLORS["BLACK"], MENU_POS + MENU_SIZE)

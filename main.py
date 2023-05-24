from typing import Dict, Tuple

import pygame

from src.interface.button import Button
from src.interface.maze import Maze
from src.interface.menu import Menu
from src.pathfinder.node import Node
from src.pathfinder.pathfinder import AStar
from src.properties.interface import LENGTH, MAIN_BUTTONS, ROWS, WIDTH


def click_button(m: Tuple[int, int], buttons: Dict[str, Button]) -> None:
    for btn in buttons.values():
        if (
            btn.pos[0] < m[0] < btn.pos[0] + btn.size[0]
            and btn.pos[1] < m[1] < btn.pos[1] + btn.size[1]
        ):
            btn.active = not btn.active
        else:
            btn.active = False


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, LENGTH))
    clock = pygame.time.Clock()
    running = True

    pathfinder = AStar()
    maze = Maze(WIDTH, ROWS, pathfinder)
    maze.create_grid()

    main_menu = Menu()
    for name, text in MAIN_BUTTONS:
        main_menu.add_button(name, text)

    while running:
        mouse = pygame.mouse.get_pos()
        if main_menu.buttons["find"].active:
            pathfinder.find_path()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 0 < mouse[0] < WIDTH < mouse[1] < LENGTH:
                    click_button(mouse, main_menu.buttons)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if set(mouse) < set(range(WIDTH)):
                    for node_type in Node.TYPE_DICT.keys():
                        if main_menu.buttons[node_type].active:
                            node = maze.get_selected_node(mouse)
                            node.action()[node_type](pathfinder)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if set(mouse) < set(range(WIDTH)):
                    node = maze.get_selected_node(mouse)
                    node.remove_wall()

        maze.draw(screen)
        for button in main_menu.buttons.values():
            button.show(screen)

        pygame.display.update()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

from typing import Tuple

import pygame

from src.interface.maze import Maze
from src.interface.menu import Menu
from src.pathfinder.node import Node
from src.pathfinder.pathfinder import AStar
from src.properties.interface import (COLORS, END_BUTTONS, LENGTH,
                                      MAIN_BUTTONS, MENU_POS, MENU_SIZE, ROWS,
                                      WIDTH)


def reset_menu() -> None:
    pygame.draw.rect(screen, COLORS["BLACK"], MENU_POS + MENU_SIZE)


def click_button(m: Tuple[int, int], menu: Menu, pathfinder: AStar = None) -> None:
    for btn in menu.buttons.values():
        if btn == menu.buttons.get("find", False) and not (
            pathfinder.start_node and pathfinder.end_node
        ):
            continue
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

    end_menu = Menu()
    for name, text in END_BUTTONS:
        end_menu.add_button(name, text)

    while running:
        mouse = pygame.mouse.get_pos()
        maze.draw(screen)
        if (
            main_menu.buttons["find"].active
            and pathfinder.start_node
            and pathfinder.end_node
        ):
            pathfinder.find_path()
            main_menu.buttons["find"].active = False
            reset_menu()

        if end_menu.buttons["reset"].active:
            end_menu.buttons["reset"].active = False
            pathfinder = AStar()
            maze = Maze(WIDTH, ROWS, pathfinder)
            maze.create_grid()
            reset_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pathfinder.completed:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if 0 < mouse[0] < WIDTH < mouse[1] < LENGTH:
                        click_button(mouse, end_menu)

            else:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if 0 < mouse[0] < WIDTH < mouse[1] < LENGTH:
                        click_button(mouse, main_menu, pathfinder)

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

        if pathfinder.completed:
            for button in end_menu.buttons.values():
                button.show(screen)
        else:
            for button in main_menu.buttons.values():
                button.show(screen)

        pygame.display.update()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

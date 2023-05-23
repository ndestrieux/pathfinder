from typing import Dict, Tuple

import pygame

from src.interface.button import Button
from src.interface.maze import Maze
from src.pathfinder.node import Node
from src.pathfinder.pathfinder import AStar
from src.properties.interface import BTN_SIZE, LENGTH, ROWS, WIDTH

# from src.properties.node import NODE_TYPE_DICT


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

    BTN_DICT = {
        "start": Button("Start node", (20, WIDTH + 20)),
        "end": Button("End node", (20 + BTN_SIZE[0] + 20, WIDTH + 20)),
        "wall": Button("Build wall", (20 + (BTN_SIZE[0] + 20) * 2, WIDTH + 20)),
        "find": Button("Find path", (20 + (BTN_SIZE[0] + 20) * 3, WIDTH + 20)),
    }

    while running:
        mouse = pygame.mouse.get_pos()
        if BTN_DICT["find"].active:
            pathfinder.find_path()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 0 < mouse[0] < WIDTH < mouse[1] < LENGTH:
                    click_button(mouse, BTN_DICT)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if set(mouse) < set(range(WIDTH)):
                    for node_type in Node.TYPE_DICT.keys():
                        if BTN_DICT[node_type].active:
                            node = maze.get_selected_node(mouse)
                            node.action()[node_type](pathfinder)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if set(mouse) < set(range(WIDTH)):
                    node = maze.get_selected_node(mouse)
                    node.remove_wall()

        maze.draw(screen)
        for button in BTN_DICT.values():
            button.show(screen)

        pygame.display.update()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

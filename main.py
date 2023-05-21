from typing import Dict, Tuple

import pygame

from utils.button import Button
from utils.maze import Maze
from utils.pathfinder import AStar
from utils.properties import BTN_SIZE, LENGTH, NODE_TYPE_DICT, ROWS, WIDTH


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

    maze = Maze(WIDTH, ROWS)
    maze.create_grid()
    pathfinder = AStar(maze)

    BTN_DICT = {
        "start": Button("Start node", (20, WIDTH + 20)),
        "end": Button("End node", (20 + BTN_SIZE[0] + 20, WIDTH + 20)),
        "wall": Button("Build wall", (20 + (BTN_SIZE[0] + 20) * 2, WIDTH + 20)),
        "find": Button("Find path", (20 + (BTN_SIZE[0] + 20) * 3, WIDTH + 20)),
    }

    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 0 < mouse[0] < WIDTH < mouse[1] < LENGTH:
                    click_button(mouse, BTN_DICT)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if set(mouse) < set(range(WIDTH)):
                    for node_type in NODE_TYPE_DICT.keys():
                        if BTN_DICT[node_type].active:
                            row, col = maze.get_click_position(mouse)
                            node = maze.grid[row][col]
                            node.action()[node_type](pathfinder)

        maze.draw(screen)
        for button in BTN_DICT.values():
            button.show(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

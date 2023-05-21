from typing import Dict, Tuple

import pygame

from utils.button import Button
from utils.maze import Maze
from utils.properties import BTN_SIZE, LENGTH, ROWS, WIDTH


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
    button_dict = {
        "btn_start": Button("Start node", (20, WIDTH + 20)),
        "btn_end": Button("End node", (20 + BTN_SIZE[0] + 20, WIDTH + 20)),
        "btn_wall": Button("Build wall", (20 + (BTN_SIZE[0] + 20) * 2, WIDTH + 20)),
        "btn_find": Button("Find path", (20 + (BTN_SIZE[0] + 20) * 3, WIDTH + 20)),
    }

    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 0 < mouse[0] < WIDTH < mouse[1] < LENGTH:
                    click_button(mouse, button_dict)

        maze.draw(screen)
        for button in button_dict.values():
            button.show(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

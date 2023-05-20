import pygame

from utils.button import Button
from utils.maze import Maze
from utils.properties import LENGTH, ROWS, WIDTH, BTN_SIZE

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, LENGTH))
    clock = pygame.time.Clock()
    running = True

    maze = Maze(WIDTH, ROWS)
    maze.create_grid()
    btn_start = Button("Start node", (20, WIDTH + 20))
    btn_end = Button("End node", (20 + BTN_SIZE[0] + 20, WIDTH + 20))
    btn_wall = Button("Build wall", (20 + (BTN_SIZE[0] + 20) * 2, WIDTH + 20))
    btn_find = Button("Find path", (20 + (BTN_SIZE[0] + 20) * 3, WIDTH + 20))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        maze.draw(screen)
        btn_start.show(screen)
        btn_end.show(screen)
        btn_wall.show(screen)
        btn_find.show(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

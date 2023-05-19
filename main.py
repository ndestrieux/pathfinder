import pygame

from utils.maze import Maze
from utils.properties import WIDTH, LENGTH, ROWS


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, LENGTH))
    clock = pygame.time.Clock()
    running = True

    maze = Maze(WIDTH, ROWS)
    maze.create_grid()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        maze.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

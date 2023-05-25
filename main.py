import pygame

from src.game.game import Game
from src.pathfinder.node import Node
from src.properties.interface import LENGTH, WIDTH

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, LENGTH))
    clock = pygame.time.Clock()
    running = True

    game = Game()

    while running:
        mouse = pygame.mouse.get_pos()
        game.maze.draw(screen)
        if (
            "find" in game.current_menu.buttons.keys()
            and game.current_menu.buttons["find"].active
            and game.maze.pathfinder.start_node
            and game.maze.pathfinder.end_node
        ):
            game.maze.pathfinder.find_path()
            game.current_menu.buttons["find"].active = False
            game.next_menu(screen)

        if (
            "reset" in game.current_menu.buttons.keys()
            and game.current_menu.buttons["reset"].active
        ):
            game.current_menu.buttons["reset"].active = False
            game = Game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game.maze.pathfinder.completed:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if 0 < mouse[0] < WIDTH < mouse[1] < LENGTH:
                        game.click_button(mouse)

            else:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if 0 < mouse[0] < WIDTH < mouse[1] < LENGTH:
                        game.click_button(mouse)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if set(mouse) < set(range(WIDTH)):
                        for node_type in Node.TYPE_DICT.keys():
                            if game.current_menu.buttons[node_type].active:
                                node = game.maze.get_selected_node(mouse)
                                node.action()[node_type](game.maze.pathfinder)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if set(mouse) < set(range(WIDTH)):
                        node = game.maze.get_selected_node(mouse)
                        node.remove_wall()

        for button in game.current_menu.buttons.values():
            button.show(screen)

        pygame.display.update()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

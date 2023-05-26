import pygame

from src.game.game import Game
from src.pathfinder.node import Node
from src.properties.interface import LENGTH, WIDTH


def start_new_game():
    new_game = Game()
    new_maze = new_game.maze
    new_pathfinder = new_game.maze.pathfinder
    return new_game, new_maze, new_pathfinder


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, LENGTH))
    clock = pygame.time.Clock()
    running = True

    game, maze, pathfinder = start_new_game()

    while running:
        mouse = pygame.mouse.get_pos()
        maze.draw(screen)
        if (
            "find" in game.current_menu.buttons.keys()
            and game.current_menu.buttons["find"].active
            and pathfinder.start_node
            and pathfinder.end_node
        ):
            pathfinder.find_path()
            game.current_menu.buttons["find"].active = False
            game.next_menu(screen)

        if (
            "reset" in game.current_menu.buttons.keys()
            and game.current_menu.buttons["reset"].active
        ):
            game.current_menu.buttons["reset"].active = False
            game, maze, pathfinder = start_new_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 0 < mouse[0] < WIDTH < mouse[1] < LENGTH:
                    game.click_button(mouse)

            if not pathfinder.completed:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if set(mouse) < set(range(WIDTH)):
                        for node_type in Node.TYPE_DICT.keys():
                            if game.current_menu.buttons[node_type].active:
                                node = maze.get_selected_node(mouse)
                                node.action()[node_type](pathfinder)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if set(mouse) < set(range(WIDTH)):
                        node = maze.get_selected_node(mouse)
                        node.remove_wall()

        if pathfinder.completed and not pathfinder.path.path:
            game.display_message(screen, "No path found")

        for button in game.current_menu.buttons.values():
            button.show(screen)

        pygame.display.update()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

from src.properties.interface import ROWS


class NodeNeighbors:
    ADJACENT_NODE_POSITIONS = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, -1),
        (-1, 1),
    )

    def __init__(self, node, maze):
        self.node = node
        self._neighbors = []
        self._maze = maze

    @property
    def neighbors(self):
        return self._neighbors

    @property
    def maze(self):
        return self._maze

    @staticmethod
    def _position_in_range(pos):
        return (0 <= pos[0] <= ROWS - 1) and (0 <= pos[1] <= ROWS - 1)

    def _position_in_closed_list(self, position):
        for node in self.maze.pathfinder.closed_list:
            if node.position == position:
                return True
        return False

    def find_neighbors(self):
        for col, row in self.ADJACENT_NODE_POSITIONS:
            new_pos = (
                self.node.position[0] + col,
                self.node.position[1] + row,
            )
            if (
                self._position_in_range(new_pos)
                and not self.maze.grid[new_pos[0]][new_pos[1]].wall
                and not self._position_in_closed_list(new_pos)
            ):
                self._neighbors.append(self.maze.grid[new_pos[0]][new_pos[1]])

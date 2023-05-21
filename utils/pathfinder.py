from utils.properties import NODE_COLORS


class AStar:
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

    def __init__(self, maze):
        self.maze = maze
        self._start_node = None
        self._end_node = None
        self._current_node = None
        self._open_list = []
        self._closed_list = []

    @property
    def start_node(self):
        return self._start_node

    @property
    def end_node(self):
        return self._end_node

    @start_node.setter
    def start_node(self, new_node):
        if self._start_node:
            self._start_node.color = NODE_COLORS["WHITE"]
        new_node.color = NODE_COLORS["GREEN"]
        self._start_node = new_node

    @end_node.setter
    def end_node(self, new_node):
        if self._end_node:
            self._end_node.color = NODE_COLORS["WHITE"]
        new_node.color = NODE_COLORS["RED"]
        self._end_node = new_node

    def _position_in_range(self, pos):
        return (0 <= pos[0] <= len(self.maze.grid) - 1) and (
            0 <= pos[1] <= len(self.maze.grid[0]) - 1
        )

    def _position_in_closed_list(self, position):
        for node in self._closed_list:
            if node.position == position:
                return True
        return False

    def _find_neighbors(self):
        neighbors = []
        for col, row in self.ADJACENT_NODE_POSITIONS:
            new_pos = (
                self._current_node.position[0] + col,
                self._current_node.position[1] + row,
            )
            if (
                self._position_in_range(new_pos)
                and not self.maze.grid[new_pos[0]][new_pos[1]].wall
                and not self._position_in_closed_list(new_pos)
            ):
                neighbors.append(self.maze.grid[new_pos[0]][new_pos[1]])
        return neighbors

    def _calculate_heuristic(self, node):
        return ((node.position[0] - self.end_node.position[0]) ** 2) + (
            (node.position[1] - self.end_node.position[1]) ** 2
        )

    def _build_path(self):
        path = []
        current = self._current_node
        while current:
            if current not in (self.start_node, self.end_node):
                current.color = NODE_COLORS["PURPLE"]
            path.append(current.position)
            current = current.parent
        return path[::-1]

    def find_path(self):
        self._open_list.append(self.start_node)

        while self._open_list:
            self._current_node = self._open_list[0]
            current_index = 0
            for index, item in enumerate(self._open_list):
                if item.f < self._current_node.f:
                    self._current_node = item
                    current_index = index

            if self._current_node == self.end_node:
                return self._build_path()

            self._open_list.pop(current_index)
            self._closed_list.append(self._current_node)

            children = self._find_neighbors()
            temp_g_score = self._current_node.g + 1
            for child in children:
                if child not in self._open_list:
                    self._open_list.append(child)
                    child.parent = self._current_node
                    child.g = temp_g_score
                    child.h = self._calculate_heuristic(child)
                    child.f = child.g + child.h
                else:
                    if temp_g_score < child.g:
                        child.parent = self._current_node
                        child.g = temp_g_score
                        child.f = child.g + child.h

        return "No path found"

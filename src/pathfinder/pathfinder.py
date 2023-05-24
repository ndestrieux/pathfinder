from src.pathfinder.path import Path
from src.properties.node import NODE_COLORS


class AStar:
    def __init__(self):
        self._start_node = None
        self._end_node = None
        self._current_node = None
        self._open_list = []
        self._closed_list = []
        self._completed = False
        self.path = Path(self)

    @property
    def start_node(self):
        return self._start_node

    @property
    def end_node(self):
        return self._end_node

    @property
    def current_node(self):
        return self._current_node

    @property
    def closed_list(self):
        return self._closed_list

    @property
    def completed(self):
        return self._completed

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

    def _get_neighbors(self):
        self._current_node.neighbors.find_neighbors()
        return self._current_node.neighbors.neighbors

    def _calculate_heuristic(self, node):
        return ((node.position[0] - self.end_node.position[0]) ** 2) + (
            (node.position[1] - self.end_node.position[1]) ** 2
        )

    def _get_path(self):
        self.path.build_path()
        return self.path.path

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
                self._completed = True
                return self._get_path()

            self._open_list.pop(current_index)
            self._closed_list.append(self._current_node)

            children = self._get_neighbors()
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
        self._completed = True

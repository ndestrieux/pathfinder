from src.properties.node import NODE_COLORS


class Path:
    def __init__(self, pathfinder):
        self._path = []
        self.pathfinder = pathfinder

    @property
    def path(self):
        return self._path

    def build_path(self):
        current = self.pathfinder.end_node
        while current:
            if current not in (self.pathfinder.start_node, self.pathfinder.end_node):
                current.color = NODE_COLORS["PURPLE"]
            self._path.append(current.position)
            current = current.parent

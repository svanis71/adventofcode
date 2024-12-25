class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position: tuple[int, int] | None = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

from warnings import warn

from pathfinding import get_adjacent_squares
from .node import Node


def return_path(current_node: Node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(maze: list[list[str]], start: tuple[int, int], end: tuple[int, int], allow_diagonal_movement: bool = False):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """

    # Create start and end node
    start_node: Node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node: Node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list: list[Node] = []
    closed_list: list[Node] = []
    open_list.append(start_node)

    # what squares do we search
    adjacent_squares = get_adjacent_squares(allow_diagonal_movement)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate neighbours
        neighbours: list[Node] = []

        for new_position in adjacent_squares:  # Adjacent squares

            # Get node position
            node_position: tuple[int, int] = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] - maze[current_node.position[0]][current_node.position[1]] > 1:
                continue

            # Create new node
            new_node: Node = Node(current_node, node_position)

            # Append
            neighbours.append(new_node)

        # Loop through neighbours
        for neighbour in neighbours:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == neighbour]) > 0:
                continue

            # Create the f, g, and h values
            neighbour.g = current_node.g + 1
            # neighbour.h = ((neighbour.position[0] - end_node.position[0]) ** 2) + (
            #         (neighbour.position[1] - end_node.position[1]) ** 2)
            neighbour.h = abs(neighbour.position[0] - end_node.position[0]) + abs(
                neighbour.position[1] - end_node.position[1])
            neighbour.f = neighbour.g + neighbour.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if
                    neighbour.position == open_node.position and neighbour.g > open_node.g]) > 0:
                continue

            # Add the neighbour to the open list
            open_list.append(neighbour)

    warn("Couldn't get a path to destination")
    return None


def output_maze(maze, path):
    for step in path:
        maze[step[0]][step[1]] = 2
    for row in maze:
        line = []
        for col in row:
            if col == 1:
                line.append("X")
            elif col == 0:
                line.append(".")
            elif col == 2:
                line.append("o")
        print("".join(line))

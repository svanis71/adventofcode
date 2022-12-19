from __future__ import annotations

import heapq
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

from indata import read_list_of_strings


@dataclass
class Graph:
    _graph: list[list[int]]
    start: tuple[int, int]
    end: tuple[int, int]
    distance_to: defaultdict[tuple[int, int], int] = field(default_factory=lambda: defaultdict(int))

    def __post_init__(self):
        self.distance_to[self.start] = 0
        self._rows = len(self._graph)
        self._cols = len(self._graph[0])

    def get(self):
        return self._graph

    def get_neighbours(self, current: tuple[int, int]) -> list[tuple[int, int]]:
        cur_y, cur_x = current
        nrows, ncols = self._rows, self._cols

        max_next = self._graph[cur_y][cur_x] + 1
        possible_neighbours = [
            (cur_y + 1, cur_x),
            (cur_y - 1, cur_x),
            (cur_y, cur_x + 1),
            (cur_y, cur_x - 1),
        ]
        return [t for t in possible_neighbours if
                0 <= t[0] < nrows and 0 <= t[1] < ncols and max_next >= self._graph[t[0]][t[1]]]

    def heuristic(self, current: tuple[int, int]) -> int:
        cur_y, cur_x = current
        end_y, end_x = self.end
        return abs(cur_y - end_y) + abs(cur_x - end_x)


def astar_search(graph: Graph, start: Optional[tuple[int, int]] = None) -> int:
    start = graph.start if start is None else start
    frontier_nodes = [(graph.distance_to[start], start)]

    while frontier_nodes:
        _, current = heapq.heappop(frontier_nodes)
        if current == graph.end:
            break
        for neighbour in graph.get_neighbours(current):
            new_cost = graph.distance_to[current] + 1
            if neighbour not in graph.distance_to or new_cost < graph.distance_to[neighbour]:
                graph.distance_to[neighbour] = new_cost
                priority = new_cost + graph.heuristic(neighbour)
                heapq.heappush(frontier_nodes, (priority, neighbour))

    shortest_path_len = graph.distance_to[graph.end]
    graph.distance_to.clear()

    return shortest_path_len


def create_graph() -> Graph:
    lines: list[list[int]] = []
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (0, 0)

    for y, row in enumerate(read_list_of_strings('day12')):
        line = []
        for x, letter in enumerate(row):
            if letter == "S":
                start, letter = (y, x), "a"
            if letter == "E":
                end, letter = (y, x), "z"
            value = ord(letter) - ord("a")
            line.append(value)
        lines.append(line)
    return Graph(lines, start, end)


def part1():
    return astar_search(create_graph())


def part2():
    graph = create_graph()
    graph_nodes = graph.get()
    starts: list[tuple[int, int]] = []

    for y, row in enumerate(graph_nodes):
        for x, _ in enumerate(row):
            is_a = graph_nodes[y][x] == 0
            has_b_neighbour = any(graph_nodes[m][n] == 1 for m, n in graph.get_neighbours((y, x)))
            if is_a and has_b_neighbour:
                starts.append((y, x))
    return min(astar_search(graph, start) for start in starts)


def run():
    print(f'Day 12 pt1: {part1()}')
    print(f'Day 12 pt2: {part2()}')

# Day 12 pt1: 437
# Day 12 pt2: 430

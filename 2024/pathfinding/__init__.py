def inbound(matrix, nxt_y, nxt_x) -> bool:
    return 0 <= nxt_y < len(matrix) and 0 <= nxt_x < len(matrix[0])


def get_adjacent_squares(allow_diagonal: bool = False) -> tuple:
    return ((0, -1), (0, 1), (-1, 0), (1, 0),) if not allow_diagonal \
        else ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)


def get_neighbors(matrix, pos: tuple[int, int]) -> list[tuple[int, int]]:
    y, x = pos[0], pos[1]
    return [(y + offset[0], x + offset[1]) for offset in get_adjacent_squares()
            if inbound(matrix, offset[0] + y, offset[1] + x)]

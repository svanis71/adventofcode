from indata import read_lines


def part1():
    seatmap = [list(y) for y in read_lines('day11')]
    occupied, adjacents = 0, [(0, -1), (-1, 0), (-1, -1), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    change_count, seatmap_copy = 0, [['.' for seat in row] for row in seatmap]
    while True:
        for y, row in enumerate(seatmap):
            for x, seat in enumerate(row):
                if seat == '.':
                    continue
                seat_empty, free_neighbours, occupied_neighbours = seatmap[y][x] == 'L', 0, 0
                for y_offset, x_offset in adjacents:
                    cy, cx = y+y_offset, x+x_offset
                    if 0 <= cx < len(row) and 0 <= cy < len(seatmap):
                        if seatmap[cy][cx] == 'L':
                            free_neighbours += 1
                        elif seatmap[cy][cx] == '#':
                            occupied_neighbours += 1
                if seat_empty and occupied_neighbours == 0 and seatmap_copy[y][x] != '#':
                    seatmap_copy[y][x] = '#'
                    change_count += 1
                elif occupied_neighbours >= 4 and seatmap_copy[y][x] != 'L':
                    seatmap_copy[y][x] = 'L'
                    change_count += 1
        seatmap = [[seat for seat in row] for row in seatmap_copy]
        if change_count == 0:
            break
        change_count = 0
    return sum([x.count('#') for x in seatmap])


def part2():
    seatmap = [list(y) for y in read_lines('day11')]
    occupied, directions = 0, [(0, -1), (-1, 0), (-1, -1), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    change_count, seatmap_copy = 0, [['.' for seat in row] for row in seatmap]
    while True:
        for y, row in enumerate(seatmap):
            for x, seat in enumerate(row):
                if seat == '.':
                    continue
                seat_empty, free_neighbours, occupied_neighbours = seatmap[y][x] == 'L', 0, 0
                for y_offset, x_offset in directions:
                    cy, cx = y+y_offset, x+x_offset
                    while 0 <= cx < len(row) and 0 <= cy < len(seatmap):
                        if seatmap[cy][cx] == 'L':
                            free_neighbours += 1
                            break
                        elif seatmap[cy][cx] == '#':
                            occupied_neighbours += 1
                            break
                        cx += x_offset
                        cy += y_offset

                if seat_empty and occupied_neighbours == 0 and seatmap_copy[y][x] != '#':
                    seatmap_copy[y][x] = '#'
                    change_count += 1
                elif occupied_neighbours >= 5 and seatmap_copy[y][x] != 'L':
                    seatmap_copy[y][x] = 'L'
                    change_count += 1
        seatmap = [[seat for seat in row] for row in seatmap_copy]
        if change_count == 0:
            break
        change_count = 0
    return sum([x.count('#') for x in seatmap])


def run():
    print(f'Day 11 part 1: {part1()}')
    print(f'Day 11 part 2: {part2()}')

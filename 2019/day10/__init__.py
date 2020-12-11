def count_asteroids(y, x, location_matrix):
    pass


def day10(asteroids_map):
    location_matrix = [[c for c in x] for x in asteroids_map.splitlines()]

    for y, zz in enumerate(location_matrix):
        asteriods = [(ix, y) for ix, candidate in enumerate(zz) if candidate == '#']
        for x, qq in enumerate(zz):
            if qq == '#':
                location_matrix[y, x] = count_asteroids(y, x, location_matrix)

from indata import read_list_of_strings


def calc_algo_value(rn: int, cn: int, image_data: list, pad_bit: int):
    neighbours = (  # (x, y) offset
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (0, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1),)
    algorithm_pos = 0
    for bit, (ox, oy) in enumerate(neighbours):
        bitval = pad_bit
        if 0 <= rn + oy < len(image_data) and 0 <= cn + ox < len(image_data[0]):
            bitval = image_data[rn + oy][cn + ox]
        algorithm_pos = algorithm_pos + (bitval << (8 - bit))
    return algorithm_pos


def enhance(algorithm: list, image_data: list, pad_bit: int):
    shadow = []
    for rn, row in enumerate(image_data):
        nr = []
        for cn, _ in enumerate(row):
            algorithm_pos = calc_algo_value(rn, cn, image_data, pad_bit)
            nr.append(algorithm[algorithm_pos])
        shadow.append(nr)
    return shadow


def solve(lines: list, reps: int):
    enhancement_algorithm = [1 if c == '#' else 0 for c in lines.pop(0)]
    image_data = [[1 if c == '#' else 0 for c in row] for row in lines]
    pad_bit = 0
    for i in range(reps):
        image_data = [[pad_bit] + [c for c in row] + [pad_bit] for row in image_data]
        new_row = [pad_bit] * len(image_data[0])
        image_data = [new_row] + image_data + [new_row]
        image_data = enhance(enhancement_algorithm, image_data, pad_bit)
        if enhancement_algorithm[0] - enhancement_algorithm[-1] == 1:
            pad_bit = pad_bit ^ 1
    return image_data, sum([bit for row in image_data for bit in row])


def part1(indata, reps):
    _, light_bits = solve(indata.copy(), reps)
    return light_bits


def part2(indata, reps):
    _, light_bits = solve(indata.copy(), reps)
    return light_bits


def run():
    indata = read_list_of_strings('day20')
    indata.pop(1)
    print(f'Day 20 pt1: {part1(indata, 2)}')
    print(f'Day 20 pt2: {part2(indata, 50)}')

# Day 20 pt1: 5057
# Day 20 pt2: 18502

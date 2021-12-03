from indata import read_list_of_strings

def get_pivot(numbers):
    pivot = []
    for line in numbers:
        for bit, bitval in enumerate(line):
            if(len(pivot) < bit + 1):
                pivot.append(bitval)
            else:
                pivot[bit] += bitval
    return pivot

def calc_oxygen_generator_rate(bit, numbers):
    if len(numbers) == 1:
        return numbers[0]
    pivot = get_pivot(numbers)
    most_common = '1' if pivot[bit].count('1') >= pivot[bit].count('0') else '0'
    return calc_oxygen_generator_rate(bit + 1, [n for n in numbers if n[bit] == most_common])

def calc_co2_scrubber_rate(bit, numbers):
    if len(numbers) == 1:
        return numbers[0]
    pivot = get_pivot(numbers)
    least_common = '1' if pivot[bit].count('1') < pivot[bit].count('0') else '0'
    return calc_co2_scrubber_rate(bit + 1, [n for n in numbers if n[bit] == least_common])

def part1():
    report = read_list_of_strings('day3')
    pivot = get_pivot(report)
    gamma_rate = ''.join(['1' if s.count('1') > s.count('0') else '0' for s in pivot])
    epsilon_rate = ''.join(['1' if c == '0' else '0' for c in gamma_rate])
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2():
    report = read_list_of_strings('day3')
    oxygen_generator_rate = calc_oxygen_generator_rate(0, report)
    co2_scrubber_rate = calc_co2_scrubber_rate(0, report)
    return int(oxygen_generator_rate, 2) * int(co2_scrubber_rate, 2)


def run():
    print(f'Day 3 pt1: {part1()}')
    print(f'Day 3 pt2: {part2()}')


# part 1: 1025636
# part 2: 793873
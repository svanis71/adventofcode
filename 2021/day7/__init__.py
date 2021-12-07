from indata import read_csv_integers


def part1():
    crab_positions = read_csv_integers('day7')
    low_crab, high_crab = min(crab_positions), max(crab_positions)
    fuel_consumption_list = []
    for align_pos in range(low_crab, high_crab + 1):
        fuel_consumption = sum(abs(x - align_pos) for x in crab_positions)
        fuel_consumption_list.append((align_pos, fuel_consumption))
    return min(fuel_consumption_list, key=lambda t : t[1])
        
def part2():
    crab_positions = read_csv_integers('day7')
    low_crab, high_crab = min(crab_positions), max(crab_positions)
    prev_consumption = sum(int(abs(low_crab - x) * (abs(low_crab - x) + 1) / 2) for x in crab_positions)
    for align_pos in range(low_crab + 1, high_crab + 1):
        for x in crab_positions:
            fuel_consumption = sum(int(abs(align_pos - x) * (abs(align_pos - x) + 1) / 2) for x in crab_positions)
            if fuel_consumption > prev_consumption:
                return prev_consumption
            prev_consumption = fuel_consumption

def run():
    print(f'Day 7 pt1: {part1()}')
    print(f'Day 7 pt2: {part2()}')


# Day 7 pt1: (331, 349769)
# Day 7 pt2: 99540554
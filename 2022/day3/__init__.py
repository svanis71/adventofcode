from indata import read_list_of_strings


def get_priority(c: str) -> int:
    base_prio: int = 1 if c.islower() else 27
    return base_prio + ord(c) - ord('A' if c.isupper() else 'a')


def part1(items_list: list) -> int:
    priorities: list[int] = []
    for items in items_list:
        half = len(items) // 2
        compartment1, compartment2 = items[0:half], items[half:]
        for c in compartment1:
            if c in compartment2:
                priorities.append(get_priority(c))
                break
    return sum(priorities)


def part2(items: list) -> int:
    priorities: list[int] = []
    for group_idx in range(0, len(items), 3):
        rucksacks: list[str] = items[group_idx:group_idx + 3]
        for c in rucksacks[0]:
            if c in rucksacks[1] and c in rucksacks[2]:
                priorities.append(get_priority(c))
                break
    return sum(priorities)


def run():
    items = read_list_of_strings('day3')
    print(f'Day 3 pt1: {part1(items)}')
    print(f'Day 3 pt2: {part2(items)}')

# Day 3 pt1: 7742
# Day 3 pt2: 2276

import math

from indata import read_infile


class Monkey:
    def __init__(self, items: str, operation: str, divby: str, throw_true: str, throw_false: str):
        self.items = [int(i) for i in items.split(':')[-1].split(',')]
        self.op: str = operation.split('=')[-1].strip()
        self.divby: int = int(divby.split(' ')[-1])
        self.throw_true: int = int(throw_true[-1])
        self.throw_false: int = int(throw_false[-1])
        self.inspections: int = 0

    def evaluate(self, item_idx: int) -> int:
        n1, op, n2 = self.op.replace('old', str(self.items[item_idx])).split(' ')
        return int(n1) * int(n2) if op == '*' else int(n1) + int(n2)


def day11_parts1_2(rounds: int) -> int:
    monkeys = [Monkey(*m[1:]) for m in [monkey_data.strip('\n').split('\n') for monkey_data in
                                        read_infile('day11').split('\n\n')]]
    modf = math.prod([m.divby for m in monkeys])
    for round_count in range(rounds):
        for monkey in monkeys:
            for idx, _ in enumerate(monkey.items):
                newval = monkey.evaluate(idx)
                if rounds <= 20:  # part 1
                    newval //= 3
                else:  # part 2
                    newval %= modf
                throw_to = monkey.throw_true if newval % monkey.divby == 0 else monkey.throw_false
                monkey.inspections += 1
                monkeys[throw_to].items.append(newval)
            monkey.items.clear()

    most_active: list[Monkey] = list(sorted(monkeys, key=lambda sort_monkey: sort_monkey.inspections, reverse=True))
    return most_active[0].inspections * most_active[1].inspections


def run():
    print(f'Day 11 pt1: {day11_parts1_2(rounds=20)}')
    print(f'Day 11 pt2: {day11_parts1_2(rounds=10000)}')

# Day 11 pt1: 56120
# Day 11 pt2: 24389045529

from indata import read_lines


def part1():
    program = read_lines('day8')
    lines_visited = []
    pc, acc = 0, 0
    while True:
        inst, amt = program[pc].split(' ')
        lines_visited.append(pc)
        acc, pc = do_instruction(acc, amt, inst, pc)
        if pc in lines_visited:
            break

    return acc


def part2():
    program = read_lines('day8')
    pc, acc, pgm_len, lines_visited = 0, 0, len(program), []
    last_good_state = (0, 0, [])
    change_next = True

    while pc < pgm_len:
        inst, amt = program[pc].split(' ')
        lines_visited.append(pc)
        if change_next and inst != 'acc':
            last_good_state, change_next = (pc, acc, [x for x in lines_visited]), False
            inst = 'nop' if inst == 'jmp' else 'jmp'

        acc, pc = do_instruction(acc, amt, inst, pc)

        if pc in lines_visited:
            pc, acc, lines_visited = last_good_state
            inst, amt = program[pc].split(' ')
            acc, pc = do_instruction(acc, amt, inst, pc)
            lines_visited.append(pc)
            change_next = True
    return acc


def do_instruction(acc, amt, inst, pc):
    amt_value = int(amt)
    if inst == 'nop':
        pc += 1
    if inst == 'acc':
        acc += amt_value
        pc += 1
    if inst == 'jmp':
        pc += amt_value
    return acc, pc


def run():
    print(f'Day 8 part 1: {part1()}')
    print(f'Day 8 part 2: {part2()}')

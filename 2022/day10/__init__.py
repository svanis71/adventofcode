from indata import read_list_of_strings

CRT_HEIGHT = 6
CRT_WIDTH = 40


def part1(program: list[str]) -> int:
    cycle, reg_x, next_checkpoint, sum_of_strengths = 0, 1, 20, 0

    for instr in program:
        cycle += (1 if instr == 'noop' else 2)
        if cycle >= next_checkpoint:
            sum_of_strengths += next_checkpoint * reg_x
            next_checkpoint += 40
        if instr.startswith('addx'):
            reg_x += int(instr.split(' ')[1])
    return sum_of_strengths


def draw_pixel(crt_pos: int, sprite_position: int, crt_display: list[list[str]]) -> int:
    crt_y, crt_x = divmod(crt_pos, CRT_WIDTH)
    if sprite_position - 1 <= crt_x <= sprite_position + 1:
        crt_display[crt_y][crt_x] = '#'
    return crt_pos + 1


def part2(program: list[str]) -> list[list[str]]:
    cycle, reg_x, crt_pos = 0, 1, 0
    crt = [[' ' for _ in range(CRT_WIDTH)] for _ in range(CRT_HEIGHT)]

    for instr in program:
        cycle += (1 if instr == 'noop' else 2)
        crt_pos = draw_pixel(crt_pos, reg_x, crt)
        if instr.startswith('addx'):
            crt_pos = draw_pixel(crt_pos, reg_x, crt)
            reg_x += int(instr.split(' ')[1])

    return crt


def show_crt(crt):
    for y in range(CRT_HEIGHT):
        for x in range(CRT_WIDTH):
            print(crt[y][x], end='')
        print()


def run():
    program = read_list_of_strings('day10', use_testdata=False)
    print(f'Day 10 pt1: {part1(program)}')
    print('Day 10 pt2:')
    show_crt(part2(program))

# Day 10 pt1: 17380
# Day 10 pt2:
####  ##   ##  #  # #### ###  ####  ##
#    #  # #  # #  #    # #  # #    #  #
###  #    #    #  #   #  #  # ###  #
#    # ## #    #  #  #   ###  #    #
#    #  # #  # #  # #    # #  #    #  #
#     ###  ##   ##  #### #  # ####  ##

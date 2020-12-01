from indata.day2_input import input_data

#
# Pos pc+0 Op (1=Add, 2=Mul, 99=Halt)
# Pos 1 Data position
# Pos 2 Data position
# Pos pc+3 Position to store result
#

print('')
print('************')
print('Day 2')
print('')

# restore the gravity assist program to the "1202 program alarm" state it
# had just before the last computer caught fire.
# replace position 1 with the value 12 and replace position 2 with the value 2

print('Part 1')


def run(instructions, noun, verb):
    program = instructions
    program[1] = noun
    program[2] = verb
    pc = 0
    (op, dp1, dp2, pos) = program[pc:4]
    while op != 99:
        if op == 1:
            program[pos] = program[dp1] + program[dp2]
        elif op == 2:
            program[pos] = program[dp1] * program[dp2]
        else:
            print('ERROR!', op)
        pc = pc + 4
        if program[pc] == 99:
            break
        (op, dp1, dp2, pos) = program[pc:pc + 4]

    return program[0]


print(run([x for x in input_data], 12, 2))

print('Part 2')
cnt, res, output = 0, 0, -1
while res != 19690720 and cnt < 10000:
    cnt = cnt + 1
    res = run([x for x in input_data], cnt // 100, cnt % 100)
print(cnt)

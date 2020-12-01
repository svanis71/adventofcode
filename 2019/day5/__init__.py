from indata.day5_input import input_data


#
# Pos pc+0 Op (1=Add, 2=Mul, 99=Halt)
# Pos 1 Data position
# Pos 2 Data position
# Pos pc+3 Position to store result
#

def get_value(program, mode, pos):
    return pos if mode == 1 else program[pos]


def run(instructions, input_value):
    pc, op = 1, instructions[0]
    while op != 99:
        mode_p0, mode_p1, mode_p2 = 0, 0, 0
        if op > 100:
            sop = list(str(op).zfill(5))
            (mode_p2, mode_p1, mode_p0, dummy, op) = [int(x) for x in sop]
            op = dummy * 10 + op
        if op == 1:
            val_0 = get_value(instructions, mode_p0, instructions[pc])
            val_1 = get_value(instructions, mode_p1, instructions[pc + 1])
            instructions[instructions[pc + 2]] = val_0 + val_1
            pc += 3
        elif op == 2:
            val_0 = get_value(instructions, mode_p0, instructions[pc])
            val_1 = get_value(instructions, mode_p1, instructions[pc + 1])
            instructions[instructions[pc + 2]] = val_0 * val_1
            pc += 3
        elif op == 3:  # Input
            instructions[instructions[pc]] = input_value
            pc += 1
        elif op == 4:  # Output
            output = get_value(instructions, mode_p0, instructions[pc])
            pc += 1
            if instructions[pc] == 99:
                print('Diagnostic code!')
            print(output)
        # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the
        # instruction pointer to the value from the second parameter. Otherwise, it does nothing.
        elif op == 5:
            val_0 = get_value(instructions, mode_p0, instructions[pc])
            val_1 = get_value(instructions, mode_p1, instructions[pc + 1])
            pc = val_1 if val_0 != 0 else pc + 2
        # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer
        # to the value from the second parameter. Otherwise, it does nothing.
        elif op == 6:
            val_0 = get_value(instructions, mode_p0, instructions[pc])
            val_1 = get_value(instructions, mode_p1, instructions[pc + 1])
            pc = val_1 if val_0 == 0 else pc + 2
        # Opcode 7 is less than: if the first parameter is less than the second parameter,
        # it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        elif op == 7:
            val_0 = get_value(instructions, mode_p0, instructions[pc])
            val_1 = get_value(instructions, mode_p1, instructions[pc + 1])
            val_2 = get_value(instructions, mode_p2, instructions[pc + 2])
            instructions[instructions[pc + 2]] = 1 if val_0 < val_1 else 0
            pc += 3
        # Opcode 8 is equals: if the first parameter is equal to the second parameter,
        # it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        elif op == 8:
            val_0 = get_value(instructions, mode_p0, instructions[pc])
            val_1 = get_value(instructions, mode_p1, instructions[pc + 1])
            instructions[instructions[pc + 2]] = 1 if val_0 == val_1 else 0
            pc += 3
        else:
            print('Error at', pc)
            return

        op = instructions[pc]
        pc += 1

    return instructions[0]


# input_data = [1002, 4, 3, 4, 33]
# input_data = [3, 0, 4, 0, 99]

print(run(input_data.copy(), 1))

# Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
# input_data = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]

# Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
# input_data = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]

# Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
# input_data = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]

# Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
# input_data = [3, 3, 1107, -1, 8, 3, 4, 3, 99]

# uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8,
# output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.
# input_data = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
#               1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
#               999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

# 8561843 fel
print(run(input_data.copy(), 5))

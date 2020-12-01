#
# Pos pc+0 Op (1=Add, 2=Mul, 99=Halt)
# Pos 1 Data position
# Pos 2 Data position
# Pos pc+3 Position to store result
#


def get_value(program, mode, pos):
    return pos if mode == 1 else program[pos]


def run_incode_program(instructions, input_values, pc_start):
    pc, op = pc_start, instructions[pc_start]
    pc += 1
    output = 0
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
            instructions[instructions[pc]] = input_values.pop(0)
            pc += 1
        elif op == 4:  # Output
            output = get_value(instructions, mode_p0, instructions[pc])
            pc += 1
            return output, pc, False
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

    return output, 0, True

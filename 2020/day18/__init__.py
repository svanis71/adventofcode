from collections import deque

from indata import read_lines


def eval_expr(expr, usePrecedence=False):
    operands = deque()
    operators = deque()

    while expr:
        token = expr.pop(0)
        if token.isspace():
            continue
        elif token == ')':
            break
        elif token.isnumeric():
            operands.append(int(token))
        elif token in '+*':
            operators.append(token)
        elif token == '(':
            operands.append(eval_expr(expr, usePrecedence))

    if not usePrecedence:
        eval_part_1(operands, operators)
    else:
        eval_part_2(operands, operators)

    return operands.pop()


def eval(lval, op, rval):
    if op == '+':
        return lval + rval
    elif op == '*':
        return lval * rval


def eval_part_1(operands: deque, operators: deque):
    while operators:
        op = operators.popleft()
        rval = operands.popleft()
        lval = operands.popleft()
        operands.insert(0, eval(lval, op, rval))


def eval_part_2(operands: deque, operators: deque):
    while operators:
        op = operators.popleft()
        lval = operands.popleft()
        rval = operands.popleft()
        if op == '+' or len(operators) == 0 or operators[0] == '*':
            operands.insert(0, eval(lval, op, rval))
        else:
            highop = operators.popleft()
            operators.insert(0, op)
            nval = operands.popleft()
            operands.insert(0, eval(rval, highop, nval))
            operands.insert(0, lval)


def part1():
    return sum([eval_expr(list(y)) for y in read_lines('day18')])


def part2():
    return sum([eval_expr(list(y), True) for y in read_lines('day18')])


def run():
    print(f'Day 18 part 1: {part1()}')
    print(f'Day 18 part 2: {part2()}')

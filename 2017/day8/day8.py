from collections import defaultdict


class Day8:
    def lt(a, b):
        return a < b

    def le(a, b):
        return a <= b

    def gt(a, b):
        return a > b

    def ge(a, b):
        return a >= b

    def eq(a, b):
        return a == b

    def ne(a, b):
        return a != b

    def inc(a, b):
        return a + b

    def dec(a, b):
        return a - b

    ops = {
        '<': lambda a,b: Day8.lt(a,b),
        '<=': lambda a,b: Day8.le(a,b),
        '>': lambda a,b: Day8.gt(a,b),
        '>=': lambda a,b: Day8.ge(a,b),
        '!=': lambda a,b: Day8.ne(a,b),
        '==': lambda a,b: Day8.eq(a,b),
    }

    funcs = {
        'inc': lambda a,b: Day8.inc(a,b),
        'dec': lambda a,b: Day8.dec(a,b)
    }
    def part1(self):
        data = [l.strip() for l in open('day8/indata.txt', 'r')]
        registers = defaultdict(int)
        ll = [x.split(' ') for x in data]
        for outreg,func,addval,dummy,cmpreg,op,cmpval in ll:
            if self.ops[op](int(registers[cmpreg]), int(cmpval)):
                registers[outreg] = self.funcs[func](int(registers[outreg]), int(addval))
        return registers[max(registers, key=registers.get)]

    def part2(self):
        data = [l.strip() for l in open('day8/indata.txt', 'r')]
        registers = defaultdict(int)
        maxi = 0
        ll = [x.split(' ') for x in data]
        for outreg,func,addval,dummy,cmpreg,op,cmpval in ll:
            if self.ops[op](int(registers[cmpreg]), int(cmpval)):
                registers[outreg] = self.funcs[func](int(registers[outreg]), int(addval))
            tmax = int(registers[outreg])
            maxi = tmax if tmax > maxi else maxi
        return maxi

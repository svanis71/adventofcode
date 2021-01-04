from functools import reduce

indata = '''1001796
37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,457,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,431,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19'''


def part1():
    data = indata.split('\n')
    arrives, busids = int(data[0]), [int(x) for x in data[1].split(',') if x != 'x']
    busid, minutes = sorted([(busid, busid - (arrives % busid)) for busid in busids], key=lambda bus: bus[1]).pop(0)
    return busid * minutes


# modular inverse driver function
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euclidean(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m


def crt(busids, mods):
    sum = 0
    lcm = reduce(lambda x, y: x * y, busids)  # Least common multiple
    for busid, remainder in zip(busids, mods):
        p = lcm // busid
        sum += remainder * modinv(p, busid) * p
    return sum % lcm


def part2():
    ign, data = indata.split('\n')
    buses = [int(busid) for busid in data.split(',') if busid != 'x']
    mods = [t if t == 0 else int(busid) - t for t, busid in enumerate(data.split(',')) if busid != 'x']
    return crt(buses, mods)


def run():
    print(f'Day 13 part 1: {part1()}')
    print(f'Day 13 part 2: {part2()}')

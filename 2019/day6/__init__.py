from collections import defaultdict
from indata.day6_input import input_data

p1_do = defaultdict(list)
p1_ido = defaultdict(list)


def get_path_p1(direct, to):
    if to in p1_do:
        for p in p1_do[to]:
            p1_ido[direct].append(p)
            get_path_p1(direct, p)


# Part 1
for line in input_data:
    orbits, orb = line.split(')')
    p1_do[orb].append(orbits)

for orb, orbits in p1_do.items():
    # find path to orb
    get_path_p1(orb, orbits[0])

# part 2
you_list = p1_ido['YOU']
san_list = p1_ido['SAN']

steps = 0
for you in you_list:
    steps += 1
    if you in san_list:
        for san in san_list:
            steps += 1
            if san == you:
                break
        break

directs = len(p1_do)
indirects = sum([len(p1_ido[x]) for x in p1_ido])
print('Part 1 Answer', directs + indirects)  # 186597
print('Part 2 answer', steps)  # 421

# johan@zenit:~/home/Kod/aoc19$ time python3 main.py
# Part 1 Answer 186597
# Part 2 answer 412
#
# real    0m0.731s
# user    0m0.141s
# sys     0m0.094s
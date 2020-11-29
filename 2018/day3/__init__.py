from collections import defaultdict
import re

regexp = r'^#(\d+)\s@\s(\d+),(\d+)\:\s(\d+)x(\d+)$'
with open('day3/in.txt') as f:
    content = f.readlines()
rows = [re.findall(regexp, x.strip())[0] for x in content]

matrix = defaultdict(int)
for row in rows:
    (dummy, x, y, w, h) = [int(v) for v in row]
    for i in range(int(w)):
        for j in range(int(h)):
            matrix[(x + i, y + j)] = matrix[(x + i, y + j)] + 1
overlaps = 0
for key in matrix.keys():
    if matrix[key] > 1:
        overlaps = overlaps + 1

print(overlaps)

# Pt 2
for row in rows:
    (elfid, x, y, w, h) = [int(v) for v in row]
    hit = True
    for i in range(int(w)):
        for j in range(int(h)):
            if hit is True and matrix[(x + i, y + j)] != 1:
                hit = False
    if hit is True:
        print('Hit at Elf id: %d' % elfid)


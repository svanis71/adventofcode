from collections import defaultdict
import re


def getSortkey(q):
    return int("".join([q[0], q[1], q[2], q[3], q[4]]))

def getSortKeyGuard(k, v):
    return v

regexp = r'^\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)$'
with open('day4/in.txt') as f:
    content = f.readlines()
rows = sorted([re.findall(regexp, x.strip())[0] for x in content], key=getSortkey)

loggbook = defaultdict(int)
guardTotal = defaultdict(int)
for r in rows:
    (yy, mm, dd, hr, min, event) = r
    if event.startswith('Guard'):
        guardid = re.findall(r'Guard #(\d+).*', event)[0]
    if event.startswith('falls'):
        sleepstart = (hr, min)
    if event.startswith('wakes'):
        sleepend = (hr, min)
        guardTotal[guardid] += (int(sleepend[1]) - int(sleepstart[1]))
        for i in range(int(sleepstart[1]), int(sleepend[1])):
            loggbook[(guardid, i)] += 1

mostTiredGuard = sorted(guardTotal.items(), key=lambda k: k[1], reverse=True)[0][0]
(maxmin, sleephours) = sorted([(x[1], loggbook[x]) for x in loggbook.keys() if x[0] == mostTiredGuard], key=lambda i: i[1], reverse=True)[0]

# Part 1
print('Guard: %s * minute: %d => %d' % (mostTiredGuard, maxmin, int(mostTiredGuard) * maxmin))

# Part 2
l = sorted(loggbook.items(), key=lambda k: k[1], reverse=True)[0]
print('Most minute: %d for guard %s => %d' % (l[0][1], l[0][0], l[0][1] * int(l[0][0])))

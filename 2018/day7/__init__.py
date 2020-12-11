import re
from collections import defaultdict

with open('day7/in.txt') as f:
    content = f.readlines()
regexp = r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.'

dd = defaultdict(list)
has_dependency = []
for ln in content:
    step, dependency_step = re.findall(regexp, ln)[0]
    dd[step].append(dependency_step)
    if not dependency_step in has_dependency:
        has_dependency.append(dependency_step)
available = sorted([s for s in dd.keys() if s not in has_dependency])
endpoints = sorted([s for s in has_dependency if s not in dd.keys()])
queue = []
nod = available[0]
while nod is not None:
    queue.append(nod)
    for step in dd[nod]:
        l = [x for x in dd.keys() if x != nod and step in dd[x]]
        if len(l) == 0:
            has_dependency.remove(step)
    del dd[nod]
    available = sorted([s for s in dd.keys() if s not in has_dependency])
    nod = None if len(available) == 0 else available[0]

queue = queue + endpoints
print(''.join(queue))


# part 2
for ln in content:
    step, dependency_step = re.findall(regexp, ln)[0]
    dd[step].append(dependency_step)
    if not dependency_step in has_dependency:
        has_dependency.append(dependency_step)
available = sorted([s for s in dd.keys() if s not in has_dependency])
endpoints = sorted([s for s in has_dependency if s not in dd.keys()])

queue = []
while len(available) > 0:
    queue.append(available[0])
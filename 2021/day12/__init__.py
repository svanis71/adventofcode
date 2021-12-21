from collections import deque

from indata import read_list_of_strings


def find_paths(max_visits_in_small_caves=1):
    indata = [{"from": fr, "to": to} for (fr, to) in read_list_of_strings('day12', '-')]
    for i in indata:
        if i["to"] == 'start':
            i['from'], i['to'], = i['to'], i['from']
    indata.extend([{"from": d["to"], "to": d["from"]} for d in indata if d["from"] != 'start' and d["to"] != 'end'])
    paths = []
    queue = deque([(tt["from"], tt["to"],) for tt in indata if tt['from'] == 'start'])
    while queue:
        curr_node = queue.popleft()
        if any(x for x in indata if x["to"] == 'end' and x["from"] == curr_node[-1]):
            paths.append(curr_node + ('end',))
        for next_candidate in [curr_node + (candidate_node["to"],) for candidate_node in indata if
                               candidate_node["to"] != 'end' and candidate_node["from"] == curr_node[-1]]:
            if max_visits_in_small_caves > 1:
                count_small_caves = len(
                    set([x for x in next_candidate if
                         x.islower() and next_candidate.count(x) == max_visits_in_small_caves]))
                if count_small_caves > 1:
                    continue
            if next_candidate[-1].islower() and next_candidate.count(
                    next_candidate[-1]) > max_visits_in_small_caves:  # next_candidate[-1] in visited_small_caves:
                continue
            queue.append(next_candidate)
    return paths


def part1():
    return len(find_paths())


def part2():
    return len(find_paths(2))


def run():
    print(f'Day 12 pt1: {part1()}')
    print(f'Day 12 pt2: {part2()}')

# Day 12 pt1: 3713
# Day 12 pt2: 91292

import re
from math import prod

from indata import read_list_of_strings


def part1():
    paper: list[str] = read_list_of_strings('day6', use_testdata=False)
    race_times: list[int] = [int(s) for s in re.findall(r'\b(\d+)\b', paper.pop(0))]
    record_list: list[int] = [int(s) for s in re.findall(r'\b(\d+)\b', paper.pop(0))]
    way_to_break_record: list[int] = []
    for (race_time, record_to_beat) in zip(race_times, record_list):
        records: int = 0
        for millis in range(1, race_time + 1):
            remaining_race_time = race_time - millis
            if remaining_race_time * millis > record_to_beat:
                records += 1
        way_to_break_record.append(records)
    return prod(way_to_break_record)


def part2():
    paper: list[str] = read_list_of_strings('day6', use_testdata=False)
    race_time: int = int(''.join(re.findall(r'\b(\d+)\b', paper.pop(0))))
    record_to_beat: int = int(''.join(re.findall(r'\b(\d+)\b', paper.pop(0))))
    records = find_ways_to_set_record(0, race_time, record_to_beat, records=race_time, steps=1)
    records = find_ways_to_set_record(race_time + 1, race_time, record_to_beat, records, -1)

    return records


def find_ways_to_set_record(millis: int, race_time: int, record_to_beat: int, records: int, steps: int):
    while True:
        millis += steps
        remaining_race_time = race_time - millis
        if remaining_race_time * millis >= record_to_beat:
            break
        records -= 1
    return records


def run():
    print(f'Day 6 pt1: {part1()}')
    print(f'Day 6 pt2: {part2()}')

# Day 6 pt1: 219849
# Day 6 pt2: 29432455

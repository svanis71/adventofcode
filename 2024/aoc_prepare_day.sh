#!/usr/bin/env bash

if [ ! -e "main.py" ]; then
    echo "from time import perf_counter

# insert import before (don't remove this line)

RUN_ALL_DAYS:bool = True
if __name__ == '__main__':
    if RUN_ALL_DAYS:
        start = perf_counter()" > main.py
fi

day=$1 
mkdir -p day${day} 
echo "import indata


def part1(puzzle_input: list[str]) -> int:
    pass


def part2(puzzle_input: list[str]) -> int:
    pass


def run():
    puzzle_data = indata.read_list_of_strings('day${day}', use_testdata=True)
    print(f'Day ${day} pt1: {part1(puzzle_data)}')
    print(f'Day ${day} pt2: {part2(puzzle_data)}')


# Day ${day} pt1: 0
# Day ${day} pt2: 0

if __name__ == '__main__':
    run()

" > day${day}/__init__.py

[ ! -d "indata" ] && mkdir indata
touch indata/day${day}.txt
touch indata/day${day}_test.txt

sed -i "/^\# insert import before/i import day${day}" main.py

echo "        day${day}.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()" >> main.py

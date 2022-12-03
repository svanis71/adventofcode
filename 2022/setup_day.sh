#!/usr/bin/env bash

day=$1 
mkdir -p day${day} 
echo "from indata import read_list_of_strings


def part1():
    pass


def part2():
    pass


def run():
    print(f'Day ${day} pt1: {part1()}')
    print(f'Day ${day} pt2: {part2()}')


# Day ${day} pt1: 
# Day ${day} pt2: 
" > day${day}/__init__.py


[ ! -d "indata" ] && mkdir indata
touch indata/day${day}.txt
touch indata/day${day}_test.txt

sed "/^\# insert import before/i import day${day}" main.py > main_tmp.py
mv main_tmp.py main.py

echo "        day${day}.run()
              print(f'Time: {perf_counter() - start} seconds')
              start = perf_counter()" >> main.py

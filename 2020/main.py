import day1
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day18
import day2
import day3
import day4
import day5
import day6
import day8
import day9

with open('indata/day16.txt') as f:
    indata = f.read().split(('\n\n'))

print(day16.part2(indata))

if __name__ == '__main__':
    day1.run()
    day2.run()
    day3.run()
    day4.run()
    day5.run()
    day6.run()
    # day 7 part 1 runs very slow so I commented out the execution of the day
    # day7.run()
    day8.run()
    day9.run()
    day10.run()
    day11.run()
    day12.run()
    day13.run()
    day14.run()
    day15.run()
    day16.run()
    day18.run()

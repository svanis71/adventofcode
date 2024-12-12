from time import perf_counter

import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day11
# insert import before (don't remove this line)


RUN_ALL_DAYS: bool = True
if __name__ == '__main__':
    if RUN_ALL_DAYS:
        start = perf_counter()
        day1.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()
        day2.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()
        day3.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()
        day4.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()
        day5.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()
        day5.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()
        day6.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()
        day7.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()
        day11.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()

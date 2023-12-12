from time import perf_counter

import day1
import day2
import day3
import day4
import day5
# insert import before (don't remove this line)

runall = True
#day2.run()

if __name__ == '__main__':
    if runall:
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

from time import perf_counter

import day1
# insert import before (don't remove this line)

runall = True
if __name__ == '__main__':
    if runall:
        start = perf_counter()
        day1.run()
        print(f'Time: {perf_counter() - start} seconds')
        start = perf_counter()

import time

import day1
# insert import before (don't remove this line)


RUN_ALL_DAYS:bool = True
if __name__ == '__main__':
    if RUN_ALL_DAYS:
        start = time.perf_counter()
        day1.run()
        print(f'Time: {time.perf_counter() - start} seconds')
        start = time.perf_counter()

from collections import Counter

class Day4:
    def __init__(self):
        with open('day4/indata.txt', 'r') as myfile:
            self.data=myfile.read().split('\n')

    def part1(self):
        sum = 0
        for line in self.data:
            if len(line) > 0:
                cnt = Counter(line.strip().split(' '))
                if(cnt.most_common(1)[0][1] == 1):
                    sum += 1
        return sum
    
    def part2(self):
        sum = 0
        for line in self.data:
            if len(line) > 0:
                sa = [''.join(sorted(list(i))) for i in line.strip().split(' ')]
                cnt = Counter(sa)
                if(cnt.most_common(1)[0][1] == 1):
                    sum += 1
        return sum

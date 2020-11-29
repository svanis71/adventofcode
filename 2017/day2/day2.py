
class Day2:
    def __init__(self):
        with open('day2/indata.txt', 'r') as myfile:
            self.data=myfile.read().split('\n')

    def part1(self):
        sum = 0
        for line in self.data:
            if(len(line) > 0):
                numbers = [int(s) for s in line.split('\t')]
                sum += (max(numbers) - min(numbers))
        return sum
    
    def part2(self):
        sum = 0
        for line in self.data:
            if len(line) > 0:
                numbers = sorted([int(s) for s in line.split('\t')], key=int, reverse=True)
                for i,x in enumerate(numbers):
                    div = [n for n in numbers[i+1:] if x % n == 0]
                    if div:
                        sum += int(x / div[0])
                        break
                    
        return sum

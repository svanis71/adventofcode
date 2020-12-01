import math
from collections import defaultdict

class Day3:
    def getSum(self, curpos, spiralen):
        curX, curY = curpos
        sum = spiralen[(curX + 1, curY)] # e
        sum += spiralen[(curX - 1, curY)] # w
        sum += spiralen[(curX, curY - 1)] # n
        sum += spiralen[(curX, curY + 1)] # s
        sum += spiralen[(curX + 1, curY + 1)] # se
        sum += spiralen[(curX - 1, curY - 1)] # nw
        sum += spiralen[(curX + 1, curY - 1)] # ne
        sum += spiralen[(curX - 1, curY + 1)] # sw
        return sum

    def nextPos(self, cur, spiralen):
        curX, curY = cur
        
        newPos = ()
        # Up
        if spiralen[(curX - 1, curY)] != 0 and spiralen[(curX, curY -1)] == 0:
            newPos = (curX, curY - 1)
            # Left
        elif spiralen[(curX, curY + 1)] != 0 and spiralen[(curX - 1, curY)] == 0:
            newPos = (curX - 1, curY)
            # Down
        elif spiralen[(curX + 1, curY)] != 0 and spiralen[(curX, curY + 1)] == 0:
            newPos = (curX, curY + 1)
            # Right
        else:
            newPos = (curX + 1, curY)
            
        return newPos

    def part1(self):

        target = 289326
        levels = math.ceil(math.sqrt(target))
        last = levels * levels
        diff = last - target

        starty = math.floor(levels / 2)
        startx = math.ceil(levels / 2) - 1

        xdiff = int(math.fabs(diff-startx))
        diff = xdiff + starty
        
        print("levels = %d" % levels)
        print("last = %d, diff = %d" % (last, diff))
        print("start (%d, %d)" % (startx, starty))
        print("xdiff = %d, ydiff = %d, dist = %d" % (xdiff, starty, diff))

        return diff
    
    def part2(self):
        target = 289326
        val = 1
        spiral = defaultdict(int)
        # x,y
        pos = (0,0)
        spiral[pos] = 1
        pos = (1,0)
        spiral[pos] = 1
        
        while spiral[pos] < target:
            pos = self.nextPos(pos, spiral)
            spiral[pos] =  self.getSum(pos, spiral)
        return spiral[pos]
            

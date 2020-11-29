class Day10:
    def knotHash(self, size, lengths):
        h = [x for x in range(size)]
        cur = 0
        skip = 0
        for l in lengths:
            print("LENGTH=%d" % l)
            if (cur + l) < size:
                tl = h[cur:cur+l]
                tl = tl[::-1]

                for i in range(len(tl)):
                    h[cur + i] = tl[i]
            else:
                tl = (h[cur:] + h[:(cur + l)-size])
                tl = tl[::-1]
                for i in range(len(tl)):
                    h[(cur + i) % size] = tl[i]
            print(h)
            cur += (l + skip)
            cur %= size
            print("cur %d" % cur)
            skip = skip + 1

        return h

    def part1(self):
        #lengths = [3, 4, 1, 5]
        lengths = [70, 66, 255, 2, 48, 0, 54, 48, 80, 141, 244, 254, 160, 108, 1, 41]
        hash = self.knotHash(256, lengths)
        return hash[0] * hash[1]

    def part2(self):
        return 0

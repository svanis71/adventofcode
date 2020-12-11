
def isAscending(num):
    for i in range(len(num) - 1):
        if ord(num[i]) > ord(num[i + 1]):
            return False
    return True


def hasGroup(num):
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            return True
    return False


def hasPair(num):
    pos = 0
    pairCandidate = num[0]
    while pos < len(num):
        if num[pos] == pairCandidate:
            cnt = 0
            while pos < len(num) and num[pos] == pairCandidate:
                cnt += 1
                pos += 1
            if cnt == 2:
                return True
            pairCandidate = '' if pos >= len(num) else num[pos]
        else:
            pos += 1
    return False


# 357253-892942
cnt1, cnt2 = 0, 0
for i in range(357253, 892942):
    sn = str(i)
    part1 = isAscending(sn) and hasGroup(sn)
    if part1:
        cnt1 += 1
    if part1 and hasPair(sn):
        cnt2 += 1

print('Part 1:', cnt1, 'Hits!')  # 530
print('Part 2:', cnt2, 'Hits!')  # 324

def readIntList(day):
    with open('indata/%s.txt' % day) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]


def readLines(day):
    with open('indata/%s.txt' % day) as f:
        content = f.readlines()
    return [x.strip() for x in content]

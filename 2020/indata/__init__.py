def read_list_of_integers(day):
    with open('indata/%s.txt' % day) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]


def read_lines(day):
    with open('indata/%s.txt' % day) as f:
        content = f.readlines()
    return [x.strip() for x in content]

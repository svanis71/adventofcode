def read_list_of_strings(day, splitchar=None):
    with open('indata/%s.txt' % day) as f:
        content = f.readlines()
    lines = [x.strip() for x in content]
    return lines if not splitchar else [line.split(splitchar) for line in lines]


def read_list_of_integers(day):
    with open('indata/%s.txt' % day) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]

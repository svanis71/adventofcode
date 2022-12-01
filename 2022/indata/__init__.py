def read_list_of_strings(filename, splitchar=None):
    with open(f'indata/{filename}.txt', encoding='utf-8') as f:
        content = f.readlines()
    lines = [x.strip() for x in content]
    return lines if not splitchar else [line.split(splitchar) for line in lines]


def read_list_of_integers(filename):
    with open(f'indata/{filename}.txt', encoding='utf-8') as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]


def read_csv_integers(filename, splitchar=','):
    with open(f'indata/{filename}.txt', encoding='utf-8') as f:
        content = f.readline()
    return [int(x.strip()) for x in content.split(splitchar)]

from os.path import dirname, realpath, join

infiles_path: str = dirname(realpath(__file__))


def read_infile(filename, is_testdata: bool = False) -> str:
    if is_testdata:
        filename += '_test'
    with open(join(infiles_path, f'{filename}.txt'), encoding='utf-8') as f:
        content = f.readlines()
    return ''.join(content)


def read_list_of_strings(filename, splitchar=None) -> list[str]:
    with open(join(infiles_path, f'{filename}.txt'), encoding='utf-8') as f:
        content = f.readlines()
    lines = [x.strip() for x in content]
    return lines if not splitchar else [line.split(splitchar) for line in lines]


def read_list_of_integers(filename) -> list[int]:
    with open(join(infiles_path, f'{filename}.txt'), encoding='utf-8') as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]


def read_csv_integers(filename, splitchar=',') -> list[int]:
    with open(join(infiles_path, f'{filename}.txt'), encoding='utf-8') as f:
        content = f.readline()
    return [int(x.strip()) for x in content.split(splitchar)]

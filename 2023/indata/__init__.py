from os.path import dirname, realpath, join

infiles_path: str = dirname(realpath(__file__))


def read_infile(filename, use_testdata: bool = False) -> str:
    if use_testdata:
        filename += '_test'
    with open(join(infiles_path, f'{filename}.txt'), encoding='utf-8') as handle:
        content = handle.readlines()
    return ''.join(content)


def read_list_of_strings(filename, splitchar=None, use_testdata: bool = False) -> list[str]:
    lines = [x.strip() for x in read_infile(filename, use_testdata).split('\n')]
    return lines if not splitchar else [line.split(splitchar) for line in lines]


def read_list_of_integers(filename, use_testdata: bool = False) -> list[int]:
    content = [x.strip() for x in read_infile(filename, use_testdata)]
    return [int(x.strip()) for x in content]

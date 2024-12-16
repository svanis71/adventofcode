import indata


def create_disk(blocks):
    disk_size = sum(blocks)
    disk = [-1] * disk_size
    next_block, file_id = 0, 0
    file_index: list[dict] = []
    free_space: list[tuple[int, int]] = []
    for ix, block_size in enumerate(blocks, 1):
        if ix % 2 != 0:
            disk[next_block:next_block + block_size] = [file_id] * block_size
            file_index.append({'file_id': file_id, 'size': block_size, 'pos': (next_block, next_block + block_size)})
            file_id += 1
        else:
            free_space.append((next_block, block_size))
        next_block += block_size
    return disk, file_index, free_space


def sort_part1(disk):
    disk_size = len(disk)
    next_free, next_to_move = -1, disk_size - 1
    while True:
        next_free = disk.index(-1, next_free + 1)
        while disk[next_to_move] == -1:
            next_to_move -= 1
        if next_free >= next_to_move:
            break
        disk[next_free] = disk[next_to_move]
        disk[next_to_move] = -1
    return disk


def sort_part2(disk, file_index, free_space):
    for file in file_index[::-1]:
        file_pos = file['pos']
        siz = file['size']
        for ix, (pos, length) in enumerate(free_space):
            if length >= siz and pos < file_pos[0]:
                disk[pos:pos + siz] = [file['file_id']] * siz
                disk[file_pos[0]:file_pos[1]] = [-1] * siz
                update_free = (pos + siz, length - siz)
                free_space[ix] = update_free
                break
    return disk


def run():
    puzzle_data: str = indata.read_infile('day9', use_testdata=False)
    blocks = list(map(int, list(puzzle_data)))
    disk, _, _ = create_disk(blocks)
    print(f'Day 9 pt1: {sum(file_id * pos for pos, file_id in enumerate(sort_part1(disk)) if file_id != -1)}')
    disk, file_index, free_space = create_disk(blocks)
    p2_checksum = sum(
        file_id * pos for pos, file_id in enumerate(sort_part2(disk, file_index, free_space)) if file_id != -1)
    print(f'Day 9 pt2: {p2_checksum}')


# Day 9 pt1: 6299243228569
# Day 9 pt2: 6326952672104

if __name__ == '__main__':
    run()

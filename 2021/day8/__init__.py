from indata import read_list_of_strings


def create_decode_map(patterns):
    decode_map, known_length = {}, {2: 1, 3: 7, 4: 4, 7: 8}
    for pattern in patterns:
        segments = set(pattern)
        pattern_length = len(pattern)
        if pattern_length < 5 or pattern_length == 7: 
            dig = known_length[pattern_length]
            decode_map[dig] = set(pattern)
        elif pattern_length == 5:
            L = decode_map[4]-decode_map[1]
            if decode_map[7].issubset(segments):
                decode_map[3] = segments
            elif L.issubset(segments):
                decode_map[5] = segments
            else:
                decode_map[2] = segments
        elif pattern_length == 6:
            L = decode_map[4]-decode_map[1]
            if not L.issubset(segments):
                decode_map[0] = segments
            elif decode_map[7].issubset(segments):
                decode_map[9] = segments
            else:
                decode_map[6] = segments
    return {''.join(sorted(decoded_value)) : pattern for pattern, decoded_value in decode_map.items()}


def part1():
    notes = [(signal_pattern.split(' '), output.split(' ')) for signal_pattern, output in read_list_of_strings('day8', ' | ')]
    l = []
    for signal, outp in notes:
        l += [num for num in outp if len(num) < 5 or len(num) == 7]
    return len(l)

def part2():
    notes = [(signal_pattern.split(' '), output.split(' ')) for signal_pattern, output in read_list_of_strings('day8', ' | ')]
    nums = []
    for signal_patterns, out_patterns in notes:
        decode_map = create_decode_map(sorted(signal_patterns, key=len))
        display_digits = ''
        for pattern in out_patterns:
            display_digits += str(decode_map[''.join(sorted(pattern))])
        nums.append(int(display_digits))
    return sum(nums)


def run():
    print(f'Day 8 pt1: {part1()}')
    print(f'Day 8 pt2: {part2()}')


# Day 8 pt1: 
# Day 8 pt2: 


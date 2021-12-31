def decode_packet(bits, versions=[], subpackages_len_so_far=0):
    versions.append(int(bits[0:3], 2))
    packet_type = int(bits[3:6], 2)
    qb = bits[6:]
    acc_subpackets_length = subpackages_len_so_far + 6
    if packet_type == 4:
        value = ''
        while True:
            is_last_number = qb[0] == '0'
            value += qb[1:5]
            qb = qb[5:]
            acc_subpackets_length += 5
            if is_last_number:
                break
        return qb, int(value, 2), acc_subpackets_length
    else:
        type_id = qb[0]
        acc_subpackets_length += 1
        qb = qb[1:]
        values = []
        if type_id == '0':
            subpackets_len, packet_length = int(qb[:15], 2), 0
            qb = qb[15:]
            acc_subpackets_length += 15
            while packet_length < subpackets_len:
                qb, packet_value, packet_len = decode_packet(qb, versions)
                values.append(packet_value)
                packet_length += packet_len
            acc_subpackets_length += packet_length
        else:
            subpackets_cnt, packet_length = int(qb[:11], 2), 0
            qb = qb[11:]
            acc_subpackets_length += 11
            for i in range(subpackets_cnt):
                qb, packet_value, packet_len = decode_packet(qb, versions)
                values.append(packet_value)
                packet_length += packet_len
            acc_subpackets_length += packet_length

        result = 0
        if packet_type == 0:
            result = sum(values)
        if packet_type == 1:
            result = 1
            for v in values:
                result *= v
        if packet_type == 2:
            result = min(values)
        if packet_type == 3:
            result = max(values)
        if packet_type == 5:
            result = 1 if values[0] > values[-1] else 0
        if packet_type == 6:
            result = 1 if values[0] < values[-1] else 0
        if packet_type == 7:
            result = 1 if values[0] == values[-1] else 0
        return qb, result, acc_subpackets_length


def part1(instr):
    bits = ''.join(str(bin(int(hd, 16))[2:]).zfill(4) for hd in instr)
    versions = []
    decode_packet(bits, versions)
    return sum(versions)


def part2(instr):
    bits = ''.join(str(bin(int(hd, 16))[2:]).zfill(4) for hd in instr)
    versions = []
    _, result, _ = decode_packet(bits, versions)
    return result


def run():
    instr = open('indata/day16.txt').readline().strip()
    print(f'Day 16 pt1: {part1(instr)}')
    print(f'Day 16 pt2: {part2(instr)}')

# Day 16 pt1:
# Day 16 pt2:

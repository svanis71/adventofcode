import indata
from indata import read_list_of_strings


def decode_packet(bits, versions=[], sublen=0):
    versions.append(int(bits[0:3], 2))
    packet_type = int(bits[3:6], 2)
    qb = bits[6:]
    sublen += 6
    if packet_type == 4:
        value = ''
        while True:
            last = qb[0] == '0'
            value += qb[1:5]
            qb = qb[5:]
            sublen += 5
            if last: break
        return qb, int(value, 2), sublen
    else:
        type_id = qb[0]
        sublen += 1
        qb = qb[1:]
        values = []
        if type_id == '0':
            subpackets_len, next_packetlen = int(qb[:15], 2), 0
            qb = qb[15:]
            sublen += 15
            while next_packetlen < subpackets_len:
                qb, packet_value, packet_len = decode_packet(qb, versions)
                values.append(packet_value)
                next_packetlen += packet_len
            sublen += next_packetlen
        else:
            subpackets_cnt, next_packetlen = int(qb[:11], 2), 0
            qb = qb[11:]
            sublen += 11
            for i in range(subpackets_cnt):
                qb, packet_value, packet_len = decode_packet(qb, versions)
                values.append(packet_value)
                next_packetlen += packet_len
            sublen += next_packetlen


        return qb, 0, sublen

def part1():
    instr = open('indata/day16.txt').readline().strip()
    bits = ''.join(str(bin(int(hd, 16))[2:]).zfill(4) for hd in instr)
    versions = []
    decode_packet(bits, versions)
    return sum(versions)


def part2():
    pass


def run():
    print(f'Day 16 pt1: {part1()}')
    print(f'Day 16 pt2: {part2()}')

# Day 16 pt1:
# Day 16 pt2:

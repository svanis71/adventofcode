import re


def part1(ticket_parts):
    valids = get_valid_numbers(ticket_parts)
    nearby_tickets = ticket_parts[2].split('\n')
    nearby_tickets.pop(0)  # header
    invalidos = [int(n) for n in ','.join(nearby_tickets).split(',') if int(n) not in valids]
    return sum(invalidos)


def part2(ticket_parts):
    valid_tickets = get_valid_nearby_tickets(ticket_parts)
    fields = get_field_numbers(ticket_parts)
    pivot = get_pivot_table(fields, valid_tickets)
    ticket_fields = analyse_columns(fields, pivot)
    my_tickets = get_my_tickets(ticket_parts)

    prod = 1
    for k, v in ticket_fields.items():
        if k.startswith('departure'):
            prod *= my_tickets[v]

    return prod


def analyse_columns(fields, pivot):
    column_field_candidates = {}
    ticket_fields = {name: -1 for name in fields}
    for ix, column in enumerate(pivot):  # (3,15,18)
        column_field_candidates[ix] = []
        for field_ix, (field, val) in enumerate(fields.items()):
            if all(x in val for x in column):
                column_field_candidates[ix].append(field)
    while True:
        if all(-1 != v for v in ticket_fields.values()):
            break
        for colnr, candidate_list in enumerate(column_field_candidates.items()):
            adjusted_list = [cand for cand in candidate_list[1] if ticket_fields[cand] == -1]
            column_field_candidates[colnr] = adjusted_list
            if len(adjusted_list) == 1:
                ticket_fields[column_field_candidates[colnr].pop(0)] = candidate_list[0]
    return ticket_fields


def get_pivot_table(fields, valid_tickets):
    pivot = []
    for col in range(len(fields)):
        coldata = ()
        for row in valid_tickets:
            coldata += (row[col],)
        pivot.append(coldata)
    return pivot


def get_field_numbers(ticket_parts):
    fields_data = ticket_parts[0].split('\n')
    fields = {}
    for field in fields_data:
        name, intervals = field.split(': ')
        valido_numbers = []
        for valido in re.findall(r'(\d+-\d+) or (\d+-\d+)', intervals):
            int1, int2 = valido
            n1, n2 = [int(n) for n in int1.split('-')]
            n3, n4 = [int(n) for n in int2.split('-')]
            for i in range(n1, n4 + 1):
                if n1 <= i <= n2 or i >= n3:
                    valido_numbers.append(i)
        fields[name] = valido_numbers
    return fields


def get_valid_nearby_tickets(ticket_parts):
    valids = get_valid_numbers(ticket_parts)
    nearby_tickets = ticket_parts[2].split('\n')
    nearby_tickets.pop(0)  # header
    return [[int(x) for x in t.split(',')] for t in nearby_tickets if all(int(n) in valids for n in t.split(','))]


def get_my_tickets(ticket_parts):
    tickets = ticket_parts[1].split('\n')
    tickets.pop(0)  # header
    return [int(x) for x in tickets.pop(0).split(',')]


def get_valid_numbers(ticket_parts):
    rules = ticket_parts[0].split('\n')
    valido_intervals = [re.findall(r'[a-z]+:\s(\d+-\d+) or (\d+-\d+)', x).pop(0) for x in rules]
    valido_numbers = set()
    for valido in valido_intervals:
        int1, int2 = valido
        n1, n2 = [int(n) for n in int1.split('-')]
        n3, n4 = [int(n) for n in int2.split('-')]
        for i in range(n1, n4 + 1):
            if n1 <= i <= n2 or i >= n3:
                valido_numbers.add(i)

    return valido_numbers


def run():
    with open('indata/day16.txt') as f:
        indata = f.read().split(('\n\n'))

    print(f'Day 16 part 1: {part1(indata)}')
    print(f'Day 16 part 2: {part2(indata)}')

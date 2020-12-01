from collections import defaultdict
from itertools import permutations
from intcode import run_incode_program
from indata.day7_input import input_data

all_combos = [x for x in permutations([0, 1, 2, 3, 4], 5)]
outputs = []

for seq in all_combos:
    res = 0
    for input in seq:
        res, pc, done = run_incode_program(input_data.copy(), [input, res], 0)
    outputs.append(res)
print(max(outputs))

# Part 2
all_combos_p2 = [x for x in permutations([5, 6, 7, 8, 9], 5)]
outdata = defaultdict(int)

for tseq in all_combos_p2:
    the_end = False
    amplifiers = ['a', 'b', 'c', 'd', 'e']
    state = {
        'a': {'inparams': [0], 'pc_start': 0, "program": input_data.copy()},
        'b': {'inparams': [], 'pc_start': 0, "program": input_data.copy()},
        'c': {'inparams': [], 'pc_start': 0, "program": input_data.copy()},
        'd': {'inparams': [], 'pc_start': 0, "program": input_data.copy()},
        'e': {'inparams': [], 'pc_start': 0, "program": input_data.copy()},
    }
    seq = list(tseq)
    out = 0
    outputs = []
    while not the_end:
        current_amplifier = amplifiers.pop(0)
        amplifier_ = state[current_amplifier]
        if len(seq) > 0:
            phase_setting = seq.pop(0)
            amplifier_['inparams'].insert(0, phase_setting)
        out, pc, the_end = run_incode_program(amplifier_['program'], amplifier_['inparams'], amplifier_['pc_start'])
        amplifier_['pc_start'] = pc
        state[amplifiers[0]]['inparams'].append(out)
        amplifiers.append(current_amplifier)
        outputs.append(out)
    if len(outputs) > 0:
        outdata[tseq] = max(outputs.copy())

res = 0
state = {}

print(max(outdata.values()))

from collections import defaultdict
from textwrap import wrap
from .input import image_data

image_width = 25
image_height = 6
size = image_width * image_height
layers = wrap(image_data, image_width * image_height)
part1_answer = defaultdict(int)
target = ['2' * image_width] * 6

for layer in layers:
    zeros = len([z for z in layer if z == '0'])
    ones = len([z for z in layer if z == '1'])
    twos = len([z for z in layer if z == '2'])
    part1_answer[zeros] = ones * twos
    rows = wrap(layer, image_width)

    for r, row in enumerate(rows):
        tmprow = ''
        for x in zip(target[r], row):
            tmprow += x[0] if x[0] != '2' or x[1] == '2' else '#' if x[1] == '1' else ' '
        target[r] = tmprow

print('Part 1 was', part1_answer[min(part1_answer.keys())])
for row in target:
    print(row)

# Part 1 was 1330

####  ##  #  # #### ####
#    #  # #  # #    #
###  #  # #### ###  ###
#    #### #  # #    #
#    #  # #  # #    #
#    #  # #  # #### #



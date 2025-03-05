import sys

import pygame

import indata
from common import DIRECTIONS
from day15 import get_start_pos, move_horizontal, move_robot, get_score, warehouse_large

# Initialize Pygame
pygame.init()

# Set up display
cell_sz = 1
width, height = 1000, 1100
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Warehouse Woes')

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

puzzle_input = indata.read_infile('day15', use_testdata=False)
warehouse_map, instructions = puzzle_input.split('\n\n')
instructions = list(instructions.replace('\n', ''))
# wm = np.array([list(itm) for itm in warehouse_map.splitlines()], dtype=str)
wm = warehouse_large(warehouse_map)
current_pos: tuple[int, int] = get_start_pos(wm)

# Main game loop
running, finished, num_instructions, cnt = True, False, len(instructions), 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    if len(instructions) > 0:
        direction = instructions.pop(0)
        dy, dx = DIRECTIONS[direction]
        ny, nx = (current_pos[0] + dy, current_pos[1] + dx)
        if wm[(ny, nx)] == '#':
            continue
        if wm[(ny, nx)] == '.':
            wm[(ny, nx)], wm[current_pos] = wm[current_pos], '.'
            current_pos = (ny, nx)
        elif direction in '<>':
            current_pos = move_horizontal(wm, current_pos, DIRECTIONS[direction])
        else:
            current_pos = move_robot(wm, current_pos, DIRECTIONS[direction])
        cnt += 1
    else:
        finished = True

    # Clear the screen
    window.fill((0, 0, 0))
    color_map = {'#': (60, 60, 60), '@': (101, 255, 143), 'O': (255, 0, 0), '[': (249, 143, 8), ']': (243, 128, 8)}
    # Draw everything
    for ir, row in enumerate(wm):
        for ic, cell in enumerate(row):
            if cell in color_map:
                pygame.draw.rect(window, color_map[cell],
                                 (ic * cell_sz * 10, ir * cell_sz * 20, cell_sz * 10, 20))

    # Draw text
    font = pygame.font.Font(None, 36)
    text_col = (255, 255, 0) if not finished else (0, 255, 0)
    status_text = 'FINAL' if finished else 'CURRENT'
    window.blit(font.render(f'{status_text} SCORE: {get_score(wm, "[")}', True, text_col), (30, 1050))
    window.blit(font.render(f'Move {cnt} of {num_instructions}', True, text_col), (30, 1010))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()

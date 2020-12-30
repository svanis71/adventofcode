import pygame

from indata import read_lines

seatmap = [list(y) for y in read_lines('day11')]

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)

plupp_space, plupp_size = 10, 6
size = (len(seatmap[0]) * plupp_space, len(seatmap) * plupp_space + 30)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Advent of code day 11')

clock, done = pygame.time.Clock(), False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

occupied, adjacents = 0, [(0, -1), (-1, 0), (-1, -1), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
change_count, seatmap_copy = 0, [['.' for seat in row] for row in seatmap]

for y, row in enumerate(seatmap):
    for x, seat in enumerate(row):
        if seat == 'L':
            col = GREEN
        if seat == '#':
            col = RED
        if seat == '.':
            col = WHITE
        pygame.draw.circle(screen, col, [x * 5 + 2, y * 5 + 2], 5)
screen.fill(WHITE)
pygame.display.flip()

while True and not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for y, row in enumerate(seatmap):
        for x, seat in enumerate(row):
            if seat == '.':
                continue
            seat_empty, free_neighbours, occupied_neighbours = seatmap[y][x] == 'L', 0, 0
            for y_offset, x_offset in adjacents:
                cy, cx = y + y_offset, x + x_offset
                if 0 <= cx < len(row) and 0 <= cy < len(seatmap):
                    if seatmap[cy][cx] == 'L':
                        free_neighbours += 1
                    elif seatmap[cy][cx] == '#':
                        occupied_neighbours += 1
            if seat_empty and occupied_neighbours == 0 and seatmap_copy[y][x] != '#':
                seatmap_copy[y][x] = '#'
                change_count += 1
            elif occupied_neighbours >= 4 and seatmap_copy[y][x] != 'L':
                seatmap_copy[y][x] = 'L'
                change_count += 1
    seatmap = [[seat for seat in row] for row in seatmap_copy]

    screen.fill(WHITE)
    for y, row in enumerate(seatmap):
        for x, seat in enumerate(row):
            if seat == 'L':
                col = GREEN
            if seat == '#':
                col = RED
            if seat == '.':
                col == WHITE
            pygame.draw.circle(screen, col,
                               [int(x * plupp_space + plupp_space / 2), int(y * plupp_space + plupp_space / 2)],
                               int(plupp_size / 2))
    tp = sum([x.count("#") for x in seatmap])
    textsurface = myfont.render(f'{tp} occupied seats', False, BLACK)
    screen.blit(textsurface, (0, size[1] - 30))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
    if change_count == 0:
        break
    change_count = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(60)

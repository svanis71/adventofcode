import sys
import time

import pygame

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)

size = (1500, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Advent of code day 2')

clock, done = pygame.time.Clock(), False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen.fill(BLACK)
pygame.display.flip()

with open('../indata/day2.txt') as f:
    content = f.readlines()
lines = [x.strip() for x in content]
commands = [line.split(' ') for line in lines]
rotcommands = commands.copy()

boat = pygame.image.load("submarine.png")
boatrect = boat.get_rect()
# boatrect.top = 200
# boatrect.left = 100
x, y = 0, 0
speed = [2, 2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # if len(rotcommands) == 0:
    #     rotcommands = commands.copy()
    #     x, y = 0, 0

    # command = rotcommands.pop(0)
    # dir, steps = command[0], int(command[1])
    # if dir == 'forward':
    #     x += steps
    #     speed[0] = steps
    #     speed[1] = 0
    # elif dir == 'up':
    #     y -= steps
    #     speed[0] = 0
    #     speed[1] = -steps
    # elif dir == 'down':
    #     y += steps
    #     speed[0] = 0
    #     speed[1] = steps

    screen.fill(BLACK)
    # textsurface = myfont.render(f'dir: {dir} steps: {speed}', False, GREEN)
    # screen.blit(textsurface, (0, 30))
    textsurface = myfont.render(f'y: {y} x: {x}', False, GREEN)
    screen.blit(textsurface, (0, 60))
    screen.blit(boat, boatrect)
    x += 2
    y += 2
    boatrect.left += x
    boatrect.top += y
    time.sleep(0.2)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(60)

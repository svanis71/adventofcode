import pygame
from indata import read_list_of_strings

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

boat = pygame.image.load("submarine.png")
boatrect = boat.get_rect()
boatrect.top = 200
boatrect.left = 100
x, y = 0, 0
speed = [0, 0]

while not done:
    for command in commands:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            dir, steps = command[0], int(command[1])
            if dir == 'forward':
                x += steps
                speed[0] = steps
                speed[1] = 0
            elif dir == 'up':
                y -= steps
                speed[0] = 0
                speed[1] = -steps
            elif dir == 'down':
                y += steps
                speed[0] = 0
                speed[1] = steps

            boatrect.move(speed)
            screen.fill(BLACK)
            screen.blit(boat, boatrect)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # --- Limit to 60 frames per second
        clock.tick(60)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(60)

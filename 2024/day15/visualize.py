import sys

import pygame

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Boilerplate')

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw everything

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()
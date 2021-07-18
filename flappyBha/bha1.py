# Learning pygame by making Flappy Bird - Clear Code

# pygame.init()
# game code -> display_surface()
# gameloop to keep the window open
# Event loop -> player's input
# pygame.quit()

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([288,512]) #width height 576 1024
clock = pygame.time.Clock()

# to maintain the screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # Shutdown the code completely

    pygame.display.update()
    clock.tick(120) #fps
# Learning pygame by making Flappy Bird - Clear Code

# Display Surface - There can be only one; will always be shown
# (regular) surface - There can be as many as you need ; Is only displayed with attached to the display surface

import pygame
import sys

def draw_floor():
    # Two floors attached at side
    screen.blit(floor_surface,(floor_x_pos,450))
    screen.blit(floor_surface,(floor_x_pos+288,450))

pygame.init()

screen = pygame.display.set_mode([288,512]) #width height 576 1024
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert() # to convert to pygame
#bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_x_pos = 0

# to maintain the screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # Shutdown the code completely


    screen.blit(bg_surface,(0,0)) # Put one surface on another ; Origin TopLeft
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120) #fps
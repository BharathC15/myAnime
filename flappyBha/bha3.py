# Learning pygame by making Flappy Bird - Clear Code

# Display Surface - There can be only one; will always be shown
# (regular) surface - There can be as many as you need ; Is only displayed with attached to the display surface

# Rect can be used to check for collision; can be placed on different parts of the screen



import pygame
import sys

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,450))
    screen.blit(floor_surface,(floor_x_pos+288,450))

pygame.init()

screen = pygame.display.set_mode([288,512]) #width height 576 1024
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0


bg_surface = pygame.image.load('sprites/background-day.png').convert() # to convert to pygame

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_x_pos = 0

bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (50,512/2)) # put rectangle around it
# to maintain the screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # Shutdown the code completely

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0 #Disable all the gravity
                bird_movement -= 6


    screen.blit(bg_surface,(0,0)) # Put one surface on another ; Origin TopLeft
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)

    pygame.display.update()
    clock.tick(120) #fps
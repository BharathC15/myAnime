# Learning pygame by making Flappy Bird - Clear Code

# Rotating surfaces lowers their quality
# Solution
# 1. We have an original surface and a rotated one
# 2. The rotated surfaced is created from scratch from the original surface, hence we only rotate once

import pygame
import sys
import random

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,450))
    screen.blit(floor_surface,(floor_x_pos+288,450))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (350,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (350,random_pipe_pos - 300/2))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2.5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024/2: # if the pipe is in the bottom of the screen
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True) #xdirection False ydirection True
            screen.blit(flip_pipe,pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            #print('collision')
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >=450:
        #print('Floor ground collision')
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird,-bird_movement*3,1) #rotate - movement; 1-scale
    return new_bird

pygame.init()

screen = pygame.display.set_mode([288,512]) #width height 576 1024
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0
gameActive = True

bg_surface = pygame.image.load('sprites/background-day.png').convert() # to convert to pygame

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_x_pos = 0

bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert_alpha() # to blend in
bird_rect = bird_surface.get_rect(center = (50,512/2)) # put rectangle around it

pipe_surface = pygame.image.load('sprites/pipe-green.png').convert()

# put lots of rectangles using timers
pipe_list = []
SPAWNPIPE = pygame.USEREVENT #not triggered by the user
pygame.time.set_timer(SPAWNPIPE,1200)  #1.2sec

pipe_height =[200, 300, 400]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # Shutdown the code completely

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0 #Disable all the gravity
                bird_movement -= 6
        
        if event.type == pygame.KEYDOWN and gameActive == False:
            gameActive = True
            pipe_list.clear()
            bird_rect.center = (100/2,512/2)
            bird_movement = 0


        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())  # extent to list      
    screen.blit(bg_surface,(0,0)) # Put one surface on another ; Origin TopLeft
    
    if gameActive:

        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect)
        gameActive = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120) #fps
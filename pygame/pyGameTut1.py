import pygame

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 30 # Frames per second.

BLACK = (0, 0, 0) #RGB
WHITE = (255, 255, 255)
# RED = (255, 0, 0), GREEN = (0, 255, 0), BLUE = (0, 0, 255).

rect = pygame.Rect((0, 0), (32, 32)) # Position of the object, shape of the object

image = pygame.Surface((112, 32)) # Appearance of the object

image .fill(WHITE)

while True:
    clock.tick(FPS)  # to tick in the loop in the extact time interval
    for event in pygame.event.get():

        # Quit if x button is pressed in the window
        if event.type == pygame.QUIT:
            quit()
        
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect.move_ip(0, -10)
            elif event.key == pygame.K_s:
                rect.move_ip(0, 10)
            elif event.key == pygame.K_a:
                rect.move_ip(-10, 0)
            elif event.key == pygame.K_d:
                rect.move_ip(10, 0)
    
    screen.fill(BLACK)
    screen.blit(image, rect) # Copying image to another surface
    pygame.display.update() # Or pygame.display.flip()

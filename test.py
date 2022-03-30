import pygame
from sys import exit

snake_head_left = pygame.image.load('Resources/Snake/snake-head-left.png')
snake_head = snake_head_left
rect = snake_head.get_rect(bottomright = (60,60))

g_fps = 8
pygame.init()
screen = pygame.display.set_mode((320,320))


#clock fps
clock = pygame.time.Clock()

screen.fill((0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(snake_head,(40,40))
    #

    pygame.display.update()
    clock.tick(g_fps)

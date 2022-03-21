import pygame
from sys import exit
from random import randint

#inherit from sprite
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        snake_head = pygame.image.load('Resources/Snake/snake-head.png')
        snake_head = pygame.transform.rotozoom(snake_head,0,2)
        snake_body_1 = pygame.image.load('Resources/Snake/snake-body1.png')
        snake_body_2 = pygame.image.load('Resources/Snake/snake-body2.png')

        self.image = snake_head
        self.rect = self.image.get_rect(midbottom = (60,60))
#check movement 
#check eating food or snail tail

class Food():
    pass
#check if eaten and random spawn

#screen
pygame.init()
screen = pygame.display.set_mode((320,320))
pygame.display.set_caption('Snake Game')

#Groups
snake = pygame.sprite.GroupSingle()
snake.add(Snake())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    snake.draw(screen)
    
    
    pygame.display.update()

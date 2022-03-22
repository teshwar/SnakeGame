import pygame
from sys import exit
from random import randint

#inherit from sprite
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.y_pos = 0
        self.snake_head_left = pygame.image.load('Resources/Snake/snake-head-left.png')
        self.snake_head_right = pygame.image.load('Resources/Snake/snake-head-right.png')
        self.snake_head_up = pygame.image.load('Resources/Snake/snake-head-up.png')
        self.snake_head_down = pygame.image.load('Resources/Snake/snake-head-down.png')
        #self.snake_head = pygame.transform.rotozoom(self.snake_head,0,2)
        self.snake_body_1 = pygame.image.load('Resources/Snake/snake-body1.png')
        self.snake_body_2 = pygame.image.load('Resources/Snake/snake-body2.png')
        
        self.snake_head = self.snake_head_left
        self.image = self.snake_head
        self.rect = self.image.get_rect(midbottom = (60,60))

    def snake_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x_pos = -1
            self.y_pos = 0
            self.snake_head = self.snake_head_left
        
        elif keys[pygame.K_RIGHT]:
            self.x_pos = 1
            self.y_pos = 0
            self.snake_head = self.snake_head_right
        
        elif keys[pygame.K_UP]:
           self.y_pos = -1
           self.x_pos = 0
           self.snake_head = self.snake_head_up
        
        elif keys[pygame.K_DOWN]:
            self.y_pos = 1
            self.x_pos = 0
            self.snake_head = self.snake_head_down

    def snake_move(self):
        
        self.rect.x += self.x_pos
        if self.rect.x > 320: 
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = 320

        self.rect.y += self.y_pos
        if self.rect.y > 320:
            self.rect.y = 0
        elif self.rect.y < 0:
            self.rect.y = 320

        self.image = self.snake_head

    def eaten_food(self):
        pass

    def eaten_tail(self):
        pass

    def update(self):
        self.snake_input()
        self.snake_move()
#check movement 
#check eating food or snail tail

class Food():
    food = pygame.image.load('Resources/Food/food.png')

    pass
#check if eaten and random spawn

#screen
pygame.init()
screen = pygame.display.set_mode((320,320))
pygame.display.set_caption('Snake Game')

#clock fps
clock = pygame.time.Clock()

#Groups
snake = pygame.sprite.GroupSingle()
snake.add(Snake())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0,0,0))
    snake.draw(screen)
    snake.update()

    pygame.display.update()
    clock.tick(60)

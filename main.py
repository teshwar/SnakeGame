import pygame
from sys import exit
from random import randint

#inherit from sprite
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.y_pos = 0
        self.tail = []
        self.pos = 1
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
            self.x_pos = -10
            self.y_pos = 0
            self.pos = 1
            self.snake_head = self.snake_head_left
        
        elif keys[pygame.K_RIGHT]:
            self.x_pos = 10
            self.y_pos = 0
            self.pos = 3
            self.snake_head = self.snake_head_right
        
        elif keys[pygame.K_UP]:
           self.y_pos = -10
           self.x_pos = 0
           self.pos = 2
           self.snake_head = self.snake_head_up
        
        elif keys[pygame.K_DOWN]:
            self.y_pos = 10
            self.x_pos = 0
            self.pos = 4
            self.snake_head = self.snake_head_down

    def snake_move(self):    
        self.rect.x += self.x_pos
        if self.rect.x > 318: 
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = 319

        self.rect.y += self.y_pos
        if self.rect.y > 310:
            self.rect.y = 0
        elif self.rect.y < 1:
            self.rect.y = 319

        self.image = self.snake_head

    def eaten_food(self):
        self.tail_rect = self.snake_body_1.get_rect()
        self.tail_rect(midbottom = (60,60))

    def eaten_tail(self):
        pass

    def update(self):
        self.snake_input()
        self.snake_move()
        self.eaten_food()
#check movement 
#check eating food or snail tail

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        food = pygame.image.load('Resources/Food/food.png')

        self.image = food
        self.rect = self.image.get_rect(midbottom = (randint(0,310), randint(0,310)))
        #(randint(0,320), randint(0,320)
#check if eaten and random spawn

def collision_cake_eaten():
    if pygame.sprite.spritecollide(snake.sprite, food_group, True):
        return True
    else: 
        return False
#screen + score
score = 0
g_fps = 8
pygame.init()
screen = pygame.display.set_mode((320,320))
pygame.display.set_caption('Snake Game')

#clock fps
clock = pygame.time.Clock()

#Groups
snake = pygame.sprite.GroupSingle()
snake.add(Snake())

food_group = pygame.sprite.Group()
food_group.add(Food())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(f'Your score was :{score}')
            exit()
    screen.fill((0,0,0))

    if collision_cake_eaten():
        food_group.add(Food())
        score += 1
        if (score % 5 == 0):
            g_fps += 2

    food_group.draw(screen)
    #food.update()

    snake.draw(screen)
    snake.update()

    



    pygame.display.update()
    clock.tick(g_fps)

import pygame
from sys import exit
from random import randint

#inherit from sprite
class Snake(object):
    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.y_pos = 0
        self.tails = []
        
        self.pos = 1
        self.snake_head_left = pygame.image.load('Resources/Snake/snake-head-left.png')
        self.snake_head_right = pygame.image.load('Resources/Snake/snake-head-right.png')
        self.snake_head_up = pygame.image.load('Resources/Snake/snake-head-up.png')
        self.snake_head_down = pygame.image.load('Resources/Snake/snake-head-down.png')
        
        self.snake_body_1 = pygame.image.load('Resources/Snake/snake-body1.png')
        self.snake_body_2 = pygame.image.load('Resources/Snake/snake-body2.png')
        
        self.snake_head = self.snake_head_left
        #self.image = self.snake_head
        self.rect = self.snake_head.get_rect(bottomright = (60,60))
        self.tails.append(self.rect)

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
        for i, rect in enumerate(self.tails):
            rect.x += self.x_pos
            if rect.x > 318: 
                rect.x = 0
            elif rect.x < 0:
                rect.x = 319

            rect.y += self.y_pos
            if rect.y > 310:
                rect.y = 0
            elif rect.y < 1:
                rect.y = 319

        #self.image = self.snake_head

    def eaten_food(self):
        #self.tail_rect = self.snake_body_1.get_rect()
        #self.tail_rect(midbottom = (60,60))
        tail_image = self.snake_body_1
        pos = len(self.tails)-1
        x_pos = self.tails[pos].x 
        y_pos = self.tails[pos].y 
        tail_rect = tail_image.get_rect(bottomright = (60,60))

        self.tails.append(tail_rect)
        pass

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

        snake.sprite.eaten_food()
        

    food_group.draw(screen)
    #food.update()

    snake.draw(screen)
    snake.update()

    



    pygame.display.update()
    clock.tick(g_fps)

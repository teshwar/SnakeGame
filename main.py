import pygame
from sys import exit
from random import randint
import itertools

#inherit from sprite
class Snake(pygame.sprite.Sprite):
    tails = []
    def __init__(self,head,x_pos, y_pos):
        super().__init__()
        self.x_pos = 0
        self.y_pos = 0
        self.pos = 1

        #loads head images
         
        self.snake_head_left = pygame.image.load('Resources/Snake/snake-head-left.png')
        self.snake_head_right = pygame.image.load('Resources/Snake/snake-head-right.png')
        self.snake_head_up = pygame.image.load('Resources/Snake/snake-head-up.png')
        self.snake_head_down = pygame.image.load('Resources/Snake/snake-head-down.png')
        
        #loads snake images
        self.snake_body_1 = pygame.image.load('Resources/Snake/snake-body1.png')
        self.snake_body_2 = pygame.image.load('Resources/Snake/snake-body2.png')
        
        #default head toward left
        if head:
            self.pos = 1
            self.snake_head = self.snake_head_left
            self.image = self.snake_head
            self.rect = self.image.get_rect(bottomright = (x_pos,y_pos))
        else:
            self.image = self.snake_body_1

            #adding last bodypart depending on head location
            #if self.pos == 1: #left
            self.rect = self.image.get_rect(bottomleft = (x_pos+1,y_pos+1))
            #elif self.pos == 2 : #up

       #self.rect = self.image.get_rect(bottomright = (x_pos,y_pos))
        Snake.tails.append(self.rect) #append snake head first time, then body the rest
       

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
        for i, rect in enumerate(Snake.tails):
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

        if i == 0 :
            if  pygame.Rect.collidelist(rect,Snake.tails) == -1:
                self.image = self.snake_head
                game_over = True

        

    def eaten_food(self):
        last_bp = Snake.tails[len(Snake.tails)-1]
        x = last_bp.x
        y = last_bp.y
        snake.add(Snake(False,x,y))
        

    def update(self):
        self.snake_input()
        self.snake_move()
        #self.eaten_food()
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
    if pygame.sprite.spritecollide(snake_h, food_group, True):
        return True
    else:
        return False
#screen + score
global game_continue
game_over = False
score = 0
g_fps = 8
pygame.init()
screen = pygame.display.set_mode((320,320))
pygame.display.set_caption('Snake Game')

#clock fps
clock = pygame.time.Clock()

#Groups
snake = pygame.sprite.Group()
snake_h = Snake(True,60,60)
snake.add(snake_h)


food_group = pygame.sprite.GroupSingle()
food_group.add(Food())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or game_over:
            pygame.quit()
            print(f'Your score was :{score}')
            exit()
    screen.fill((0,0,0))

    if collision_cake_eaten():
        food_group.add(Food())
        snake_h.eaten_food()
        score += 1
        if (score % 5 == 0):
            g_fps += 2

    food_group.draw(screen)
    #food.update()

    snake.draw(screen)
    snake.update()

    



    pygame.display.update()
    clock.tick(g_fps)

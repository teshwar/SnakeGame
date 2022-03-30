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
        
        
        self.dir = 1
        self.snake_head_left = pygame.image.load('Resources/Snake/snake-head-left.png')
        self.snake_head_right = pygame.image.load('Resources/Snake/snake-head-right.png')
        self.snake_head_up = pygame.image.load('Resources/Snake/snake-head-up.png')
        self.snake_head_down = pygame.image.load('Resources/Snake/snake-head-down.png')
        
        self.snake_body_1 = pygame.image.load('Resources/Snake/snake-body1.png')
        self.snake_body_2 = pygame.image.load('Resources/Snake/snake-body2.png')
        
        self.snake_head = self.snake_head_left
        #self.image = self.snake_head
        self.rect = self.snake_head.get_rect(bottomright = (60,60))
        self.h_pos = (self.rect.x, self.rect.y)
        self.tails.append(self.rect)

    def snake_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x_pos = -10
            self.y_pos = 0
            self.dir = 1
            self.snake_head = self.snake_head_left
        
        elif keys[pygame.K_RIGHT]:
            self.x_pos = 10
            self.y_pos = 0
            self.dir = 3
            self.snake_head = self.snake_head_right
        
        elif keys[pygame.K_UP]:
           self.y_pos = -10
           self.x_pos = 0
           self.dir = 2
           self.snake_head = self.snake_head_up
        
        elif keys[pygame.K_DOWN]:
            self.y_pos = 10
            self.x_pos = 0
            self.dir = 4
            self.snake_head = self.snake_head_down

    def snake_move(self):    
        for i, rect in enumerate(self.tails):

            if i == 0: 
                self.h_pos = (rect.x, rect.y)
            
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

    def draw(self):
        for i, rect in enumerate(self.tails):
            if i == 0: 
                screen.blit(self.snake_head,self.h_pos)
            else:
                screen.blit(self.snake_body_1, (rect.x,rect.y))
            

    def update(self):
        self.snake_input()
        self.snake_move()
        self.eaten_food()
        self.draw()
#check movement 
#check eating food or snail tail

class Food(object):
    def __init__(self):
        super().__init__()
        food = pygame.image.load('Resources/Food/food.png')

        self.image = food
        self.rect = self.image.get_rect(midbottom = (randint(0,310), randint(0,310)))
        self.f_pos = (self.rect.x,self.rect.y)
    
    def update(self):
        self.draw()
    
    def draw(self):
        screen.blit(self.image,self.f_pos)
        #(randint(0,320), randint(0,320)
#check if eaten and random spawn

def collision_cake_eaten():
    if snake.h_pos == food.f_pos:
        return True
    else: 
        return False

#screen + score
global snake, food, screen
score = 0
g_fps = 8
pygame.init()
screen = pygame.display.set_mode((320,320))
refresh_s = pygame.display.set_mode((320,320))
pygame.display.set_caption('Snake Game')

#clock fps
clock = pygame.time.Clock()

#Groups
snake = Snake()
food = Food()

empty = pygame.Color(255,255,255,0)
#mask = pygame.Surface((180,100),pygame.SRCALPHA)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(f'Your score was :{score}')
            exit()

    #mask.fill
    #mask.set_apha(255)
   

    if collision_cake_eaten():
        food = Food()
        score += 1
        if (score % 5 == 0):
            g_fps += 2

        snake.sprite.eaten_food()
        
    screen.fill(empty)
    food.update()
    snake.update()
    
    #screen.blit(mask,(0,0),special_flags=(pygame.BLEND_RGBA_ADD))
    pygame.display.update()
    clock.tick(g_fps)

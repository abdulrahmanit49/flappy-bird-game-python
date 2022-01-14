import pygame
import random
from pygame import display
pygame.init()
SCREEN = pygame.display.set_mode((625,499)) 
BACKGROUND_IMAGE = pygame.image.load('1.jpg')
HARRY_IMAGE = pygame.image.load('poo.png')
harry_x = 10  
harry_y = 10
harry_y_change = 0

def display_bird(x, y):
    SCREEN.blit(HARRY_IMAGE, (x, y))

OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = random.randint(150,500)
OBSTACLE_COLOR = (153,101,21)
OBSTACE_X_CHANGE = -0.5
obstacle_x = 400

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_y = height + 200  
    bottom_height = 635 - bottom_y
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, pygame.Rect(obstacle_x, bottom_y, OBSTACLE_WIDTH, bottom_height))

def collision_detection (obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
    return False


score=0
scoreFont=pygame.font.Font('LUMOS.TTF',32)
def score_display(score):
    display=scoreFont.render(f"Score:{score}",True,(137,0,0))
    SCREEN.blit(display,(10,10))

startFont=pygame.font.Font('LUMOS.TTF',32)
def start():
    display = startFont.render(f"HIT THE SPACE BAR TO START", True, (137,0,0))
    SCREEN.blit(display, (50 , 100))
    pygame.display.update()
score_list=[0]
game_over_font1=pygame.font.Font('LUMOS.TTF',64)
game_over_font2=pygame.font.Font('LUMOS.TTF',32)
def game_over():
    display1=game_over_font1.render(f"HOW PATHETIC",True,(250, 249, 246))
    SCREEN.blit(display1,(50, 250))
    display2=game_over_font2.render(f"Score:{score}",True,(218,165,32))
    SCREEN.blit(display2,(200, 350))

running = True
waiting = True
collision = False

while running:

    SCREEN.fill((0, 0, 0))
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    while waiting:
        if collision:
            game_over()
            start()
        else:
            start()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    harry_y = 300
                    obstacle_x = 500
                    waiting = False

            if event.type == pygame.QUIT:
                waiting = False
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                harry_y_change = -0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                 harry_y_change = 0.5
    harry_y +=  harry_y_change
    if harry_y <= 0:
        harry_y = 0
    if harry_y >= 450:
        harry_y = 450
    obstacle_x += OBSTACE_X_CHANGE 
    collision=collision_detection(obstacle_x,OBSTACLE_HEIGHT,harry_y,OBSTACLE_HEIGHT+200)
    if collision==True:
        waiting=True 
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(100, 300)
        score += 1
    display_obstacle(OBSTACLE_HEIGHT)
    display_bird(harry_x, harry_y)
    score_display(score)

    pygame.display.update()

pygame.quit()
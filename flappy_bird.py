import pygame
import random

def draw_floor():
    screen.blit(floor, (floor_x,90))
    screen.blit(floor, (floor_x+ 450,90))
pygame.init()

#screen size
WINDOW_W = 400
WINDOW_H = 650
WINDOW_SIZE = (WINDOW_W,WINDOW_H)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird")

#background
bk_img = pygame.image.load('background.png')
bk_img = pygame.transform.scale(bk_img , (400,650))

#floor
floor = pygame.image.load('floor.png')
floor = pygame.transform.scale(floor, (400,90))
floor_x = 800
#floor2
floor2 = pygame.image.load('floor2.png')
floor2 = pygame.transform.scale(floor2,(800,90))
#bird
bird_img = pygame.image.load('bird1.png')
bird_x = 50
bird_y = 300
bird_y_change = 0
#clock
clock = pygame.time.Clock()
def display_bird(x, y):
    screen.blit(bird_img, (x, y))

#loop
play = True

while play == True:
    clock.tick(130)

    screen.fill((0, 0, 0))
    screen.blit(bk_img,(0, 0))
    screen.blit(floor, (0,560))
    screen.blit(floor2, (floor_x, 560))
    draw_floor()
    if floor_x < -450:
        floor_x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False   
    
    pygame.display.update()

pygame.quit()
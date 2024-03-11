
# libraries
import pygame
import sys
import time

# initialise pygame
pygame.init()

# define colours
BLUE = pygame.Color(15, 186, 189)
GREEN = pygame.Color(33, 103, 94)
YELLOW = pygame.Color(251, 189, 60)
RED = pygame.Color(188, 19, 31)
PURPLE = pygame.Color(140, 16, 68)

# main screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
 
# create grid for screen
def getGrid():
    for x in range(0, SCREEN_WIDTH)

def draw_screen():
    screen.fill(YELLOW)

# snake

x1 = SCREEN_WIDTH/2
y1 = SCREEN_HEIGHT/2

snake_head = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

run = True
while run:
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                x1_change = 0
                y1_change = -snake_head
            elif event.key == pygame.K_s:
                x1_change = 0
                y1_change = snake_head
            elif event.key == pygame.K_a:
                x1_change = -snake_head
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = snake_head
                y1_change = 0
    if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
        run = False

    x1 += x1_change
    y1 += y1_change

pygame.draw.rect(screen, RED, [x1, y1, 10, 10])

pygame.display.update()

clock.tick(snake_speed)
time.sleep(2)

pygame.quit()

# Skeleton Code
# Lucy Allen
# Version 1

# Python libaries
import pygame
import time
# initalise pygame
pygame.init()
# set time
current_time = time.time()
# making the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

run = True
while run:
    screen.fill((000))

fps = pygame.time.Clock()
# leaving the game
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    pygame.display.update()

pygame.quit()

# snake position
snake_position = [100, 50]
# snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50]]
# Import libraries
import pygame
import time
import random

# Initialise Game
pygame.init()

# Define colours
BLUE = pygame.Color(15, 186, 189)
GREEN = pygame.Color(33, 103, 94)
YELLOW = pygame.Color(251, 189, 60)
RED = pygame.Color(188, 19, 31)
PURPLE = pygame.Color(140, 16, 68)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)


# Load background image
BG = pygame.image.load('green_bg.jpg')

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# FPS
fps = pygame.time.Clock()

# Snake speed
snake_speed = 20

# Snake position and body
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Fruit position
fruit_position = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                  random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]

# Directions
direction = 'RIGHT'
change_to = direction

# Score
score = 0

# pause
paused = False


# Start menu
def mainMenu():
    pygame.display.set_caption("Main Menu")
    menu = True
    while menu:
        screen.fill(BLACK)
        screen.blit(BG, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
        font = pygame.font.SysFont('copperplate gothic', 50)
        text = font.render('Press Enter to start', True, WHITE)
        screen.blit(text, (50, 50))
        pygame.display.update()
        fps.tick(15)

# Pause the game
def paused():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False


# Game Over
def game_over():
    global score
    font = pygame.font.SysFont('copperplate gothic', 50)
    game_over_surface = font.render('Your score is: '
                                    + str(score), True, PURPLE)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


# Main game loop
def game():
    global direction, change_to, snake_position, \
        snake_body, score, fruit_position
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused()
                if event.key == pygame.K_w:
                    change_to = 'UP'
                elif event.key == pygame.K_s:
                    change_to = 'DOWN'
                elif event.key == pygame.K_a:
                    change_to = 'LEFT'
                elif event.key == pygame.K_d:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and \
                snake_position[1] == fruit_position[1]:
            score += 10
            fruit_position = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                              random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        else:
            snake_body.pop()

        screen.fill(YELLOW)

        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect
                             (pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, RED, pygame.Rect
                         (fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > SCREEN_WIDTH - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > SCREEN_HEIGHT - 10:
            game_over()
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # Display score
        font = pygame.font.SysFont('copperplate gothic', 24)
        score_surface = font.render('Score: ' + str(score), True, PURPLE)
        score_rect = score_surface.get_rect()
        score_rect.topleft = (10, 10)
        screen.blit(score_surface, score_rect)
        
        if paused:
            pygame.display.update()
            fps.tick(snake_speed)
        


# Main game loop
def main():
    global direction, change_to, snake_position, snake_body, \
        score, fruit_position

    mainMenu()
    game()


if __name__ == "__main__":
    main()

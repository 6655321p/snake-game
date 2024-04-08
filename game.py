# Import libraries
import pygame
import time
import random

# Define colours
BLUE = pygame.Color(15, 186, 189)
GREEN = pygame.Color(33, 103, 94)
YELLOW = pygame.Color(251, 189, 60)
RED = pygame.Color(188, 19, 31)
PURPLE = pygame.Color(140, 16, 68)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

# Load background image
BG = pygame.image.load("green_bg.jpg")

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GAME_SPEED = 20


class Game:

    def __init__(self) -> None:

        # Initialise Game
        pygame.init()

        # Initialize window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        # FPS
        self.fps = pygame.time.Clock()

        # Snake position and body
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

        # Fruit position
        self.fruit_position = [
            random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
            random.randrange(1, (SCREEN_HEIGHT // 10)) * 10,
        ]

        # Directions
        self.snake_direction = "RIGHT"
        self.change_snake_direction_to = self.snake_direction

        # Score
        self.game_score = 0

        self.is_game_paused = False

        self.main_loop()

    # Pause the game
    def pause_game(self):
        self.is_game_paused = True

    def display_options_loop(self):
        return

    # Game Over
    def on_game_over(self):
        font = pygame.font.SysFont("copperplate gothic", 50)
        game_over_surface = font.render(
            "Your score is: " + str(self.game_score), True, PURPLE
        )
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    def on_key_event(self, event):

        if event.key == pygame.K_ESCAPE:
            self.pause_game()

        if event.key == pygame.K_w:
            self.change_snake_direction_to = "UP"
        elif event.key == pygame.K_s:
            self.change_snake_direction_to = "DOWN"
        elif event.key == pygame.K_a:
            self.change_snake_direction_to = "LEFT"
        elif event.key == pygame.K_d:
            self.change_snake_direction_to = "RIGHT"
        elif event.key == pygame.K_SPACE:
            self.is_game_paused = False

    def gameplay_loop(self):
        if (
            self.change_snake_direction_to == "UP"
            and self.snake_direction != "DOWN"
        ):
            self.snake_direction = "UP"
        if (
            self.change_snake_direction_to == "DOWN"
            and self.snake_direction != "UP"
        ):
            self.snake_direction = "DOWN"
        if (
            self.change_snake_direction_to == "LEFT"
            and self.snake_direction != "RIGHT"
        ):
            self.snake_direction = "LEFT"
        if (
            self.change_snake_direction_to == "RIGHT"
            and self.snake_direction != "LEFT"
        ):
            self.snake_direction = "RIGHT"

        if self.snake_direction == "UP":
            self.snake_position[1] -= 10
        if self.snake_direction == "DOWN":
            self.snake_position[1] += 10
        if self.snake_direction == "LEFT":
            self.snake_position[0] -= 10
        if self.snake_direction == "RIGHT":
            self.snake_position[0] += 10

        self.snake_body.insert(0, list(self.snake_position))
        if (
            self.snake_position[0] == self.fruit_position[0]
            and self.snake_position[1] == self.fruit_position[1]
        ):
            self.game_score += 10
            self.fruit_position = [
                random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                random.randrange(1, (SCREEN_HEIGHT // 10)) * 10,
            ]
        else:
            self.snake_body.pop()

        self.screen.fill(YELLOW)

        for pos in self.snake_body:
            pygame.draw.rect(
                self.screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10)
            )
        pygame.draw.rect(
            self.screen,
            RED,
            pygame.Rect(self.fruit_position[0], self.fruit_position[1], 10, 10),
        )

        if self.snake_position[0] < 0 or self.snake_position[0] > SCREEN_WIDTH - 10:
            self.on_game_over()
        if (
            self.snake_position[1] < 0
            or self.snake_position[1] > SCREEN_HEIGHT - 10
        ):
            self.on_game_over()
        for block in self.snake_body[1:]:
            if (
                self.snake_position[0] == block[0]
                and self.snake_position[1] == block[1]
            ):
                self.on_game_over()

        # Display score
        font = pygame.font.SysFont("copperplate gothic", 24)
        score_surface = font.render("Score: " + str(self.game_score), True, PURPLE)
        score_rect = score_surface.get_rect()
        score_rect.topleft = (10, 10)
        self.screen.blit(score_surface, score_rect)

    # Main game loop
    def main_loop(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.on_key_event(event)

            if self.is_game_paused:
                self.display_options_loop()

            else:
                self.gameplay_loop()

            pygame.display.update()
            self.fps.tick(GAME_SPEED)
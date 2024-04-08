# Import libraries
import pygame
import random
import json

from screeninfo import get_monitors

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
monitors = get_monitors()
monitor = monitors[0]
SCREEN_WIDTH = monitor.width
SCREEN_HEIGHT = monitor.height

# MIDDLE OF THE SCREEN
SCREEN_MIDDLE = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

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
        self.is_game_over = False

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

        # Game status
        self.is_game_paused = False

        # Mouse inside buttons
        self.is_mouse_inside_exit = False
        self.is_mouse_inside_resume = False
        self.is_mouse_inside_new_game = False

        self.main_loop()

    # Pause the game
    def pause_game(self):
        self.is_game_paused = True

    def is_mouse_inside(self, mouse_pos, object_pos, object_size_x=40, object_size_y=30):

        is_mouse_inside = False

        if mouse_pos[0] < object_pos[0] + object_size_x and mouse_pos[0] > object_pos[0] - object_size_x:
            if mouse_pos[1] < object_pos[1] + object_size_y and mouse_pos[1] > object_pos[1] - object_size_y:
                is_mouse_inside = True

        return is_mouse_inside

    def display_options_loop(self):
        mouse_pos = self.mouse_pos

        screen_pos_adition_y = SCREEN_MIDDLE[1]/4.5

        font = pygame.font.SysFont("copperplate gothic", 40)

        exit_surface = font.render("Exit", True, RED)
        exit_button_pos = (SCREEN_MIDDLE[0],
                            SCREEN_MIDDLE[1] + (screen_pos_adition_y * 8))

        self.is_mouse_inside_exit = self.is_mouse_inside(mouse_pos, exit_button_pos)
        if self.is_mouse_inside_exit:
            exit_surface = font.render("Exit", True, WHITE)

        exit_rect = exit_surface.get_rect()
        exit_rect.midtop = exit_button_pos
        self.screen.blit(exit_surface, exit_rect)

        if not self.is_game_over:
            resume_surface = font.render("Resume", True, RED)
            resume_button_pos = (SCREEN_MIDDLE[0],
                                SCREEN_MIDDLE[1] + (screen_pos_adition_y * 2))

            self.is_mouse_inside_resume = self.is_mouse_inside(mouse_pos,
                                                               resume_button_pos,
                                                               object_size_x=80)
            if self.is_mouse_inside_resume:
                resume_surface = font.render("Resume", True, WHITE)

            resume_rect = resume_surface.get_rect()
            resume_rect.midtop = resume_button_pos
            self.screen.blit(resume_surface, resume_rect)

        if self.is_game_over:
            new_game_surface = font.render("New Game", True, RED)
            new_game_button_pos = (SCREEN_MIDDLE[0],
                                SCREEN_MIDDLE[1] + (screen_pos_adition_y * 2))

            self.is_mouse_inside_new_game = self.is_mouse_inside(mouse_pos,
                                                               new_game_button_pos,
                                                               object_size_x=100)
            if self.is_mouse_inside_new_game:
                new_game_surface = font.render("New Game", True, WHITE)

            new_game_rect = new_game_surface.get_rect()
            new_game_rect.midtop = new_game_button_pos
            self.screen.blit(new_game_surface, new_game_rect)

    # Game Over
    def on_game_over(self):
        self.is_game_over = True
        font = pygame.font.SysFont("copperplate gothic", 40)
        game_over_surface = font.render(
            "Game Over!, Your score is: " + str(self.game_score), True, PURPLE
        )
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = SCREEN_MIDDLE
        self.screen.blit(game_over_surface, game_over_rect)
        self.pause_game()

    def start_new_game(self):

        # Snake position and body
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.is_game_over = False

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

        self.is_game_over = False
        self.is_game_paused = False
        self.is_mouse_inside_new_game = False

    def on_mouse_click_event(self, event):
        if self.is_game_paused:
            if self.is_mouse_inside_exit:
                exit()
            if self.is_mouse_inside_resume:
                self.is_game_paused = False
            if self.is_mouse_inside_new_game:
                self.start_new_game()

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
        if self.change_snake_direction_to == "UP" and self.snake_direction != "DOWN":
            self.snake_direction = "UP"
        if self.change_snake_direction_to == "DOWN" and self.snake_direction != "UP":
            self.snake_direction = "DOWN"
        if self.change_snake_direction_to == "LEFT" and self.snake_direction != "RIGHT":
            self.snake_direction = "LEFT"
        if self.change_snake_direction_to == "RIGHT" and self.snake_direction != "LEFT":
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
            pygame.draw.rect(self.screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(
            self.screen,
            RED,
            pygame.Rect(self.fruit_position[0], self.fruit_position[1], 10, 10),
        )

        if self.snake_position[0] < 0 or self.snake_position[0] > SCREEN_WIDTH - 10:
            self.on_game_over()
        if self.snake_position[1] < 0 or self.snake_position[1] > SCREEN_HEIGHT - 10:
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

            self.mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.on_key_event(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_mouse_click_event(event)

            if self.is_game_paused:
                self.display_options_loop()

            else:
                self.gameplay_loop()

            pygame.display.update()
            self.fps.tick(GAME_SPEED)

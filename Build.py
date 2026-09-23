import pygame
import sys

# --- Constants ---
WIDTH, HEIGHT = 900, 600
FPS = 60
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 110
BALL_SIZE = 18
PADDLE_SPEED = 6
BALL_SPEED_X = 5
BALL_SPEED_Y = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)

pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# --- Game Objects ---
left_paddle = pygame.Rect(40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

left_score = 0
right_score = 0
font = pygame.font.Font(None, 60)


def reset_ball(direction):
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x = direction * BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y
    
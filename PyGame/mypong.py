
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# color variable, look for RGB codes
PURPLE = (128, 0, 128)
GREEN  = (0, 255, 0)
PADDLE_SPEED = 6
BALL_SPEED_X=5
BALL_SPEED_Y=4

PADDLE_WIDTH=10
PADDLE_HEIGHT=110
BALL_SIZE=18

left_paddle = pygame.Rect( 
    40,
    HEIGHT // 2 - PADDLE_HEIGHT // 2,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
)

right_paddle = pygame.Rect(
    WIDTH - 40 - PADDLE_WIDTH,
    HEIGHT // 2 - PADDLE_HEIGHT // 2,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
)
ball = pygame.Rect(
    WIDTH // 2 - BALL_SIZE // 2,
    HEIGHT // 2 - BALL_SIZE // 2,
    BALL_SIZE,
    BALL_SIZE,
)


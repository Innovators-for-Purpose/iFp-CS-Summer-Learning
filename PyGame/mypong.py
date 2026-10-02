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

def reset_ball (direction):
    ball.center = (WIDTH // 2, HEIGHT // 2)

reset_ball(1)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

def reset_ball(direction):
    global ball_speed_x, ball_speed_y

    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x = direction * BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

def main (window):
    clock = pygame.time.Clock()

    while True:
        #game code
        clock.tick (60)
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong Game")
    main(window)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

keys = pygame.key.get_pressed()
if keys[pygame.K_w] and left_paddle.top > 0:
    left_paddle.y -= PADDLE_SPEED
if keys [pygame.K_s] and left_paddle.bottom < HEIGHT:
    left_paddle.y += PADDLE_SPEED

ball.x += ball_speed_x
ball.y += ball_speed_y
if ball.top <= 0 or ball.bottom >= HEIGHT:
    ball_speed_y *= -1

if ball.colliderect(left_paddle) and ball_speed_x < 0:
    ball_speed_x *= -1

offset = (ball.centery - left_paddle.centery) / (PADDLE_HEIGHT / 2)
ball_speed_y = offset * 6

left_score = 0
right_score = 0

if ball.left <= 0:
    right_score += 1
    reset_ball(1)
elif ball.right >= WIDTH:
    left_score += 1
    reset_ball(-1)

window.fill(BLACK)

for y in range (0, HEIGHT, 30):
    pygame.draw.rect(window, PURPLE, (WIDTH // 2 - 2, y, 4, 10))
pygame.draw.rect(window, GREEN, left_paddle)
pygame.draw.rect(window, GREEN, right_paddle)
pygame.draw.ellipse(window, GREEN, ball)

score_text = font.render(f"{left_score} {right_score}", True, GREEN)
window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
pygame.display.flip()
clock.tick(FPS)

import pygame
import sys

WIDTH, HEIGHT = 900, 600
FPS = 60
def reset_ball(direction):
    pass
def main(window):
    while TRUE:
        pass
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)
    pygame.quit()


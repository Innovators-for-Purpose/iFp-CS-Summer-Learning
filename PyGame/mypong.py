import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 800, 600

window =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_SPEED = 10
BALL_SPEED_X = 8
BALL_SPEED_Y = 8
RED = (150, 0, 132) #RN purple
GREEN = (0, 255, 0)
BLUE = (0, 0, 144) #RN dark blue

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 110
BALL_SIZE = 18

left_paddle = pygame.Rect(40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
font = pygame.font.Font(size=74)

# ---Game variables---


ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

def reset_ball(direction):
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x = direction * BALL_SPEED_X
    ball_speed_y = direction *BALL_SPEED_Y

left_score = 0
right_score = 0

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    if keys[pygame.K_o] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_l] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

    if ball.colliderect(left_paddle) and ball_speed_x < 0:
        ball_speed_x *= -1
        offset = (ball.centery - left_paddle.centery) / (PADDLE_HEIGHT / 2) 
        ball_speed_y = offset * 6

    if ball.colliderect(right_paddle) and ball_speed_x > 0:
            ball_speed_x *= -1
            offset = (ball.centery - right_paddle.centery) / (PADDLE_HEIGHT / 2) 
            ball_speed_y = offset * 6

  


    if ball.left <= 0:
        right_score += 1
        reset_ball(1)
    elif ball.right >= WIDTH:
        left_score += 1
        reset_ball(-1)

    window.fill(RED)

    for y in range(0, HEIGHT, 20):
         pygame.draw.line(window, WHITE, (WIDTH // 2 - 2, y), (WIDTH // 2 + 2, y), width=1)

    pygame.draw.rect(window, BLUE, left_paddle)
    pygame.draw.rect(window, BLUE, right_paddle)
    pygame.draw.ellipse(window, WHITE, ball)

    score_text = font.render(f"{left_score} {right_score}", True, WHITE)
    window.blit(score_text, (WIDTH // 2 - score_text.get_width()// 2, 20))

    pygame.display.flip()
    clock.tick(FPS)

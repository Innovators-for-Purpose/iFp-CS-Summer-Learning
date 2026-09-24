import pygame
import sys


#Variables
WIDTH, HEIGHT = 900, 600
FPS = 60
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
PADDLE_SPEED = 6
BALL_SPEED_X = 5
BALL_SPEED_Y = 4

BLUE = (48, 105, 152)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
MAROON = (128, 0, 0)
ROSE = (255, 120, 127)

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 110
BALL_SIZE = 18

left_score = 0
right_score = 0

pygame.init()
pygame.display.set_caption("My Pong")
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


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


#MAIN FUNCTION!!!!


while True:
    #codeeeeee
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:right_paddle.y += PADDLE_SPEED

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


    window.fill(WHITE)

    for y in range(0, HEIGHT, 20):
        pygame.draw.rect(window, MAROON, (WIDTH // 2 - 2, y, 4, 10))


    pygame.draw.rect(window, BLUE, left_paddle)
    pygame.draw.rect(window, ROSE, right_paddle)
    pygame.draw.ellipse(window, ORANGE, ball)

    score_text = font.render(f"{left_score}  {right_score}", True, MAROON)
    window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()
    clock.tick(FPS)



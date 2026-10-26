import pygame
import sys

WIDTH, HEIGHT = 1200, 800
FPS = 90
Black = (0, 0, 0)
Orange = (255, 165, 0)
Paddle_Speed = 9
Ball_Speed_X = 7.5
Ball_Speed_Y = 7.5
Paddle_Width = 11
Paddle_Height = 72
Ball_Size = 15

pygame.init()
pygame.display.set_caption("Pong")
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()




Left_Paddle = pygame.Rect(
20,
HEIGHT // 2 - Paddle_Height // 2,
Paddle_Width,
Paddle_Height
)

Right_Paddle = pygame.Rect(
WIDTH - 20 - Paddle_Width,
HEIGHT // 2 - Paddle_Height // 2,
Paddle_Width,
Paddle_Height
)

ball = pygame.Rect(
WIDTH // 2 - Ball_Size // 2,
HEIGHT // 2 - Ball_Size // 2,
Ball_Size,
Ball_Size
)


ball_speed_x = Ball_Speed_X
ball_speed_y = Ball_Speed_Y


Left_Score = 0
Right_Score = 0
font = pygame.font.Font(None, 60)


def reset_ball(direction):
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x = direction * Ball_Speed_X
    ball_speed_y = Ball_Speed_Y


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and Left_Paddle.top > 0:
        Left_Paddle.y -= Paddle_Speed
    if keys [pygame.K_s] and Left_Paddle.bottom < HEIGHT:
        Left_Paddle.y += Paddle_Speed
    if keys [pygame.K_UP] and Right_Paddle.top > 0:
        Right_Paddle.y -= Paddle_Speed
    if keys [pygame.K_DOWN] and Right_Paddle.bottom < HEIGHT:
        Right_Paddle.y += Paddle_Speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(Left_Paddle) and ball_speed_x < 0:
        ball_speed_x *= -1
        offset = (ball.centery - Left_Paddle.centery) / (Paddle_Height / 2)
        ball_speed_y = offset * 6

    if ball.colliderect(Right_Paddle) and ball_speed_x > 0:
            ball_speed_x *= -1
            offset = (ball.centery - Right_Paddle.centery) / (Paddle_Height / 2)
            ball_speed_y = offset * 6

    if ball.left <= 0:
        Right_Score += 1
        reset_ball(1)
    elif ball.right >= WIDTH:
        Left_Score += 1
        reset_ball(-1)


    
    window.fill(Black)

    for y in range(0, HEIGHT, 20):
        pygame.draw.rect(window, Orange, (WIDTH // 2 - 2, y, 4, 10))
    pygame.draw.rect(window, Orange, Left_Paddle)
    pygame.draw.rect(window, Orange, Right_Paddle)
    pygame.draw.ellipse(window, Orange, ball)

    score_text = font.render(f"{Left_Score} {Right_Score}", True, Orange)
    window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()
    clock.tick(FPS)

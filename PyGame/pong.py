import pygame
import sys

# --- Constants ---
WIDTH, HEIGHT = 900, 600
FPS = 120
PADDLE_WIDTH = 150
PADDLE_HEIGHT = 110
PADDLE_IMAGE = pygame.transform.scale(
    pygame.image.load("PyGame/images/rectangle.png"),
    (PADDLE_WIDTH, PADDLE_HEIGHT),
)
BALL_SIZE = 20
PADDLE_SPEED = 12
BALL_SPEED_X = 10
BALL_SPEED_Y = 8z
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)

pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# --- Game Objects ---
left_paddle = PADDLE_IMAGE.get_rect(topleft=(40, HEIGHT // 2 - PADDLE_HEIGHT // 2))
right_paddle = PADDLE_IMAGE.get_rect(topright=(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2))
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


# --- Main game loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions with top/bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball hits paddles
    if ball.colliderect(left_paddle) and ball_speed_x < 0:
        ball_speed_x *= -1
        offset = (ball.centery - left_paddle.centery) / (PADDLE_HEIGHT / 2)
        ball_speed_y = offset * 6
    if ball.colliderect(right_paddle) and ball_speed_x > 0:
        ball_speed_x *= -1
        offset = (ball.centery - right_paddle.centery) / (PADDLE_HEIGHT / 2)
        ball_speed_y = offset * 6

    # Scoring
    if ball.left <= 0:
        right_score += 1
        reset_ball(1)
    elif ball.right >= WIDTH:
        left_score += 1
        reset_ball(-1)

    # Draw frame
    screen.fill(BLACK)

    # Center line
    for y in range(0, HEIGHT, 20):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 2, y, 4, 10))

    screen.blit(PADDLE_IMAGE, left_paddle)
    screen.blit(PADDLE_IMAGE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    score_text = font.render(f"{left_score}  {right_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()
    clock.tick(FPS)

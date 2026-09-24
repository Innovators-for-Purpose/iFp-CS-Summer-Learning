import pygame
import sys


# -----------------------------
# Settings
# -----------------------------

WIDTH, HEIGHT = 900, 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 80, 80)

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 110
PADDLE_SPEED = 6

BALL_SIZE = 18
BALL_SPEED_X = 5
BALL_SPEED_Y = 4

WINNING_SCORE = 5


# -----------------------------
# Reset the ball
# -----------------------------

def reset_ball(direction):
    global ball_speed_x, ball_speed_y

    ball.center = (WIDTH // 2, HEIGHT // 2)

    ball_speed_x = direction * BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y


# -----------------------------
# Handle keyboard/window events
# -----------------------------

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# -----------------------------
# Move the paddles
# -----------------------------

def move_paddles(keys):
    # Left paddle: W and S
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED

    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    # Right paddle: Up and Down arrows
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED

    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED


# -----------------------------
# Move the ball
# -----------------------------

def move_ball():
    global ball_speed_x, ball_speed_y
    global left_score, right_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce off top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Hit left paddle
    if ball.colliderect(left_paddle) and ball_speed_x < 0:
        ball.left = left_paddle.right
        ball_speed_x *= -1

        offset = (
            (ball.centery - left_paddle.centery)
            / (PADDLE_HEIGHT / 2)
        )
        ball_speed_y = offset * 6

    # Hit right paddle
    if ball.colliderect(right_paddle) and ball_speed_x > 0:
        ball.right = right_paddle.left
        ball_speed_x *= -1

        offset = (
            (ball.centery - right_paddle.centery)
            / (PADDLE_HEIGHT / 2)
        )
        ball_speed_y = offset * 6

    # Right player scores
    if ball.left <= 0:
        right_score += 1
        reset_ball(1)

    # Left player scores
    elif ball.right >= WIDTH:
        left_score += 1
        reset_ball(-1)


# -----------------------------
# Draw the game
# -----------------------------

def draw_game(window, font):
    window.fill(BLACK)

    # Center line
    for y in range(0, HEIGHT, 20):
        pygame.draw.rect(
            window,
            WHITE,
            (WIDTH // 2 - 2, y, 4, 10)
        )

    # Paddles
    pygame.draw.rect(window, BLUE, left_paddle)
    pygame.draw.rect(window, RED, right_paddle)

    # Ball
    pygame.draw.ellipse(window, WHITE, ball)

    # Score
    score_text = font.render(
        f"{left_score}    {right_score}",
        True,
        WHITE
    )

    window.blit(
        score_text,
        (
            WIDTH // 2 - score_text.get_width() // 2,
            20
        )
    )

    pygame.display.flip()


# -----------------------------
# Main game function
# -----------------------------

def main(window):
    global left_paddle, right_paddle, ball
    global left_score, right_score

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 64)

    # Create paddles
    left_paddle = pygame.Rect(
        40,
        HEIGHT // 2 - PADDLE_HEIGHT // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT
    )

    right_paddle = pygame.Rect(
        WIDTH - 40 - PADDLE_WIDTH,
        HEIGHT // 2 - PADDLE_HEIGHT // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT
    )

    # Create ball
    ball = pygame.Rect(
        WIDTH // 2 - BALL_SIZE // 2,
        HEIGHT // 2 - BALL_SIZE // 2,
        BALL_SIZE,
        BALL_SIZE
    )

    # Starting scores
    left_score = 0
    right_score = 0

    # Start ball moving toward the right
    reset_ball(1)

    # Game loop
    while True:
        handle_events()

        # Keyboard input
        keys = pygame.key.get_pressed()

        # Move paddles
        move_paddles(keys)

        # Move ball and check collisions
        move_ball()

        # Draw everything
        draw_game(window, font)

        # Limit game to 60 FPS
        clock.tick(FPS)


# -----------------------------
# Start the program
# -----------------------------

if __name__ == "__main__":
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Pong Game")

    main(window)

    pygame.quit()

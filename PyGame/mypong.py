pygame.init()

python
WIDTH, HEIGHT = 900, 600

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_SPEED = 6
BALL_SPEED_X = 5
BALL_SPEED_Y = 4

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 110
BALL_SIZE = 18

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
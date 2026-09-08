import pygame
import sys


WIDTH, HEIGHT = 960, 600
FPS = 60
WORLD_WIDTH = 3600
PLAYER_SIZE = 34
MOVE_SPEED = 5
JUMP_SPEED = -13
GRAVITY = 0.6

SKY = (116, 190, 212)
SUN = (255, 220, 132)
CLOUD = (224, 244, 237)
HILL_FAR = (103, 166, 151)
HILL_NEAR = (72, 135, 119)
GROUND = (50, 77, 68)
PLATFORM_TOP = (226, 183, 91)
PLATFORM_SIDE = (157, 103, 61)
PLAYER_COLOR = (239, 91, 91)
PLAYER_FACE = (255, 232, 188)
INK = (35, 45, 48)

pygame.init()
pygame.display.set_caption("Little Leap")
clock = pygame.time.Clock()


def make_platforms():
    return [
        pygame.Rect(0, 530, 720, 70),
        pygame.Rect(800, 530, 620, 70),
        pygame.Rect(1510, 530, 720, 70),
        pygame.Rect(2320, 530, 1280, 70),
        pygame.Rect(420, 430, 180, 22),
        pygame.Rect(960, 390, 190, 22),
        pygame.Rect(1240, 470, 150, 22),
        pygame.Rect(1660, 410, 210, 22),
        pygame.Rect(1980, 330, 180, 22),
        pygame.Rect(2470, 420, 210, 22),
        pygame.Rect(2860, 350, 180, 22),
        pygame.Rect(3200, 455, 190, 22),
    ]


def draw_player(surface, player_rect, camera_x):
    """Draw the placeholder character; replace this function with sprite blitting later."""
    screen_rect = player_rect.move(-camera_x, 0)
    pygame.draw.ellipse(surface, PLAYER_COLOR, screen_rect)
    pygame.draw.circle(surface, PLAYER_FACE, (screen_rect.centerx, screen_rect.top + 13), 10)
    pygame.draw.circle(surface, INK, (screen_rect.centerx - 4, screen_rect.top + 12), 2)
    pygame.draw.circle(surface, INK, (screen_rect.centerx + 4, screen_rect.top + 12), 2)


def draw_background(surface, camera_x):
    surface.fill(SKY)
    pygame.draw.circle(surface, SUN, (WIDTH - 110, 90), 48)
    for cloud_x, cloud_y in ((150, 105), (540, 170), (830, 90)):
        x = cloud_x - int(camera_x * 0.15) % (WIDTH + 240)
        pygame.draw.circle(surface, CLOUD, (x, cloud_y), 25)
        pygame.draw.circle(surface, CLOUD, (x + 28, cloud_y - 10), 34)
        pygame.draw.circle(surface, CLOUD, (x + 60, cloud_y), 25)
    for offset, color, height in ((0.18, HILL_FAR, 110), (0.32, HILL_NEAR, 160)):
        points = [(-200, HEIGHT), (-200, HEIGHT - height)]
        for world_x in range(-200, WORLD_WIDTH + 400, 260):
            screen_x = world_x - int(camera_x * offset)
            points.extend(((screen_x, HEIGHT - height), (screen_x + 130, HEIGHT - height - 85),
                           (screen_x + 260, HEIGHT - height)))
        points.append((WIDTH + 200, HEIGHT))
        pygame.draw.polygon(surface, color, points)


def move_player(player, velocity, platforms):
    player.x += velocity.x
    player.x = max(0, min(player.x, WORLD_WIDTH - PLAYER_SIZE))
    for platform in platforms:
        if player.colliderect(platform):
            if velocity.x > 0:
                player.right = platform.left
            elif velocity.x < 0:
                player.left = platform.right

    velocity.y += GRAVITY
    player.y += velocity.y
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if velocity.y > 0:
                player.bottom = platform.top
                velocity.y = 0
                on_ground = True
            elif velocity.y < 0:
                player.top = platform.bottom
                velocity.y = 0
    return on_ground


def main(window):
    platforms = make_platforms()
    player = pygame.Rect(100, 470, PLAYER_SIZE, PLAYER_SIZE)
    velocity = pygame.Vector2(0, 0)
    camera_x = 0
    on_ground = False
    won = False
    font = pygame.font.Font(None, 28)
    big_font = pygame.font.Font(None, 46)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
                if on_ground and not won:
                    velocity.y = JUMP_SPEED
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                player.topleft = (100, 470)
                velocity.update(0, 0)
                won = False

        keys = pygame.key.get_pressed()
        velocity.x = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) * MOVE_SPEED - (keys[pygame.K_a] or keys[pygame.K_LEFT]) * MOVE_SPEED
        if not won:
            on_ground = move_player(player, velocity, platforms)
            if player.top > HEIGHT:
                player.topleft = (100, 470)
                velocity.update(0, 0)
            if player.right >= WORLD_WIDTH - 180:
                won = True

        camera_x = max(0, min(player.centerx - WIDTH // 2, WORLD_WIDTH - WIDTH))
        draw_background(window, camera_x)
        for platform in platforms:
            visible = platform.copy().move(-camera_x, 0)
            pygame.draw.rect(window, PLATFORM_SIDE, visible)
            pygame.draw.rect(window, PLATFORM_TOP, (visible.x, visible.y, visible.width, 7))
        draw_player(window, player, camera_x)

        hint = font.render("A / D or arrows: move    SPACE: jump    R: restart", True, INK)
        window.blit(hint, (22, 20))
        if won:
            message = big_font.render("You made it!", True, INK)
            window.blit(message, (WIDTH // 2 - message.get_width() // 2, 76))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)

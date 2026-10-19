import pygame
import sys

# -----------------------------
# Game settings
# -----------------------------

WIDTH, HEIGHT = 960, 600
FPS = 60
WORLD_WIDTH = 3600

PLAYER_SIZE = 34
MOVE_SPEED = 10
JUMP_SPEED = -13
GRAVITY = 0.6

# -----------------------------
# Colors
# -----------------------------

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

# -----------------------------
# Pygame setup
# -----------------------------

pygame.init()
pygame.display.set_caption("My Platform Game")
clock = pygame.time.Clock()


# -----------------------------
# Create platforms
# -----------------------------

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


# -----------------------------
# Draw player
# -----------------------------

def draw_player(surface, player_rect, camera_x):
    screen_rect = player_rect.move(-camera_x, 0)

    # Body
    pygame.draw.ellipse(
        surface,
        PLAYER_COLOR,
        screen_rect
    )

    # Face
    pygame.draw.circle(
        surface,
        PLAYER_FACE,
        (screen_rect.centerx, screen_rect.top + 13),
        10
    )

    # Eyes
    pygame.draw.circle(
        surface,
        INK,
        (screen_rect.centerx - 4, screen_rect.top + 12),
        2
    )

    pygame.draw.circle(
        surface,
        INK,
        (screen_rect.centerx + 4, screen_rect.top + 12),
        2
    )


# -----------------------------
# Draw background
# -----------------------------

def draw_background(surface, camera_x):
    # Sky
    surface.fill(SKY)

    # Sun
    pygame.draw.circle(
        surface,
        SUN,
        (WIDTH - 110, 90),
        48
    )

    # Clouds
    for cloud_x, cloud_y in (
        (150, 105),
        (540, 170),
        (830, 90)
    ):
        x = cloud_x - int(camera_x * 0.15) % (WIDTH + 240)

        pygame.draw.circle(
            surface,
            CLOUD,
            (x, cloud_y),
            25
        )

        pygame.draw.circle(
            surface,
            CLOUD,
            (x + 28, cloud_y - 10),
            34
        )

        pygame.draw.circle(
            surface,
            CLOUD,
            (x + 60, cloud_y),
            25
        )

    # Hills
    for offset, color, height in (
        (0.18, HILL_FAR, 110),
        (0.32, HILL_NEAR, 160)
    ):
        points = [
            (-200, HEIGHT),
            (-200, HEIGHT - height)
        ]

        for world_x in range(
            -200,
            WORLD_WIDTH + 400,
            260
        ):
            screen_x = world_x - int(camera_x * offset)

            points.extend((
                (screen_x, HEIGHT - height),
                (
                    screen_x + 130,
                    HEIGHT - height - 85
                ),
                (
                    screen_x + 260,
                    HEIGHT - height
                )
            ))

        points.append((WIDTH + 200, HEIGHT))

        pygame.draw.polygon(
            surface,
            color,
            points
        )


# -----------------------------
# Move player
# -----------------------------

def move_player(player, velocity, platforms):
    # Horizontal movement
    player.x += velocity.x

    # Keep player inside the world
    player.x = max(
        0,
        min(
            player.x,
            WORLD_WIDTH - PLAYER_SIZE
        )
    )

    # Horizontal collision
    for platform in platforms:
        if player.colliderect(platform):
            if velocity.x > 0:
                player.right = platform.left

            elif velocity.x < 0:
                player.left = platform.right

    # Gravity
    velocity.y += GRAVITY

    # Vertical movement
    player.y += velocity.y

    on_ground = False

    # Vertical collision
    for platform in platforms:
        if player.colliderect(platform):

            # Landing on top
            if velocity.y > 0:
                player.bottom = platform.top
                velocity.y = 0
                on_ground = True

            # Hitting bottom of platform
            elif velocity.y < 0:
                player.top = platform.bottom
                velocity.y = 0

    return on_ground


# -----------------------------
# Main game
# -----------------------------

def main(window):
    platforms = make_platforms()

    player = pygame.Rect(
        100,
        470,
        PLAYER_SIZE,
        PLAYER_SIZE
    )

    velocity = pygame.Vector2(0, 0)

    camera_x = 0
    on_ground = False
    won = False

    font = pygame.font.Font(None, 28)
    big_font = pygame.font.Font(None, 46)

    # -------------------------
    # Game loop
    # -------------------------

    while True:

        # -------------------------
        # Events
        # -------------------------

        for event in pygame.event.get():

            # Close game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Keyboard events
            if event.type == pygame.KEYDOWN:

                # Jump
                if event.key in (
                    pygame.K_SPACE,
                    pygame.K_w,
                    pygame.K_UP
                ):
                    if on_ground and not won:
                        velocity.y = JUMP_SPEED

                # Restart
                if event.key == pygame.K_r:
                    player.topleft = (100, 470)
                    velocity.update(0, 0)
                    won = False

        # -------------------------
        # Keyboard movement
        # -------------------------

        keys = pygame.key.get_pressed()

        velocity.x = (
            (keys[pygame.K_d] or keys[pygame.K_RIGHT])
            * MOVE_SPEED
            -
            (keys[pygame.K_a] or keys[pygame.K_LEFT])
            * MOVE_SPEED
        )

        # -------------------------
        # Update player
        # -------------------------

        if not won:

            on_ground = move_player(
                player,
                velocity,
                platforms
            )

            # Player fell off screen
            if player.top > HEIGHT:
                player.topleft = (100, 470)
                velocity.update(0, 0)

            # Player reached the end
            if player.right >= WORLD_WIDTH - 180:
                won = True

        # -------------------------
        # Camera
        # -------------------------

        camera_x = max(
            0,
            min(
                player.centerx - WIDTH // 2,
                WORLD_WIDTH - WIDTH
            )
        )

        # -------------------------
        # Draw background
        # -------------------------

        draw_background(
            window,
            camera_x
        )

        # -------------------------
        # Draw platforms
        # -------------------------

        for platform in platforms:

            visible = platform.copy().move(
                -camera_x,
                0
            )

            # Platform body
            pygame.draw.rect(
                window,
                PLATFORM_SIDE,
                visible
            )

            # Platform top
            pygame.draw.rect(
                window,
                PLATFORM_TOP,
                (
                    visible.x,
                    visible.y,
                    visible.width,
                    7
                )
            )

        # -------------------------
        # Draw player
        # -------------------------

        draw_player(
            window,
            player,
            camera_x
        )

        # -------------------------
        # Game instructions
        # -------------------------

        hint = font.render(
            "A / D or arrows: move    SPACE: jump    R: restart",
            True,
            INK
        )

        window.blit(
            hint,
            (22, 20)
        )

        # -------------------------
        # Winning message
        # -------------------------

        if won:
            message = big_font.render(
                "You made it!",
                True,
                INK
            )

            window.blit(
                message,
                (
                    WIDTH // 2
                    - message.get_width() // 2,
                    76
                )
            )

        # -------------------------
        # Update screen
        # -------------------------

        pygame.display.flip()
        clock.tick(FPS)


# -----------------------------
# Start game
# -----------------------------

if __name__ == "__main__":
    window = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )

    main(window)

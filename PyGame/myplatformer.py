import pygame
import sys

# Constants
WIDTH, HEIGHT = 960, 600
FPS = 60
WORLD_WIDTH = 3600
PLAYER_SIZE = 34
MOVE_SPEED = 5
JUMP_SPEED = -13
GRAVITY = 0.6

#Questionable constant


#Color definitions
SKY = (116, 190, 212)
SUN = (255, 220, 132)
CLOUD = (224, 244, 237)
HILL_FAR = (103, 166, 151)
HILL_NEAR = (72, 135, 119)
GROUND = (50, 77, 68)
PLATFOM_TOP = (226, 183, 91)
PLATFORM_SIDE = (157, 103, 61)
PLAYER_COLOR = (239, 91, 91)
PLAYER_FACE = (255, 232, 188)
INK = (35, 45, 48)

pygame.init()
pygame.display.set_caption("My Platformer")
clock = pygame.time.Clock



def make_platforms():
    return [
        pygame.Rect(0,530, 720, 70),
        pygame.Rect(800, 530, 620, 70),
        pygame.Rect(1510, 530, 720, 70),
        pygame.Rect(2320, 530, 1280, 70),
        pygame.Rect(420, 430, 180, 22),
        pygame.Rect(960, 390, 190,22),
        pygame.Rect(1240, 470, 150, 22),
        pygame.Rect(1660, 410, 210, 22),
        pygame.Rect(1980, 330, 180, 22),
        pygame.Rect(2470, 420, 210, 22),
        pygame.Rect(2860, 350, 180, 22),
        pygame.Rect(3200, 455, 190, 22),
    ]

#player
def draw_player(surface, player_rect, camera_x):
    screen_rect = player_rect.move(-camera_x, 0)
    pygame.draw.ellipse(surface, PLAYER_COLOR, screen_rect)
    pygame.draw.circle(surface, PLAYER_FACE, (screen_rect.centrx, screen_rect.top + 13), 10)
    pygame.draw.circle(surface, INK, (screen_rect.centerx +4, screen_rect.top +12), 2)

#background
def draw_background(surface, camera_x):
    surface.fill(SKY)
    pygame.draw.circle(surface, SUN, (WIDTH - 110,90), 48)

    for clouds_x, cloud_y in ((150, 105), (540, 170), (830, 90)):
        x = clouds_x - int(camera_x * 0.15) % (WIDTH + 240)
        pygame.draw.circle(surface, CLOUD, (x, cloud_y), 25)
        pygame.draw.circle(surface, CLOUD, (x + 28, cloud_y - 10), 34)
        pygame.draw.circle(surface, CLOUD, (x + 60, cloud_y), 25)

        for offset, color, height in ((0.18, HILL_FAR, 110), (0.32, HILL_NEAR, 160)):
            points = [(-200, HEIGHT),(-200, HEIGHT - height)]
            for world_x in range (-200, WORLD_WIDTH + 400, 260): 
                screen_x = world_x - int(camera_x * offset)
                points.extend(((screen_x, HEIGHT - height)))
            points.append((WIDTH + 200, HEIGHT))
            pygame.draw.polygon(surface, color, points)

#Player movement
def move_player(player, velocity, platforms):
    player.x += velocity.x
    player.x = max(0, min(player.x, WORLD_WIDTH - PLAYER_SIZE))
    for platform in platforms:
        if player.collidereact(platform):
            if velocity.x > 0:
                player.right = platform.left
            elif velocity.x > 0:
                player.left = platform.right

    velocity.y += GRAVITY
    player.y += velocity.y
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if velocity.y > 0:
                player.bottom = player.top
                velocity.y = 0
                on_ground = True
            elif velocity.y < 0:
                player.top = platform.bottom
                velocity.y = 0
    return on_ground

# Main Function

def main(window):
    #rotate = g
    platforms = make_platforms()
    player = pygame.Rect(100, 470, PLAYER_SIZE, PLAYER_SIZE)
    velocity = pygame.Vector2(0, 0)
    camera_x = 0
    on_ground = False
    won = False
    front = pygame.font.Font(None, 28)
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
                velocity.update(0,0)
                won = False
            #if event.type == pygame.KEYDOWN and event.key == pygame.K_p:player.center 
            
            velocity.x = ()
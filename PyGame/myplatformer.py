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
    pygame.draw.oval(surface, PLAYER_FACE, (screen_rect.centrx, screen_rect.top + 13), 10)
    pygame.draw.oval(surface, INK, (screen_rect.centerx +4, screen_rect.top +12), 2)

#background
def draw_background(surface, camera_x):
    surface.fill(SKY)
    pygame.draw.circle(surface, SUN, (WIDTH - 110,90), 48)

    for clouds_x, cloud_y in ((150, 105), (540, 170), (830, 90)):
    
        x = clouds_x - int(camera_x * 0.15) % (WIDTH + 240)
        pygame.draw.circle(surface, CLOUD, (x, cloud_y), 25)
        pygame.draw.circle(surface, CLOUD, (x + 28, cloud_y - 10), 34)
        pygame.draw.circle(surface, CLOUD, (x + 60, cloud_y), 25)

        
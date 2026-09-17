# myplatformer
# this is my testing version of platformer

import pygame #loads pygame library
import sys #loads the system where our game will be open

# Creating the game window

WIDTH, HEIGHT = 960, 600 #this is how big your window will be!
FPS = 60 #this represents the frames per second, this value controls how quickly the game runs
WORLD_WIDTH = 3600 #the world width inside of the window is wider than it looks like!

# Creating the variables that control the player moves

PLAYER_SIZE = 34 # how big or small is our main character
MOVE_SPEED = 5 # how fast the player moves
JUMP_SPEED = -13 # how fast the player jumps
GRAVITY = 0.6 #

SKY = (116, 190, 212) #colors!!!
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

# initializing pygame library
pygame.init() 
pygame.display.set_caption("My Platform Game") #changes title of game
clock = pygame.time.Clock() #control how fast game runs


# Creating the platforms for the game!

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

# Drawing the player

def draw_player(surface, player_rect, camera_x):
    screen_rect = player_rect.move(-camera_x, 0)

    pygame.draw.ellipse(surface, PLAYER_COLOR, screen_rect) #draws player's body

    pygame.draw.circle(surface, PLAYER_FACE, (screen_rect.centerx, screen_rect.top + 13), 10) #draws player's face, notice how we are calling variables we declare at the beginning of our program!

    pygame.draw.circle(surface, INK, (screen_rect.centerx - 4, screen_rect.top + 12), 2) #draws player's left eye

    pygame.draw.circle(surface, INK, (screen_rect.centerx + 4, screen_rect.top + 12), 2) #draws player's right eye

# Drawing background

    for cloud_x, cloud_y in ((150, 105), (540, 170), (830, 90)): #for loop to create a lot of clouds
        x = cloud_x - int(camera_x * 0.15) % (WIDTH + 240)
        pygame.draw.circle(surface, CLOUD, (x, cloud_y), 25)
        pygame.draw.circle(surface, CLOUD, (x + 28, cloud_y - 10), 34)
        pygame.draw.circle(surface, CLOUD, (x + 60, cloud_y), 25)

    for offset, color, height in ((0.18, HILL_FAR, 110), (0.32, HILL_NEAR, 160)): # creating hills!
        points = [(-200, HEIGHT), (-200, HEIGHT - height)]
        for world_x in range(-200, WORLD_WIDTH + 400, 260):
            screen_x = world_x - int(camera_x * offset)
            points.extend(((screen_x, HEIGHT - height), (screen_x + 130, HEIGHT - height - 85),
                           (screen_x + 260, HEIGHT - height)))
        points.append((WIDTH + 200, HEIGHT))
        pygame.draw.polygon(surface, color, points)

# Start working on the movement of the player

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

### Creating main function!
    

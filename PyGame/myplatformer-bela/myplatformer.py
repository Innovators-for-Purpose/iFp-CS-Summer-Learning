# myplatformer
# this is my testing version of platformer

import pygame #loads pygame library
import sys #loads the system where our game will be open

# initializing pygame library
pygame.init()

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



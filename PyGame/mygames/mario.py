import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

SKY_BLUE = (92, 148, 252)
MARIO_RED = (255, 0, 0)
MARIO_BLUE = (0, 0, 255)
BRICK_RED = (205, 92, 92)
PIPE_GREEN = (0, 128, 0)
COIN_YELLOW = (255, 221, 111)

class Mario:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.jump_power = 15
        self.on_ground = False
        
    def draw(self, screen, camera_X):
        x = self.x - camera_X
        pygame.draw.rect(screen, MARIO_RED, (x + 8, self.y + 12, 16, 12))
        pygame.draw.rect(screen, MARIO_BLUE, (x + 6, self.y + 16, 20, 16))
        pygame.draw.rect(screen, (255, 220, 177), (x + 4, self.y, 24, 16))
        pygame.draw.rect(screen, MARIO_RED, (x + 2, self.y - 4, 28, 8))

        def update_camera(self):
            self.camera_x = self.mario.x - SCREEN_WIDTH // 2
            if self.camera_x < 0:
                self.camera_x = 0

class Goomba:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = -1
        self.alive = True

class Coin:
    def __init__(self, x, y):
        self.rotation = 0
        self.collected = False

    def update(self):
        self.rotation += 0.2

    def draw(self, screen, camera_x):
        x = self.x - camera_x
        scale = abs(math.sin(self.rotation))
        width = int(self.width * scale)
        pygame.draw.ellipse(screen, COIN_YELLOW, (x + (self.width - width) // 2, self.y, width, self.height))


def handle_collisions(self):
    mario_rect = pygame.Rect(self.mario.x, self.mario.y, 
                              self.mario.width, self.mario.height)

    for coin in self.coins:
        if not coin.collected:
            coin_rect = pygame.Rect(coin.x, coin.y, coin.width, coin.height)
            if mario_rect.colliderect(coin_rect):
                coin.collected = True
                self.score += 100

    for goomba in self.goombas:
        if goomba.alive:
            goomba_rect = pygame.Rect(goomba.x, goomba.y, goomba.width, goomba.height)
            if mario_rect.colliderect(goomba_rect):
                if self.mario.vel_y > 0 and self.mario.y < goomba.y:
                    goomba.alive = False
                    self.mario.vel_y = -8
                    self.score += 200
                else:
                    self.lives -= 1
def draw_background(self):
    self.screen.fill(SKY_BLUE)
    for i in range(10):
        x = (i * 200 - self.camera_x * 0.5) % (SCREEN_WIDTH + 100)
        self.draw_cloud(x, 80 + (i % 3) * 30)

def run(self):
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        self.mario.update(self.platforms)
        for goomba in self.goombas:
            goomba.update(self.platforms)
        for coin in self.coins:
            coin.update()

        self.handle_collisions()
        self.update_camera()

        self.draw_background()
        self.draw_all_objects()
        self.draw_ui()

        pygame.display.flip()
        clock.tick(FPS)



import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
SKY_BLUE = (92, 148, 252)
MARIO_RED = (255, 0, 0)
MARIO_BLUE = (0, 0, 255)
BRICK_RED = (205, 92, 92)
PIPE_GREEN = (0, 128, 0)
COIN_YELLOW = (255, 221, 111)
WHITE = (255, 255, 255)


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

    def update(self, platforms):
        # Handle Input
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -self.jump_power
            self.on_ground = False

        # Apply Gravity
        self.vel_y += 0.8  # Gravity force
        if self.vel_y > 12:
            self.vel_y = 12

        # Move X and check collisions
        self.x += self.vel_x
        mario_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for platform in platforms:
            if mario_rect.colliderect(platform):
                if self.vel_x > 0:
                    self.x = platform.left - self.width
                elif self.vel_x < 0:
                    self.x = platform.right

        # Move Y and check collisions
        self.y += self.vel_y
        mario_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.on_ground = False
        for platform in platforms:
            if mario_rect.colliderect(platform):
                if self.vel_y > 0:
                    self.y = platform.top - self.height
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.y = platform.bottom
                    self.vel_y = 0

    def draw(self, screen, camera_x):
        x = self.x - camera_x
        # Simple bounding shapes mimicking Mario
        pygame.draw.rect(screen, (255, 220, 177), (x + 4, self.y, 24, 16))  # Face
        pygame.draw.rect(screen, MARIO_RED, (x + 2, self.y - 4, 28, 8))     # Cap
        pygame.draw.rect(screen, MARIO_RED, (x + 8, self.y + 12, 16, 12))   # Shirt
        pygame.draw.rect(screen, MARIO_BLUE, (x + 6, self.y + 16, 20, 16))  # Overalls


class Goomba:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.vel_x = -2
        self.vel_y = 0
        self.alive = True

    def update(self, platforms):
        if not self.alive:
            return

        # Apply Gravity
        self.vel_y += 0.8
        
        # Horizontal Movement & Collision
        self.x += self.vel_x
        goomba_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for platform in platforms:
            if goomba_rect.colliderect(platform):
                self.vel_x *= -1  # Reverse direction
                if self.vel_x > 0:
                    self.x = platform.right
                else:
                    self.x = platform.left - self.width

        # Vertical Movement & Collision
        self.y += self.vel_y
        goomba_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for platform in platforms:
            if goomba_rect.colliderect(platform):
                if self.vel_y > 0:
                    self.y = platform.top - self.height
                    self.vel_y = 0

    def draw(self, screen, camera_x):
        if self.alive:
            x = self.x - camera_x
            pygame.draw.rect(screen, BRICK_RED, (x, self.y, self.width, self.height))
            pygame.draw.circle(screen, (0, 0, 0), (x + 8, self.y + 12), 3)
            pygame.draw.circle(screen, (0, 0, 0), (x + 24, self.y + 12), 3)


class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 28
        self.rotation = 0
        self.collected = False  # Fixed typo: changed 'colected' to 'collected'

    def update(self):
        self.rotation += 0.1

    def draw(self, screen, camera_x):
        if not self.collected:
            x = self.x - camera_x
            scale = abs(math.sin(self.rotation))
            width = int(self.width * scale)
            if width < 2: 
                width = 2
            pygame.draw.ellipse(screen, COIN_YELLOW, (x + (self.width - width) // 2, self.y, width, self.height))


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Super Mario Prototype")
        self.font = pygame.font.SysFont(None, 36)
        
        # Entities
        self.mario = Mario(100, 300)
        self.camera_x = 0
        self.score = 0
        self.lives = 3
        
        # World Layout
        self.platforms = [
            pygame.Rect(0, 500, 2000, 100),    # Floor Ground
            pygame.Rect(400, 400, 120, 32),    # Raised Platform 1
            pygame.Rect(600, 320, 150, 32),    # Raised Platform 2
            pygame.Rect(900, 420, 64, 80)      # Static Pipe Obstacle
        ]
        
        self.coins = [Coin(450, 350), Coin(650, 270), Coin(700, 270)]
        self.goombas = [Goomba(500, 450), Goomba(1100, 450)]

    def update_camera(self):
        self.camera_x = self.mario.x - SCREEN_WIDTH // 2
        if self.camera_x < 0:
            self.camera_x = 0

    def handle_collisions(self):
        mario_rect = pygame.Rect(self.mario.x, self.mario.y, self.mario.width, self.mario.height)
        
        # Coin Collection
        for coin in self.coins:
            if not coin.collected:
                coin_rect = pygame.Rect(coin.x, coin.y, coin.width, coin.height)
                if mario_rect.colliderect(coin_rect):
                    coin.collected = True
                    self.score += 100

        # Goomba Collisions
        for goomba in self.goombas:
            if goomba.alive:
                goomba_rect = pygame.Rect(goomba.x, goomba.y, goomba.width, goomba.height)
                if mario_rect.colliderect(goomba_rect):
                    # Falling on Goomba from above
                    if self.mario.vel_y > 0 and (self.mario.y + self.mario.height - self.mario.vel_y) <= goomba.y + 12:
                        goomba.alive = False
                        self.mario.vel_y = -10
                        self.score += 200
                    else:
                        # Taking damage
                        self.lives -= 1
                        self.mario.x = 100  # Reset Position
                        self.mario.y = 300

    def draw_background(self):
        self.screen.fill(SKY_BLUE)
        for i in range(15):
            # Parallax Cloud Effect
            x = int(i * 300 - self.camera_x * 0.3) % (SCREEN_WIDTH + 200) - 100
            y = 80 + (i % 3) * 40
            pygame.draw.circle(self.screen, WHITE, (x, y), 30)
            pygame.draw.circle(self.screen, WHITE, (x + 25, y - 10), 35)
            pygame.draw.circle(self.screen, WHITE, (x + 50, y), 30)

    def draw_all_objects(self):
        # Draw Environment Blocks
        for rect in self.platforms:
            screen_rect = pygame.Rect(rect.x - self.camera_x, rect.y, rect.width, rect.height)
            # Differentiate the Pipe from the Floor Ground
            color = PIPE_GREEN if rect.width == 64 else BRICK_RED
            pygame.draw.rect(self.screen, color, screen_rect)

        # Draw Entities
        for coin in self.coins:
            coin.draw(self.screen, self.camera_x)
            
        for goomba in self.goombas:
            goomba.draw(self.screen, self.camera_x)
            
        self.mario.draw(self.screen, self.camera_x)

    def draw_ui(self):
        score_txt = self.font.render(f"SCORE: {self.score}", True, WHITE)
        lives_txt = self.font.render(f"LIVES: {self.lives}", True, WHITE)
        self.screen.blit(score_txt, (20, 20))
        self.screen.blit(lives_txt, (SCREEN_WIDTH - 150, 20))

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Game Engine States Update
            self.mario.update(self.platforms)
            for goomba in self.goombas:
                goomba.update(self.platforms)
            for coin in self.coins:
                coin.update()
                
            self.handle_collisions()
            self.update_camera()
            
            # Graphics Render Lifecycle
            self.draw_background()
            self.draw_all_objects()
            self.draw_ui()
            
            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()


import pygame
import sys



Width, Height = 1000, 900
FPS = 60
World_Width = 3600



Player_Size = 20
Move_Speed = 7.5
Jump_Speed = -15
Gravity = 0.75



Sky = (95, 126, 160)
Cloud = (255, 255, 255)
Sun = (207, 255, 4)
Hill_Far = (144, 238, 144)
Hill_Near = (10, 221, 8)
Ground = (115, 115, 208)
Platform_Top = (255, 255, 255)
Platform_Side = (115, 115, 208)
Player_Color = (255, 142, 87)
Player_Face = (255, 255, 255)
Ink = (0, 0, 0)



pygame.init()
pygame.display.set_caption("MESD Platformer")
clock = pygame.time.Clock()


def make_platforms():
    return [
        pygame.Rect(0, 625, 850, 125),
        pygame.Rect(750, 625, 600, 125),
        pygame.Rect(1500, 625, 850, 125),
        pygame.Rect(2250, 625, 1300, 125),
        pygame.Rect(500, 523, 220, 28),
        pygame.Rect(975, 420, 245, 28),
        pygame.Rect(1300, 490, 175, 28),
        pygame.Rect(1725, 440, 315, 28),
        pygame.Rect(2225, 340, 285, 28),
        pygame.Rect(2950, 430, 315, 28),
        pygame.Rect(3700, 360, 285, 28),
        pygame.Rect(4200, 525, 295, 28),

    ]

def draw_player(Surface, Player_Rect, Camera_X):
    Screen_Rect = Player_Rect.move(-Camera_X, 0)

    pygame.draw.ellipse(Surface, Player_Color, 
Screen_Rect) 

    pygame.draw.circle(Surface, Player_Face, 
(Screen_Rect.centerx, Screen_Rect.top + 13), 10)
    
    pygame.draw.circle(Surface, Ink, (Screen_Rect.centerx 
- 4, Screen_Rect.top + 12), 2)

    pygame.draw.circle(Surface, Ink, (Screen_Rect.centerx 
+ 4, Screen_Rect.top + 12), 2)
    

def draw_background(Surface, Camera_X):
    Surface.fill(Sky)
    pygame.draw.circle(Surface, Sun, (Width - 100, 100), 50)
    
    
    for Cloud_X, Cloud_Y in ((125, 95), (555, 200), (1025, 475)):
        X = Cloud_X - int(Camera_X * 0.15) % (Width + 200)
        pygame.draw.circle(Surface, Cloud, (X, Cloud_Y),50)
        pygame.draw.circle(Surface, Cloud, (X + 50, Cloud_Y - 10), 50)
        pygame.draw.circle(Surface, Cloud, (X + 100, Cloud_Y), 50)

    for offset, Color, height in ((0, Hill_Far, 150),
    (50, Hill_Near, 250)):
        points = [(0, Height), (0, Height - height)]
        for World_X in range(-200, World_Width + 200, 200):
            Screen_X = World_X - int(Camera_X * offset)
            points.extend(((Screen_X, Height - height),
        (Screen_X + 100, Height - height - 50), (Screen_X 
    + 200, Height - height))) 
        points.append((Width + 200, height))
        pygame.draw.polygon(Surface, Color, points)

    
def Move_Player(Player, Velocity, Platforms):
    Player.x += Velocity.x
    Player.x = max(0, min(Player.x, World_Width - Player_Size))
    for platform in Platforms:
        if Player.colliderect(platform):
            if Velocity.x > 0:
                Player.right = platform.left
            elif Velocity.x < 0:
                Player.left = platform.right

    Velocity.y += Gravity 
    Player.y += Velocity.y
    On_Ground = False
    for platform in Platforms:
        if Player.colliderect(platform):
            if Velocity.y > 0:
                Player.bottom = platform.top
                Velocity.y = 0
                On_Ground = True
            elif Velocity.y < 0:
                Player.top = platform.bottom
                Velocity.y = 0
    return On_Ground

def main(window):
    Platforms = make_platforms()
    player = pygame.Rect(100, 400, Player_Size, Player_Size)
    Velocity = pygame.Vector2(0, 0)
    Camera_X = 0
    On_Ground = False
    won = False
    font = pygame.font.Font(None, 48)
    Big_Font = pygame.font.Font(None, 72)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, 
            pygame.K_w, pygame.K_UP):
                if On_Ground and not won:
                    Velocity.y = Jump_Speed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                player.topleft = (120, 490)
                Velocity.update(0, 0)
                won = False
            keys = pygame.key.get_pressed()
            Velocity.x = (
                 (keys[pygame.K_d] or keys[pygame.K_RIGHT]) * Move_Speed 
            - (keys[pygame.K_a] or keys[pygame.K_LEFT]) * Move_Speed
            )
            if not won:
                On_Ground = Move_Player(player, Velocity, Platforms)
            if player.top > Height:
                player.topleft = (120, 490)
                Velocity.update(0, 0)
            Camera_X = max(0, 
            min(player.centerx - Width // 
            2, World_Width - Width))
            draw_background(window, 
            Camera_X)
            for platform in Platforms:
                visible = platform.move(-Camera_X, 0)
                pygame.draw.rect(window, Platform_Side, visible)
                pygame.draw.rect(window, Platform_Top, (visible.x, visible.y, visible.width, 5))
            if won: 
                message = Big_Font.render("You Win!", True, Ink)
                window.blit(message, (Width // 2 - message.get_width() // 2, 76))
            pygame.display.flip()
            clock.tick(FPS)
           
           
           
if __name__ == "__main__":
    window = pygame.display.set_mode((Width, Height))
    main(window)



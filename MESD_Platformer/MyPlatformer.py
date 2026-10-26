
import pygame
import sys



Width, Height = 900, 600
FPS = 60
World_Width = 10000
Player_Size = 100
Move_Speed = 25
Jump_Speed = -14
Gravity = 0.6


Sky = (0, 0, 0)
Cloud = (255, 255, 255)
Moon = (255, 255, 255)
Hill_Far = (191, 191, 191)
Hill_Near = (64, 64, 64)
Ground = (115, 115, 208)
Platform_Top = (255, 255, 255)
Platform_Side = (115, 115, 208)
Player_Color = (255, 0, 0)
Player_Face = (0, 0, 0)
Ink = (255, 0, 255)



pygame.init()
pygame.display.set_caption("MESD Platformer")
clock = pygame.time.Clock()


def make_platforms():
    return [
        #ground 1
        pygame.Rect(0, 530, 10000, 70),
        # ground 2
        pygame.Rect(2100, 530, 6000, 70),
        pygame.Rect(500, 390, 190, 22),
        pygame.Rect(800, 470, 150, 22),
        pygame.Rect(1200, 410, 210, 22),
        pygame.Rect(1500, 330, 180, 22),
        pygame.Rect(1800, 420, 210, 22),
        pygame.Rect(2100, 350, 180, 22),
        pygame.Rect(2400, 455, 190, 22),
        pygame.Rect(2750, 342, 244, 22),
        pygame.Rect(3000, 400, 250, 22),
        pygame.Rect(3600, 279, 192, 22),
        pygame.Rect(4200, 375, 391, 252),
        


    ]

def draw_player(Surface, Player_Rect, Camera_X):
    Screen_Rect = Player_Rect.move(-Camera_X, 0)
    pygame.draw.ellipse(Surface, Player_Color, Screen_Rect) 
    pygame.draw.circle(Surface, Player_Face, (Screen_Rect.centerx, Screen_Rect.top + 13), 10)
    pygame.draw.circle(Surface, Ink, (Screen_Rect.centerx - 4, Screen_Rect.top + 12), 2)
    pygame.draw.circle(Surface, Ink, (Screen_Rect.centerx + 4, Screen_Rect.top + 12), 2)
    

def draw_background(Surface, Camera_X):
    Surface.fill(Sky)
    pygame.draw.circle(Surface, Moon, (Width - 110, 90), 50)
    
    
    for Cloud_X, Cloud_Y in ((150, 105), (540, 170), (830, 90)):
        X = Cloud_X - int(Camera_X * 0.15) % (Width + 240)
        pygame.draw.circle(Surface, Cloud, (X, Cloud_Y), 25)
        pygame.draw.circle(Surface, Cloud, (X + 28, Cloud_Y - 10), 34)
        pygame.draw.circle(Surface, Cloud, (X + 60, Cloud_Y), 25)

    for offset, Color, height in ((0.18, Hill_Far, 110),(0.32, Hill_Near, 160)):
        points = [(-200, Height), (-200, Height - height)]
        for World_X in range(-200, World_Width + 400, 260):
            Screen_X = World_X - int(Camera_X * offset)
            points.extend(((Screen_X, Height - height), (Screen_X + 130, Height - height - 85), 
                           (Screen_X + 260, Height - height))) 
        points.append((Width + 200, Height))
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
    Player = pygame.Rect(100, 470, Player_Size, Player_Size)
    Velocity = pygame.Vector2(0, 0)
    Camera_X = 0
    On_Ground = False
    won = False
    font = pygame.font.Font(None, 48)
    Big_Font = pygame.font.Font(None, 46)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
                if On_Ground and not won:
                    Velocity.y = Jump_Speed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                Player.topleft = (100, 470)
                Velocity.update(0, 0)
                won = False

        keys = pygame.key.get_pressed()
        Velocity.x = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) * Move_Speed - (keys[pygame.K_a] or keys[pygame.K_LEFT]) * Move_Speed
        if not won:
            On_Ground = Move_Player(Player, Velocity, Platforms)
            if Player.top > Height:
                Player.topleft = (100, 470)
                Velocity.update(0, 0)
            if Player.right >= World_Width - 180:
                won = True



        Camera_X = max(0, min(Player.centerx - Width // 2, World_Width - Width))
        draw_background(window, Camera_X)
        for platform in Platforms:
            visible = platform.move(-Camera_X, 0)
            pygame.draw.rect(window, Platform_Side, visible)
            pygame.draw.rect(window, Platform_Top, (visible.x, visible.y, visible.width, 2))
        draw_player(window, Player, Camera_X)


        hint = font.render("Good Luck!", True, Ink)
        window.blit(hint, (22, 20))
        if won: 
            message = Big_Font.render("You Win!", True, Ink)
            window.blit(message, (Width // 2 - message.get_width() // 2, 76))
        pygame.display.flip()
        clock.tick(FPS)
           
           
           
if __name__ == "__main__":
    window = pygame.display.set_mode((Width, Height))
    main(window)



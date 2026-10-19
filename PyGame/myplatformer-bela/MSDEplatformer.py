
import pygame
import sys



Width, Height = 900, 600
FPS = 60
World_Width = 3600
Player_Size = 37
Move_Speed = 5
Jump_Speed = -13
Gravity = 0.6


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

def draw_player(Surface, Player_Rect, Camera_X):
    Screen_Rect = Player_Rect.move(-Camera_X, 0)
    pygame.draw.ellipse(Surface, Player_Color, Screen_Rect) 
    pygame.draw.circle(Surface, Player_Face, (Screen_Rect.centerx, Screen_Rect.top + 13), 10)
    pygame.draw.circle(Surface, Ink, (Screen_Rect.centerx - 4, Screen_Rect.top + 12), 2)
    pygame.draw.circle(Surface, Ink, (Screen_Rect.centerx + 4, Screen_Rect.top + 12), 2)
    

def draw_background(Surface, Camera_X):
    Surface.fill(Sky)
    pygame.draw.circle(Surface, Sun, (Width - 110, 90), 50)
    
    
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
# Error detected here: if not won was not in right aligment
        keys = pygame.key.get_pressed()
        Velocity.x = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) * Move_Speed - (keys[pygame.K_a] or keys[pygame.K_LEFT]) * Move_Speed
        if not won:
            On_Ground = Move_Player(Player, Velocity, Platforms)
            if Player.top > Height:
                Player.topleft = (100, 470)
                Velocity.update(0, 0)
            if Player.right >= World_Width - 180:
                won = True
                

#Same error here for platform in Platforms was not align correctly
        Camera_X = max(0, min(Player.centerx - Width // 2, World_Width - Width))
        draw_background(window, Camera_X)
        for platform in Platforms:
            visible = platform.move(-Camera_X, 0)
            pygame.draw.rect(window, Platform_Side, visible)
            pygame.draw.rect(window, Platform_Top, (visible.x, visible.y, visible.width, 5))
        draw_player(window, Player, Camera_X)


        hint = font.render("A / D or arrows: move    SPACE: jump    R: restart", True, Ink)
        window.blit(hint, (22, 20))

        if won: 
            message = Big_Font.render("You Win!", True, Ink)
            window.blit(message, (Width // 2 - message.get_width() // 2, 76))
        
        pygame.display.flip()
        clock.tick(FPS)
           
           
           
if __name__ == "__main__":
    window = pygame.display.set_mode((Width, Height))
    main(window)
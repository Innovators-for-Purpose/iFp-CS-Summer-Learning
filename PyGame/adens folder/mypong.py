import pygame
import sys

fps = 60

width, height = 900, 600

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
paddle_speed = 15
ball_speed_x = 8
ball_speed_y = 7

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

paddle_width = 15
paddle_height = 110
ball_size = 18
font = pygame.font.Font(None, 60)

left_score = 0
right_score = 0

left_paddle = pygame.Rect(40, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 40 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size) 


def reset_ball(direction):
    global ball_speed_x, ball_speed_y
    ball.center = (width // 2, height // 2)
    ball_speed_x = direction * ball_speed_x
    ball_speed_y = ball_speed_y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()


    keys = pygame.key.get_pressed()

    # Update the right paddle movement
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed

    if keys[pygame.K_DOWN] and right_paddle.bottom < height:
        right_paddle.y += paddle_speed

    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed

    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += paddle_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) and ball_speed_x < 0:
        ball_speed_x *= -1  
        offset = (ball.centery - left_paddle.centery) / (paddle_height / 2)
        ball_speed_y = offset * 6
    if ball.colliderect(right_paddle) and ball_speed_x > 0:
        ball_speed_x *= -1
        offset = (ball.centery - right_paddle.centery) / (paddle_height / 2)
        ball_speed_y = offset * 6


    if ball.left <= 0:
        right_score += 1
        reset_ball(1)
    elif ball.right >= width:
        left_score += 1
        reset_ball(-1)  

    window.fill(red)

    for y in range(0, height, 20):
        pygame.draw.rect(window, white, (width // 2 - 2, y, 4, 10))

    pygame.draw.rect(window, white, left_paddle)
    pygame.draw.rect(window, white, right_paddle)
    pygame.draw.ellipse(window, white, ball)

    score_text = font.render(f"{left_score}  {right_score}", True, white)
    window.blit(score_text, (width // 2 - score_text.get_width() // 2, 20)) 

    pygame.display.flip()
    clock.tick(fps)



   



#     import pygame
# import sys

# width, height = 900, 600
# fps = 60

# def reset_ball(direction):
#     # reset the ball position and speed
#     pass

#     if __name__ == "__main__":





#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

#             keys = pygame.key.get_pressed()

#             if keys[pygame.K_w] and left_paddle.top > 0:
#                 left_paddle.y -= paddle_speed

#             if keys[pygame.K_s] and left_paddle.bottom < height:
#                  left_paddle.y += paddle_speed
#             if keys[pygame.K_UP] and right_paddle.top > 0:
#                 right_paddle.y -= paddle_speed
#             if keys[pygame.K_DOWN] and right_paddle.bottom < height:
#                 right_paddle.y += paddle_speed

#             ball.x += ball_speed_x
#             ball.y += ball_speed_y

#             if ball.top <= 0 or ball.bottom >= height:
#                 ball_speed_y *= -1

#             if ball.colliderect(left_paddle) and ball_speed_x < 0:
#                 ball_speed_x *= -1  
#                 offset = (ball.centery - left_paddle.centery) / (paddle_height / 2)
#                 ball_speed_y = offset * 6
#             if ball.left <= 0:
#                 right_score += 1
#                 reset_ball(1) 
#             elif ball.right >= width:
#                 left_score += 1
#                 reset_ball(-1)
#             screen.fill(blue)
#             for y in range(0, height, 20):
#                 pygame.draw.rect(screen, white, (width // 2 - 2, y,4, 10))
#             pygame.draw.rect(screen, white, left_paddle)
#             pygame.draw.rect(screen, white, right_paddle)
#             pygame.draw.ellipse(screen, white, ball)

#             score_text = font.render(f"{left_score}  {right_score}", True, white)
#             screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 20)) 

#             pygame.display.flip()
#             clock.tick(fps)
             
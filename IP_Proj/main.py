import pygame

from paddle import Paddle
from ball import Ball

pygame.init()

# set up display
height = 600
width = 900
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paddle Ball (Pong)")

FPS = 60

# Paddle dimensions
paddle_wd = 15
paddle_ht = 120

# ball dimensions
size = 7

# winning score
win_score = 5

# create a font object
score_txt = pygame.font.SysFont("roboto", 50)


def draw(display, L_paddle, R_paddle, ball, L_score, R_score):

    paddles = (L_paddle, R_paddle)

    # Fill colour
    display.fill((0, 0, 0))

    # Render the score as text with the appropriate color
    L_score_text = score_txt.render(f"{L_score}", 1, (200, 200, 200))
    R_score_text = score_txt.render(f"{R_score}", 1, (200, 200, 200))

    # Blit the left and right scores to the top of the screen
    # The first parameter is the surface to blit, in this case the rendered score text
    # The second parameter is the position of the surface, which is centered horizontally
    # along the top of the screen for the left score, and centered horizontally
    # along the top of the screen for the right score
    score_width_L = L_score_text.get_width()//2
    score_width_R = R_score_text.get_width()//2
    display.blit(L_score_text, (width//4 - score_width_L, 80))
    display.blit(R_score_text, (width * (3/4) -
                                score_width_L, 80))

    # render() creates a surface with the specified text, font, and coluor, and blit() is then used to draw that surface onto the main surface or screen.

    for paddle in paddles:
        paddle.draw(display)

    ball.draw(display)
    pygame.display.update()


def collisions(ball, L_paddle, R_paddle):
    # Handle ball collisions with top and bottom walls
    ball_lmt_y = ball.y + ball.size
    ball_lmt_x = ball.x + ball.size
    lmt2 = ball.y - ball.size
    if ball_lmt_y >= height:
        ball.y_vel = ball.y_vel * (-1)
    elif lmt2 <= 0:
        ball.y_vel = ball.y_vel * (-1)

    # Handle ball collisions with left paddle
    L_lmt_y = L_paddle.y + L_paddle.ht
    L_lmt_x = L_paddle.x + L_paddle.wd
    R_lmt_y = R_paddle.y + R_paddle.ht
    if ball.x_vel < 0:
        if ball.y <= L_lmt_y and ball.y >= L_paddle.y:
            if L_lmt_x >= ball.x - ball.size:
                ball.x_vel = ball.x_vel * (-1)

                mid_y = L_lmt_y / 2
                difference_in_y = mid_y - ball.y
                reduction_factor = (L_paddle.ht / 2) / ball.max_vel
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    # Handle ball collisions with right paddle
    else:
        if ball.y >= R_paddle.y and ball.y <= R_lmt_y:
            if ball_lmt_x >= R_paddle.x:
                ball.x_vel *= -1

                mid_y = R_lmt_y / 2
                difference_in_y = mid_y - ball.y
                reduction_factor = (R_paddle.ht / 2) / ball.max_vel
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def paddle_movement_control(keys, L_paddle, R_paddle):
    if keys[pygame.K_w] and L_paddle.y - L_paddle.vel >= 0:
        L_paddle.move("up")
    if keys[pygame.K_s] and L_paddle.y + L_paddle.vel + L_paddle.ht <= height:
        L_paddle.move("down")
    if keys[pygame.K_UP] and R_paddle.y - R_paddle.vel >= 0:
        R_paddle.move("up")
    if keys[pygame.K_DOWN] and R_paddle.y + R_paddle.vel + R_paddle.ht <= height:
        R_paddle.move("down")


def main():  # main function
    flag = True
    clk = pygame.time.Clock()

    # giving dimensions
    L_paddle = Paddle(10, height//2 - paddle_ht //
                      2, paddle_wd, paddle_ht)
    R_paddle = Paddle(width - 10 - paddle_wd, height //
                      2 - paddle_ht//2, paddle_wd, paddle_ht)
    ball = Ball(width // 2, height // 2, size)

    L_score = 0
    R_score = 0

    while flag:
        clk.tick(FPS)
        draw(display, L_paddle, R_paddle,
             ball, L_score, R_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                break

        keys = pygame.key.get_pressed()
        paddle_movement_control(keys, L_paddle, R_paddle)

        ball.move()
        collisions(ball, L_paddle, R_paddle)

        if ball.x < 0:
            R_score += 1
            ball.reset()
        elif ball.x > width:
            L_score += 1
            ball.reset()

        victory = False
        if L_score >= win_score:
            victory = True
            window_text = "Left Player Won!"
        elif R_score >= win_score:
            victory = True
            window_text = "Right Player Won!"

        if victory:
            text = score_txt.render(window_text, 1, (200, 200, 200))
            display.blit(text, (width//2 - text.get_width() //
                                2, height//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            L_paddle.reset()
            R_paddle.reset()
            L_score = 0
            R_score = 0
    pygame.quit()


if __name__ == '__main__':
    main()

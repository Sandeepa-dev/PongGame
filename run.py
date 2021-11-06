import pygame, sys
from pygame.locals import *

def playerAnimation(key_pressed):
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    if key_pressed[pygame.K_UP]:
        player.y -= player_speed
    if key_pressed[pygame.K_DOWN]:
        player.y += player_speed

def opponentAnimation():
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    # Previous OpponentAI
    # if opponent.top <= ball.top:
    #     opponent.top += opponent_speed
    # if opponent.bottom >= ball.bottom:
    #     opponent.top -= opponent_speed

    # New opponentAI
    if opponent.centery > ball.centery:
        opponent.centery -= opponent_speed
    if opponent.centery < ball.centery:
        opponent.centery += opponent_speed


def ballAnimation():
    global ball_speed_x, ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -(ball_speed_y)
    if ball.left <= 0 or ball.right >= screen_width:
        ballRestart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x = -(ball_speed_x)
        
    ball.x += ball_speed_x
    ball.y += ball_speed_y


def ballRestart():
    ball.center = (screen_width/2, screen_height/2)

pygame.init()
fps_clock = pygame.time.Clock()

#Set up the window
screen_width, screen_height = 1280, 760
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# objs
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (screen_width/2, screen_height/2)
ball_speed_x, ball_speed_y = 9, 9

player = pygame.Rect(0, 0, 10, 140)
player.center = (screen_width - 20, screen_height / 2)
player_speed = 7

opponent = pygame.Rect(0, 0, 10, 140)
opponent.center = (20, screen_height / 2)
opponent_speed = 7

while True:

    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    key_pressed = pygame.key.get_pressed()
    playerAnimation(key_pressed)
    opponentAnimation()
    ballAnimation()

    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)

    pygame.display.update()
    fps_clock.tick(60)
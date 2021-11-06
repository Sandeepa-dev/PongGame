import pygame, sys
from pygame import display
from pygame.locals import *

def ballAnimation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ballRestart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def playerAnimation():
    # player.y += player_speed

    # if player.top <= 0:
    #     player.top = 0
    # if player.bottom >= screen_height:
    #     player.bottom = screen_height
    if player.top < ball.top:
        player.top += opponent_speed
    if opponent.bottom > ball.bottom:
        player.top -= opponent_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponentAI():
    if opponent.top < ball.top:
        opponent.top += opponent_speed
    if opponent.bottom > ball.bottom:
        opponent.top -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ballRestart():
    ball.center = (screen_width/2, screen_height/2)

pygame.init()
fps_clock = pygame.time.Clock()

#Set up the window
screen_width, screen_height = 1280, 760
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game
ball = pygame.Rect(0,0, 30, 30)
ball.center = (screen_width/2, screen_height/2)

player = pygame.Rect(screen_width - 20,screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10,screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x, ball_speed_y = 7, 7
player_speed = 0
opponent_speed = 7

while True:


    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ballAnimation()
    playerAnimation()
    opponentAI()


    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))

    # Update the window 
    pygame.display.update()
    fps_clock.tick(60)
import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Game")

BACKGROUND = [(135, 206, 250), (255, 182, 193), (230, 230, 250), (176, 224, 230), (255, 253, 208)]
PLAYER_COLOR = [(102, 51, 153), (54, 117, 136), (111, 78, 55), (220, 20, 60), (158, 180, 159)]

background_color = random.choice(BACKGROUND)
player_color = random.choice(PLAYER_COLOR)

player = pygame.Rect(100, 100, 50, 50)
speed = 10

run = True

while run:
    screen.fill(background_color)
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - speed >= 0:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.x + speed <= WIDTH - player.width:
        player.x += speed
    if keys[pygame.K_UP] and player.y - speed >= 0:
        player.y -= speed
    if keys[pygame.K_DOWN] and player.y + speed <= HEIGHT - player.height:
        player.y += speed
    if keys[pygame.K_q]:
        run = False
    pygame.draw.rect(screen, player_color, player)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python test")

# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# player = pygame.Rect(100, 100, 50, 50)
# speed = 5

# running = True

# while running:
#     screen.fill(WHITE)
#     for x in pygame.event.get():
#         if x.type == pygame.QUIT:
#             running = False
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         player.x -= speed
#     if keys[pygame.K_RIGHT]:
#         player.x += speed
#     if keys[pygame.K_UP]:
#         player.y -= speed
#     if keys[pygame.K_DOWN]:
#         player.y += speed
#     if keys[pygame.K_q]:
#         running = False
#     pygame.draw.rect(screen, RED, player)
#     pygame.display.flip()
#     pygame.time.Clock().tick(60)

BLUE = (9, 28, 87)
YELLOW = (255, 255, 0)

player = pygame.Rect(100, 100, 50, 50)
speed = 15

running = True

while running:
    screen.fill(BLUE)
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.y += speed
    if keys[pygame.K_q]:
        running = False
    pygame.draw.rect(screen, YELLOW, player)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    

pygame.quit()
sys.exit()


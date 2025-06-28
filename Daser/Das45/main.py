import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

sound = pygame.mixer.Sound("flap.mp3")

running = True
sound_playing = False

RED = (255, 0, 0)
player = pygame.Rect(10, 250, 50, 50)
speed = 5


while running:
    screen.blit(background, (0, 0))
    # mouse_pos = pygame.mouse.get_pos()
    # mouse_pressed = pygame.mouse.get_pressed()[0]

    # if mouse_pressed:
    #     if not sound_playing:
    #         sound.play(-1)
    #         sound_playing = True
    # else:
        # if sound_playing:
        #     sound.stop()
        #     sound_playing = False

    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_LEFT]:
        player.x -= speed
        moving = True
    if keys[pygame.K_RIGHT]:
        player.x += speed
        moving = True

    if moving and not sound_playing:
        sound.play(-1)
        sound_playing = True
    elif not moving and sound_playing:
        sound.stop()
        sound_playing = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen, RED, player)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()


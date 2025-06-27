import telebot
import pygame
import sys
import random

BOT_TOKEN = "7893466060:AAEaoAiG_wHUjIofxM8WbwwbKGRFRvN1P-o"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):

    pygame.init()

    WIDTH = 700
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Game")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    player = pygame.Rect(100, 100, 50, 50)
    speed = 10

    enemies = []
    for x in range(3):
        x = random.randint(0, WIDTH - 50)
        y = random.randint(0, HEIGHT - 50)
        enemies.append(pygame.Rect(x, y, 50, 50))

    run = True
    lost = False

    while run:
        screen.fill(WHITE)
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed
        if keys[pygame.K_UP]:
            player.y -= speed
        if keys[pygame.K_DOWN]:
            player.y += speed
        if keys[pygame.K_q]:
            run = False
        if player.x < 0 or player.x + player.width > WIDTH or player.y < 0 or player.y + player.height > HEIGHT:
            lost = True

        for enemy in enemies:
            if player.colliderect(enemy):
                lost = True

        pygame.draw.rect(screen, BLACK, player)
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)

        pygame.display.flip()
        pygame.time.Clock().tick(60)
        if lost:
            bot.reply_to(message, "Ցավում եմ դուք պարտվեցիք")
            run = False
    pygame.quit()
    sys.exit()


bot.polling()
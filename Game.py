import pygame
import math
import random

from pygame import mixer


# start af pygame
pygame.init()

# screen for spillet
screen = pygame.display.set_mode((800, 600))

# Baggrund
background = pygame.image.load('background.jpg')

#baggrunds musik
mixer.music.load('song.mp3')
mixer.music.play(-1)



# Title og Icon
pygame.display.set_caption("Pirate Invaders")
icon = pygame.image.load('whatthef.PNG')
pygame.display.set_icon(icon)

# spiller
heltImg = pygame.image.load('pirat64.png')
heltX = 370
heltY = 480
heltX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy2.png'))
    enemyX.append(random.randint(0, 734))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.1)
    enemyY_change.append(40)

# skyd

# read = not on screen
# fire = skyd kommer frem og bevæger

skydImg = pygame.image.load('bullet2.png')
skydX = 0
skydY = 480
skydX_change = 0
skydY_change = 0.3
skyd_state = "ready"

# scoreboard

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

#gameover text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def helt(x, y):
    screen.blit(heltImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_skyd(x, y):
    global skyd_state
    skyd_state = "fire"
    screen.blit(skydImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, skydX, skydY):
    distance = math.sqrt((math.pow(enemyX - skydX, 2)) + math.pow(enemyY - skydY, 2))
    if distance < 27:
        return True
    else:
        return False


# Loop
running = True

while running:

    # Farver for background
    screen.fill((0, 0, 0))
    # baggrund billed
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                heltX_change = -0.3
            if event.key == pygame.K_RIGHT:
                heltX_change = 0.3
            if event.key == pygame.K_SPACE:
                if skyd_state is "ready":
                    skyd_Sound = mixer.Sound('bshot.mp3')
                    skyd_Sound.play()

                    skydX = heltX
                    fire_skyd(skydX, skydY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                heltX_change = 0

    # boundry
    heltX += heltX_change

    if heltX <= 0:
        heltX = 0
    elif heltX >= 736:
        heltX = 736

    # enemy movement
    enemyX += enemyX_change

    for i in range(num_of_enemies):

        #game over
        if enemyY[i] > 200:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.1
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], skydX, skydY)
        if collision:
            explosion_Sound = mixer.Sound('whack.mp3')
            explosion_Sound.play()
            skydY = 480
            skyd_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 734)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet move
    if skydY <= 0:
        skydY = 480
        skyd_state = "ready"

    if skyd_state is "fire":
        fire_skyd(skydX, skydY)
        skydY -= skydY_change

    helt(heltX, heltY)
    show_score(textX, textY)
    pygame.display.update()

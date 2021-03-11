import pygame


pygame.init()

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("SpaceInvader")
icon = pygame.image.load('whatthef.PNG')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('pirat64.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg,(playerX, playerY))


running = True
while running:

    #Background
    screen.fill((0, 90, 55))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()

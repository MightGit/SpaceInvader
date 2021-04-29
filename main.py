import pygame

class Game:
    screen = None
    aliens = []
    shots = []
    lost = False


    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        helt = Helt(self, width / 2, height - 20)
        generator = Generator(self)
        shot = None

        while not done:
            if len(self.aliens) == 0:
                self.displayText("VICTORY ACHIEVED")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                helt.x -= 2 if helt.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                helt.x += 2 if helt.x < width - 20 else 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.shot.append(Shot(self, helt.x, helt.y))


class Generator:
    def __init__(self, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))

class Shot:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (254, 52, 110),
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2

class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 30

    def draw(self):
        pygame.draw.rect(self.game.screen,  # renderovací plocha
                         (81, 43, 88),  # barva objektu
                         pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05

    def checkCollision(self, game):
        for shot in game.shots:
            if (shot.x < self.x + self.size and
                    shot.x > self.x - self.size and
                    shot.y < self.y + self.size and
                    shot.y > self.y - self.size):
                game.shot.remove(shot)
                game.aliens.remove(self)

pygame.init()

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("SpaceInvader")
icon = pygame.image.load('whatthef.PNG')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('pirat64.png')
playerX = 370
playerY = 480

class Helt:

    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y


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


class RocketClass:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (254, 52, 110),
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2

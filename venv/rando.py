import  pygame


class  Game :
    screen = None
    aliens = []
    rockets = []
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
        rocket = None

        while not done:
            if len(self.aliens) == 0:
                self.displayText("VICTORY ACHIEVED")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  # sipka doleva
                helt . x  -=  2  if  helt . x  >  20  else  0   # left area boundary
            elif  pressed [ pygame . K_RIGHT ]:   # right arrow
                helt.x += 2 if helt.x < width - 20 else 0  # prava hranice

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, helt.x, helt.y))

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)
                if (alien.y > height):
                    self.lost = True
                    self.displayText("YOU DIED")

            for rocket in self.rockets:
                rocket.draw()

            if not self.lost: helt.draw()

    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.screen.blit(textsurface, (110, 160))


class  Alien :
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self . y  =  y
        self.size = 30

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         ( 81 , 43 , 88 ),
                         pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                    rocket.x > self.x - self.size and
                    rocket.y < self.y + self.size and
                    rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                game.aliens.remove(self)


class Helt:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self . y  =  y

    def draw(self):

        pygame.draw.rect(self.game.screen,
                         (210, 0, 251),
                         pygame.Rect(self.x, self.y, 8, 5))



class  Generator :
    def __init__(self, game):
        margin  =  30   # space from the edge of the screen
        width  =  50   # space between aliens
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))

        # game.aliens.append(Alien(game, 280, 50))


class Rocket:
    def __init__(self, game, x, y):
        self.x = x
        self . y  =  y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,  # renderovací plocha
                         ( 254 , 52 , 110 ),   # object color
                         pygame.Rect(self.x, self.y, 2, 4))
        self . y  -=  2   # will fly up 2px / frame on the playing area



def game_loop():
    pygame.mixer.music.play(-1)

if __name__ == '__main__':
    game = Game(800, 800)



import pygame

class Game:
    screen = None
    enemy = []
    score = []
    helt = []

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False


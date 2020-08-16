import pygame

X_SIZE = 1280
Y_SIZE = 800
class Board:
    def __init__(self, drawables):
        pygame.init()
        clock = pygame.time.Clock()
        clock.tick(60)
        self.screen = pygame.display.set_mode((X_SIZE, Y_SIZE))
        self.items = drawables

    def print(self):
        self.screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        for item in self.items:
            pygame.draw.circle(self.screen, item.color, (int(item.x), int(item.y)),int(item.radius))
        pygame.display.flip()

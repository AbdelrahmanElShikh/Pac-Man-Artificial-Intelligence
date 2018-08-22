import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,9))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
            
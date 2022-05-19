import pygame


class Hamburguer(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.surface.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load("assets/hamburguer.png").convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (150, 150))
        self.__surface = surface

    @property
    def image(self) -> pygame.surface.Surface:
        return self.__image

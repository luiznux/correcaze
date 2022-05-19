import pygame

from typing import Tuple

from classes.coodinates import Coordinates
from contants import HEIGHT


class Weight(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.surface.Surface, position: Coordinates):
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load("assets/weight.png").convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (200, 150))
        self.__surface = surface
        self.__position = position

    def go_down(self) -> None:
        self.__position.y = self.__position.y + 5

    def is_over_screen(self) -> bool:
        return self.__position.y > (HEIGHT - self.__image.get_height())

    @property
    def image(self) -> pygame.surface.Surface:
        return self.__image

    @property
    def position(self) -> Tuple[int, int]:
        return (self.__position.x, self.__position.y)

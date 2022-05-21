from typing import Optional, Tuple
import pygame

from classes.coodinates import Coordinates


class Caze(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.surface.Surface):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("assets/caze_placeholder.png").convert_alpha()
        self.__image = pygame.transform.scale(image, (200, 200))
        self.__surface = surface
        self.__stamina = 100
        self._speed = 10
        self._lane = 1
        self.__points = 0
        self.__coordinates: Tuple[int, int] = (0, 0)

    def render(self, coordinates: Tuple[int, int]):
        self.__coordinates = coordinates
        self.__surface.blit(self.__image, coordinates)

    def increase_points(self) -> None:
        self.__points += 10

    def decrease_points(self) -> None:
        self.__points -= 10

    def increase_stamina(self) -> None:
        self.__stamina += 10

    def decrease_stamina(self) -> None:
        self.__stamina -= 10

    def change_lane(self, direction: str):
        if direction == "left":
            self.move_left()
        else:
            self.move_right()

    def move_left(self):
        if self._lane - 1 < 0:
            pass
        else:
            self._lane -= 1

    def move_right(self):
        if self._lane + 1 > 2:
            pass
        else:
            self._lane += 1

    @property
    def points(self):
        return self.__points

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def lane(self):
        return self._lane

    @property
    def stamina(self):
        return self.__stamina

    @property
    def coordinates(self) -> Tuple[int, int]:
        return self.__coordinates

    def get_height(self) -> int:
        return self.__image.get_height()

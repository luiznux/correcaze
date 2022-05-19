from typing import Tuple
import pygame

from classes.caze import Caze
from classes.hamburguer import Hamburguer
from contants import LANES_POSITION


class Game:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self.__caze = Caze(surface)
        self.__lanes = self.__initialize_lanes()

    def render(self):
        self.__draw_lanes()
        self.__surface.blit(
            self.__caze.image,
            (LANES_POSITION[self.__caze.lane], self.__caze.get_height()),
        )
        hamburguer = Hamburguer(self.__surface)
        self.__surface.blit(
            hamburguer.image,
            (
                LANES_POSITION[self.__caze.lane] + (self.__caze.get_height() / 2),
                hamburguer.image.get_height(),
            ),
        )

    def move_caze(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.__caze.change_lane("left")
            if event.key == pygame.K_RIGHT:
                self.__caze.change_lane("right")

    def __initialize_lanes(self) -> Tuple[pygame.Rect, pygame.Rect, pygame.Rect]:
        lanes_width = (self.__surface.get_width() - 200) / 3
        lanes_height = self.__surface.get_height() - 10
        return (
            pygame.Rect(100, 200, lanes_width, lanes_height),
            pygame.Rect(100 + lanes_width, 200, lanes_width, lanes_height),
            pygame.Rect(100 + lanes_width * 2 - 1, 200, lanes_width, lanes_height),
        )

    def __draw_lanes(self):
        pygame.draw.rect(self.__surface, color=(220, 20, 10), rect=self.__lanes[0])
        pygame.draw.rect(self.__surface, color=(180, 60, 160), rect=self.__lanes[1])
        pygame.draw.rect(self.__surface, color=(140, 80, 250), rect=self.__lanes[2])

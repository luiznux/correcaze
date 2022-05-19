from typing import List, Tuple
from random import randint
import pygame

from classes.caze import Caze
from classes.coodinates import Coordinates
from classes.hamburguer import Hamburguer, Weight
from contants import HEIGHT, LANES_POSITION


class Game:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self.__caze = Caze(surface)
        self.__lanes = self.__initialize_lanes()
        self.__lane_obstacles: List[Hamburguer] = []
        self.__lane_objects: List[Weight] = []

    def render(self):
        self.__draw_lanes()
        # TODO: Mover isso para um método na classe cazé
        self.__surface.blit(
            self.__caze.image,
            (LANES_POSITION[self.__caze.lane], HEIGHT-self.__caze.get_height()),
        )

        for index, obstacle in enumerate(self.__lane_obstacles):
            if obstacle.is_over_screen():
                self.__lane_obstacles.pop(index)

        if len(self.__lane_obstacles) == 0:
            random_lane = randint(0, 2)
            x = LANES_POSITION[random_lane]
            y = 20
            self.__lane_obstacles.append(
                Hamburguer(self.__surface, Coordinates(x, y))
            )
        else:
            for obstacle in self.__lane_obstacles:
                obstacle.go_down()

        # TODO: Mover isso para um método na classe Hamburguer
        for obstacle in self.__lane_obstacles:
            self.__surface.blit(obstacle.image, (obstacle.position))

        for index, object in enumerate(self.__lane_objects):
            if object.is_over_screen():
                self.__lane_objects.pop(index)

        if len(self.__lane_objects) == 0:
            random_lane = randint(0, 2)
            x = LANES_POSITION[random_lane]
            y = 20
            self.__lane_objects.append(
                Weight(self.__surface, Coordinates(x, y))
            )
        else:
            for object in self.__lane_objects:
                object.go_down()

        # TODO: Mover isso para um método na classe Hamburguer
        for object in self.__lane_objects:
            self.__surface.blit(object.image, (object.position))

    def update() -> None:
        pass

    # TODO: Depois esse método deve ser movido pro Cazé, não faz
    # sentido estar exposto aqui.
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

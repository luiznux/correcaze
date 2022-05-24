from typing import Tuple

import pygame


class Caze(pygame.sprite.Sprite):
    MAX_STAMINA = 200

    def __init__(self, surface: pygame.surface.Surface):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("assets/images/caze_placeholder.png").convert_alpha()
        self.__image = pygame.transform.scale(image, (200, 200))
        self.__surface = surface
        self.__stamina = 100
        self._speed = 10
        self._lane = 1
        self.__points = 0
        self.__coordinates: Tuple[int, int] = (0, 0)
        self.__rendered_image: pygame.rect.Rect = pygame.rect.Rect(
            self.__coordinates[0],
            self.__coordinates[1],
            self.__image.get_width(),
            self.__image.get_height(),
        )

    def render(self, coordinates: Tuple[int, int]):
        self.__coordinates = coordinates
        self.__rendered_image = self.__surface.blit(self.__image, coordinates)

    def run(self) -> None:
        self.__stamina -= 0.1

    def rendered_caze(self) -> pygame.rect.Rect:
        return self.__rendered_image

    def increase_points_for_salad(self) -> None:
        self.__points += 5

    def increase_points_for_weight(self) -> None:
        self.__points += 10

    def decrease_points(self) -> None:
        self.__points -= 10

    def increase_stamina(self) -> None:
        if self.__stamina < self.MAX_STAMINA:
            # Se o aumento ultrapassa o limite então maximiza a
            # stamina.
            if (self.__stamina + 10) > self.MAX_STAMINA:
                self.__stamina = self.MAX_STAMINA
            else:
                self.__stamina += 10

    def decrease_stamina(self) -> None:
        self.__stamina -= 10

    def is_out_of_stamina(self) -> bool:
        return self.__stamina <= 0

    def on_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.__change_lane("left")
            if event.key == pygame.K_RIGHT:
                self.__change_lane("right")

    def __change_lane(self, direction: str):
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

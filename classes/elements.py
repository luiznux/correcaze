from typing import Optional, Tuple
import pygame

from classes.coodinates import Coordinates
from contants import HEIGHT


class LaneElement(pygame.sprite.Sprite):
    def __init__(
        self,
        surface: pygame.surface.Surface,
        position: Coordinates,
        image: pygame.surface.Surface,
    ):
        pygame.sprite.Sprite.__init__(self)
        self.__image = image
        self.__surface = surface
        self.__position = position
        self.__rendered_element: Optional[pygame.rect.Rect] = None

    def go_down(self) -> None:
        self.__position.y = self.__position.y + 5

    def is_over_screen(self) -> bool:
        return self.__position.y > (HEIGHT + self.__image.get_height())

    def collided_with(self, rect: pygame.rect.Rect) -> bool:
        if self.__rendered_element is None:
            return False
        return self.__rendered_element.colliderect(rect)

    def render(self) -> None:
        self.__rendered_element = self.__surface.blit(
            self.__image, (self.position_as_tuple)
        )

    @property
    def image(self) -> pygame.surface.Surface:
        return self.__image

    @property
    def position_as_tuple(self) -> Tuple[int, int]:
        return (self.__position.x, self.__position.y)

    @property
    def position(self) -> Coordinates:
        return self.__position


class Hamburguer(LaneElement):
    def __init__(self, surface: pygame.surface.Surface, position: Coordinates):
        image = pygame.image.load("assets/images/hamburguer.png").convert_alpha()
        image = pygame.transform.scale(image, (150, 150))
        super().__init__(surface, position, image)


class Weight(LaneElement):
    def __init__(self, surface: pygame.surface.Surface, position: Coordinates):
        image = pygame.image.load("assets/images/weight.png").convert_alpha()
        image = pygame.transform.scale(image, (200, 150))
        super().__init__(surface, position, image)

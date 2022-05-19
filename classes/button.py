import pygame
from classes import coodinates

from contants import *

from classes.coodinates import Coordinates


class Button:
    def __init__(
        self,
        surface: pygame.surface.Surface,
        text: str,
        coordinates: Coordinates,
        width: int,
    ):
        self.__surface = surface
        self.__font = pygame.font.SysFont("Monaco", 40)
        self.__text = text
        self.__color = (255, 0, 0)
        self.__button = pygame.Rect((coordinates.x, coordinates.y, width, 100))

    def was_clicked(self, event: pygame.event.Event) -> bool:
        if event.type != pygame.MOUSEBUTTONUP:
            return False

        mouse_position = pygame.mouse.get_pos()
        return self.__button.collidepoint(mouse_position)

    def render_button_with_centralized_text(self):
        pygame.draw.rect(self.__surface, self.__color, self.__button)
        text_surface = self.__font.render(self.__text, True, (0, 0, 0))

        width_margin, height_margin = self.__calculate_button_margins(
            self.__button, text_surface
        )

        self.__surface.blit(
            text_surface,
            (self.__button.x + width_margin, self.__button.y + height_margin),
        )

    def __calculate_button_margins(
        self, button: pygame.Rect, text: pygame.surface.Surface
    ):
        width_margin = int((button.width - text.get_width()) / 2)
        height_margin = int((button.height - text.get_height()) / 2)
        return width_margin, height_margin

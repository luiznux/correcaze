from typing import Optional

import pygame

from button import Button
from coodinates import Coordinates
from constants import *


class Credits:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self.__button_font = pygame.font.SysFont("Monaco", 40)
        self.__menu_button: Optional[Button] = None

    def render(self):
        title_surface = self.__render_title()
        self.__render_centralized_text(title_surface, "Edison Aguiar - 31812295", 150)
        self.__render_centralized_text(title_surface, "Lucas Morita - 31826199", 200)
        self.__render_centralized_text(
            title_surface, "Luiz Tagliaferro - 31861806", 250
        )
        self.__render_centralized_text(
            title_surface, "Raphael Prandini - 31828728", 300
        )
        self.__menu_button = Button(
            self.__surface,
            "Voltar",
            Coordinates(title_surface.x, 450),
            title_surface.width,
        )
        self.__menu_button.render_button_with_centralized_text()

    def clicked_on_menu(self, event: pygame.event.Event) -> bool:
        if self.__menu_button is None:
            return False
        return self.__menu_button.was_clicked(event)

    def __render_title(self) -> pygame.rect.Rect:
        title_font = pygame.font.SysFont("Monaco", 60)
        title_surface = title_font.render("Créditos", True, (0, 0, 0))
        title_surface_x = (WIDTH / 2) - (title_surface.get_width() / 2)
        return self.__surface.blit(title_surface, (title_surface_x, 100))

    def __render_centralized_text(
        self, title_surface: pygame.rect.Rect, text: str, y: int
    ):
        button = pygame.Rect((title_surface.x, y, title_surface.width, 100))
        text_surface = self.__button_font.render(text, True, (0, 0, 0))

        width_margin, height_margin = self.__calculate_text_margins(
            button, text_surface
        )

        self.__surface.blit(
            text_surface,
            (button.x + width_margin, button.y + height_margin),
        )

    def __calculate_text_margins(
        self, button: pygame.Rect, text: pygame.surface.Surface
    ):
        width_margin = int((button.width - text.get_width()) / 2)
        height_margin = int((button.height - text.get_height()) / 2)
        return width_margin, height_margin

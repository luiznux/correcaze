from typing import Optional
import pygame

from contants import *

from classes.button import Button
from classes.coodinates import Coordinates


class Menu:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self.__start_button: Optional[Button] = None
        self.__credits_button: Optional[Button] = None
        self.__quit_button: Optional[Button] = None

    def clicked_on_start_game(self, event: pygame.event.Event) -> bool:
        if self.__start_button is None:
            return False
        return self.__start_button.was_clicked(event)

    def clicked_on_credits(self, event: pygame.event.Event) -> bool:
        if self.__credits_button is None:
            return False
        return self.__credits_button.was_clicked(event)

    def clicked_on_quit(self, event: pygame.event.Event) -> bool:
        if self.__quit_button is None:
            return False
        return self.__quit_button.was_clicked(event)

    def render(self):
        title_surface = self.__render_main_title()
        self.__render_start_game_button(title_surface)
        self.__render_credits_button(title_surface)
        self.__render_quit_button(title_surface)

    def __render_main_title(self) -> pygame.rect.Rect:
        title_font = pygame.font.SysFont("Monaco", 60)
        title_surface = title_font.render("Corre Cazé", True, (0, 0, 0))
        # Define o X como o meio da tela
        title_surface_x = (WIDTH / 2) - (title_surface.get_width() / 2)
        return self.__surface.blit(title_surface, (title_surface_x, 100))

    def __render_start_game_button(self, title_surface: pygame.rect.Rect):
        self.__start_button = Button(
            self.__surface,
            "Iniciar Jogo",
            Coordinates(title_surface.x, 150),
            title_surface.width,
        )
        self.__start_button.render_button_with_centralized_text()

    def __render_credits_button(self, title_surface: pygame.rect.Rect):
        self.__credits_button = Button(
            self.__surface,
            "Créditos",
            Coordinates(title_surface.x, 300),
            title_surface.width,
        )
        self.__credits_button.render_button_with_centralized_text()

    def __render_quit_button(self, title_surface: pygame.rect.Rect):
        self.__quit_button = Button(
            self.__surface,
            "Sair",
            Coordinates(title_surface.x, 450),
            title_surface.width,
        )
        self.__quit_button.render_button_with_centralized_text()

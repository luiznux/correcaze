import pygame

from contants import *


class Menu:
    def __init__(self, surface: pygame.surface.Surface):
        self._surface = surface
        self._button_font = pygame.font.SysFont("Monaco", 40)

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
        return self._surface.blit(title_surface, (title_surface_x, 100))

    def __render_start_game_button(self, title_surface: pygame.rect.Rect):
        self.__render_centralized_button(title_surface, "Iniciar Jogo", 150)

    def __render_credits_button(self, title_surface: pygame.rect.Rect):
        self.__render_centralized_button(title_surface, "Créditos", 300)

    def __render_quit_button(self, title_surface: pygame.rect.Rect):
        self.__render_centralized_button(title_surface, "Sair", 450)

    def __render_centralized_button(
        self, title_surface: pygame.rect.Rect, text: str, y: int
    ):
        button = pygame.Rect((title_surface.x, y, title_surface.width, 100))
        pygame.draw.rect(self._surface, (255, 0, 0), button)
        text_surface = self._button_font.render(text, True, (0, 0, 0))

        width_margin, height_margin = self.__calculate_button_margins(
            button, text_surface
        )

        self._surface.blit(
            text_surface,
            (button.x + width_margin, button.y + height_margin),
        )

    def __calculate_button_margins(
        self, button: pygame.Rect, text: pygame.surface.Surface
    ):
        width_margin = int((button.width - text.get_width()) / 2)
        height_margin = int((button.height - text.get_height()) / 2)
        return width_margin, height_margin

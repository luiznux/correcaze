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
        start_game_button = pygame.Rect((title_surface.x, 150, title_surface.width, 100))
        pygame.draw.rect(self._surface, (255, 0, 0), start_game_button)
        start_game_text = self._button_font.render("Iniciar Jogo", True, (0, 0, 0))

        width_margin, height_margin = self.__calculate_button_margins(
            start_game_button, start_game_text)

        self._surface.blit(start_game_text, (start_game_button.x + width_margin,
                                       start_game_button.y + height_margin))

    def __render_credits_button(self, title_surface: pygame.rect.Rect):
        credits_button = pygame.Rect((title_surface.x, 300, title_surface.width, 100))
        pygame.draw.rect(self._surface, (255, 0, 0), credits_button)
        credits_text = self._button_font.render("Créditos", True, (0, 0, 0))
        width_margin, height_margin = self.__calculate_button_margins(
            credits_button, credits_text)
        self._surface.blit(credits_text, (credits_button.x + width_margin,
                                    credits_button.y + height_margin))

    def __render_quit_button(self, title_surface: pygame.rect.Rect):
        quit_button = pygame.Rect((title_surface.x, 450, title_surface.width, 100))
        pygame.draw.rect(self._surface, (255, 0, 0), quit_button)
        quit_text = self._button_font.render("Sair", True, (0, 0, 0))
        width_margin, height_margin = self.__calculate_button_margins(
            quit_button, quit_text)
        self._surface.blit(quit_text, (quit_button.x + width_margin,
                                 quit_button.y + height_margin))

    def __calculate_button_margins(self, button: pygame.Rect,
                                   text: pygame.surface.Surface):
        width_margin = int((button.width - text.get_width()) / 2)
        height_margin = int((button.height - text.get_height()) / 2)
        return width_margin, height_margin


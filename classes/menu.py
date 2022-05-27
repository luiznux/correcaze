from typing import Optional

import pygame
from constants import *

from classes.button import Button
from classes.coodinates import Coordinates
from classes.rank import Ranking


class Menu:
    def __init__(self, surface: pygame.surface.Surface, title: str):
        self.__surface = surface
        self.__start_button: Optional[Button] = None
        self.__credits_button: Optional[Button] = None
        self.__quit_button: Optional[Button] = None
        self.__ranking_button: Optional[Button] = None
        self.__title = title

    def clicked_on_start_game(self, event: pygame.event.Event) -> bool:
        if self.__start_button is None:
            return False
        return self.__start_button.was_clicked(event)

    def clicked_on_credits(self, event: pygame.event.Event) -> bool:
        if self.__credits_button is None:
            return False
        return self.__credits_button.was_clicked(event)

    def clicked_on_ranking(self, event: pygame.event.Event) -> bool:
        if self.__ranking_button is None:
            return False
        return self.__ranking_button.was_clicked(event)

    def clicked_on_quit(self, event: pygame.event.Event) -> bool:
        if self.__quit_button is None:
            return False
        return self.__quit_button.was_clicked(event)

    def clicked_on_mute(self, event: pygame.event.Event) -> bool:
        if self.__sound_button is None:
            return False
        return self.__sound_button.was_clicked(event)

    def render(self, start_game_text: str):
        title_surface = self._render_main_title()
        self.__render_start_game_button(title_surface, start_game_text)
        self.__render_credits_button(title_surface)
        self.__render_ranking_button(title_surface)
        self._render_quit_button(title_surface)
        self._render_sound_buttun(title_surface)

    def _render_main_title(self) -> pygame.rect.Rect:
        title_font = pygame.font.SysFont("Monaco", 60)
        title_surface = title_font.render(self.__title, True, (0, 0, 0))
        # Define o X como o meio da tela
        title_surface_x = (WIDTH / 2) - (title_surface.get_width() / 2)
        return self.__surface.blit(title_surface, (title_surface_x, 100))

    def __render_start_game_button(self, title_surface: pygame.rect.Rect, text: str):
        self.__start_button = Button(
            self.__surface,
            text,
            Coordinates(title_surface.x, 150),
            title_surface.width,
        )
        self.__start_button.render_button_with_centralized_text(text)

    def __render_credits_button(self, title_surface: pygame.rect.Rect):
        self.__credits_button = Button(
            self.__surface,
            "Créditos",
            Coordinates(title_surface.x, 300),
            title_surface.width,
        )
        self.__credits_button.render_button_with_centralized_text()

    def __render_ranking_button(self, title_surface: pygame.rect.Rect):
        self.__ranking_button = Button(
            self.__surface,
            "Ranking",
            Coordinates(title_surface.x, 450),
            title_surface.width,
        )
        self.__ranking_button.render_button_with_centralized_text()

    def _render_quit_button(self, title_surface: pygame.rect.Rect):
        self.__quit_button = Button(
            self.__surface,
            "Sair",
            Coordinates(title_surface.x, 600),
            title_surface.width,
        )
        self.__quit_button.render_button_with_centralized_text()

    def _render_sound_buttun(self, title_surface: pygame.rect.Rect):
        self.__sound_button = Button(
            self.__surface,
            "Mute",
            Coordinates(WIDTH-200, HEIGHT-200),
            width=200,
            height=200
        )
        self.__sound_button.render_button_with_centralized_text()


class PauseMenu(Menu):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface, "Jogo Pausado")

    def render(self):
        super().render("Voltar ao jogo")


class InitialMenu(Menu):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface, "Corre Cazé")

    def render(self):
        super().render("Iniciar Jogo")


class LoserMenu(Menu):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface, "Você perdeu!")
        self.__surface = surface
        self.__saved_ranking = False
        self.__menu_button: Optional[Button] = None
        self.__save_rank_button: Optional[Button] = None
        self.player_name = ""

    def render(self):
        title_surface = self._render_main_title()
        self.__render_player_input(title_surface)
        self.__render_save_ranking_button(title_surface)
        self.__render_menu_button(title_surface)
        self._render_quit_button(title_surface)

    def on_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]
            else:
                if len(self.player_name) <= 12:
                    self.player_name = self.player_name + event.unicode

    def clicked_on_menu(self, event: pygame.event.Event) -> bool:
        if self.__menu_button is None:
            return False
        return self.__menu_button.was_clicked(event)

    def clicked_on_save_ranking(self, event: pygame.event.Event) -> bool:
        if self.__save_rank_button is None:
            return False

        if self.__save_rank_button.was_clicked(event):
            self.__saved_ranking = True
            return True

        return False

    def __render_player_input(self, title_surface: pygame.rect.Rect) -> None:
        player_input = Button(
            self.__surface,
            self.player_name,
            Coordinates(title_surface.x, 150),
            title_surface.width,
            color=(0, 0, 0),
            font_color=(255, 255, 255),
        )
        player_input.render_button_with_centralized_text()

    def __render_save_ranking_button(self, title_surface: pygame.rect.Rect) -> None:
        if self.__saved_ranking:
            color = (128, 0, 0)
            text = "Salvo"
        else:
            color = (255, 0, 0)
            text = "Salvar"

        self.__save_rank_button = Button(
            self.__surface,
            text,
            Coordinates(title_surface.x, 300),
            title_surface.width,
            color,
        )
        self.__save_rank_button.render_button_with_centralized_text()

    def __render_menu_button(self, title_surface: pygame.rect.Rect) -> None:
        self.__menu_button = Button(
            self.__surface,
            "Menu",
            Coordinates(title_surface.x, 450),
            title_surface.width,
        )
        self.__menu_button.render_button_with_centralized_text()


class RankMenu(Menu):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface, "Ranking (Top 5)")
        self.__surface = surface
        self.__menu_button: Optional[Button] = None
        self.__ranking = Ranking()
        self.__font = pygame.font.SysFont("Monaco", 40)

    def render(self) -> None:
        title_surface = self._render_main_title()
        self.__render_rankings(title_surface)
        self.__render_menu_button(title_surface)

    def clicked_on_menu(self, event: pygame.event.Event) -> bool:
        if self.__menu_button is None:
            return False
        return self.__menu_button.was_clicked(event)

    def __render_rankings(self, title_surface: pygame.rect.Rect) -> None:
        rankings = sorted(
            self.__ranking.read_scoreboard(),
            key=lambda player: player.points,
            reverse=True,
        )
        backoff = 0
        for ranking in rankings[:5]:
            self.__render_centralized_text(
                title_surface, f"{ranking.name} - {ranking.points}", 150 + backoff
            )
            backoff += 50

    def __render_centralized_text(
        self, title_surface: pygame.rect.Rect, text: str, y: int
    ):
        button = pygame.Rect((title_surface.x, y, title_surface.width, 100))
        text_surface = self.__font.render(text, True, (0, 0, 0))

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

    def __render_menu_button(self, title_surface: pygame.rect.Rect) -> None:
        self.__menu_button = Button(
            self.__surface,
            "Voltar",
            Coordinates(title_surface.x, 550),
            title_surface.width,
        )
        self.__menu_button.render_button_with_centralized_text()

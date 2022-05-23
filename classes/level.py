from enum import Enum
from typing import Tuple

import pygame
from constants import BLACK, HEIGHT, RED, WHITE, WIDTH


class Level(Enum):
    One = 1
    Two = 2
    Three = 3


class LevelBar:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self.__surface = surface
        self.__font = pygame.font.SysFont("Monaco", 30)

    def render(self, level: Level) -> None:
        text = self.__font.render(f"Nível: {level.value}", True, BLACK)
        # Renderiza a quantidade de pontos no centro do eixo x da
        # tela.
        self.__surface.blit(text, (WIDTH - text.get_rect().width, 0))


class LevelTransition:
    def __init__(self, surface: pygame.surface.Surface, level: Level) -> None:
        self._surface = surface
        self.__title_font = pygame.font.SysFont("Monaco", 100)
        self._instructions_font = pygame.font.SysFont("Monaco", 25)
        self._background = self.__create_background()
        self._title = self.__title_font.render(f"Nível {level.value}", True, WHITE)

    def render(self) -> None:
        pass

    def _render(self) -> None:
        self.__render_background()
        self.__render_title()
        self.__render_continue_text()

    def __create_background(self) -> pygame.rect.Rect:
        width = WIDTH / 3
        height = HEIGHT / 3
        return pygame.rect.Rect(
            WIDTH / 2 - width / 2, HEIGHT / 2 - height / 2, width, height
        )

    def __render_background(self) -> None:
        pygame.draw.rect(self._surface, BLACK, self._background)

    def __render_continue_text(self) -> None:
        width_margin, _ = self.__calculate_margin_for_title()

        text = self._instructions_font.render(
            "Pressione enter pra continuar", True, RED
        )

        self._surface.blit(
            text,
            (
                self._background.x + width_margin,
                self._background.y + self._background.height - text.get_height(),
            ),
        )

    def __render_title(self):
        width_margin, height_margin = self.__calculate_margin_for_title()

        self._surface.blit(
            self._title,
            (self._background.x + width_margin, self._background.y + height_margin),
        )

    def __calculate_margin_for_title(self) -> Tuple[int, int]:
        width_margin = int((self._background.width - self._title.get_width()) / 2)
        height_margin = int((self._background.height - self._title.get_height()) / 8)
        return width_margin, height_margin

    def _calculate_margin_for_instructions(
        self, line_text: pygame.surface.Surface
    ) -> Tuple[int, int]:
        width_margin = int((self._background.width - line_text.get_width()) / 2)
        height_margin = int(
            (self._background.height - self._instructions_font.get_height()) / 2
        )
        return width_margin, height_margin


class LevelOneTransition(LevelTransition):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface, Level.One)
        self._first_line = self._instructions_font.render(
            "Fuja das comidas não saudáveis",
            True,
            WHITE,
        )
        self._second_line = self._instructions_font.render(
            "Pegue as comidas saudáveis",
            True,
            WHITE,
        )

    def render(self) -> None:
        self._render()
        self._render_instructions()

    def _render_instructions(self) -> None:
        self._render_first_line()
        self._render_second_line()

    def _render_first_line(self):
        width_margin, height_margin = self._calculate_margin_for_instructions(
            self._first_line
        )

        self._surface.blit(
            self._first_line,
            (
                self._background.x + width_margin,
                self._background.y + height_margin + self._title.get_height() / 2,
            ),
        )

    def _render_second_line(self):
        width_margin, height_margin = self._calculate_margin_for_instructions(
            self._second_line
        )

        self._surface.blit(
            self._second_line,
            (
                self._background.x + width_margin,
                self._background.y
                + height_margin
                + self._title.get_height() / 2
                + self._instructions_font.get_height(),
            ),
        )


class LevelTwoTransition(LevelTransition):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface, Level.Two)
        self.__level_one_transition = LevelOneTransition(surface)
        self._third_line = self._instructions_font.render(
            "Pegue os halteres para ganhar mais pontos",
            True,
            WHITE,
        )

    def render(self) -> None:
        super()._render()
        self.__level_one_transition._render_instructions()
        self._render_instructions()

    def _render_instructions(self) -> None:
        self._render_third_line()

    def _render_third_line(self):
        width_margin, height_margin = self._calculate_margin_for_instructions(
            self._third_line
        )

        self._surface.blit(
            self._third_line,
            (
                self._background.x + width_margin,
                self._background.y
                + height_margin
                + self._title.get_height() / 2
                + self._instructions_font.get_height() * 2,
            ),
        )


class LevelThreeTransition(LevelTransition):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface, Level.Three)
        self.__level_one_transition = LevelOneTransition(surface)
        self.__level_two_transition = LevelTwoTransition(surface)
        self._fourth_line = self._instructions_font.render(
            "Agora o cazé está mais rápido!",
            True,
            WHITE,
        )

    def render(self) -> None:
        super()._render()
        self.__level_one_transition._render_instructions()
        self.__level_two_transition._render_instructions()
        self._render_fourth_line()

    def _render_fourth_line(self):
        width_margin, height_margin = self._calculate_margin_for_instructions(
            self._fourth_line
        )

        self._surface.blit(
            self._fourth_line,
            (
                self._background.x + width_margin,
                self._background.y
                + height_margin
                + self._title.get_height() / 2
                + self._instructions_font.get_height() * 3,
            ),
        )

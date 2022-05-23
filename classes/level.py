from enum import Enum
from typing import Tuple

import pygame
from contants import BLACK, HEIGHT, WHITE, WIDTH


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
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self._surface = surface
        self.__title_font = pygame.font.SysFont("Monaco", 100)
        self._instructions_font = pygame.font.SysFont("Monaco", 25)

    def render(self, level: Level) -> None:
        pass

    def _render(self, level: Level) -> Tuple[pygame.rect.Rect, pygame.surface.Surface]:
        background = self._render_background()
        title = self.__render_title(background, level)
        return background, title

    def __render_title(
        self, background: pygame.rect.Rect, level: Level
    ) -> pygame.surface.Surface:
        title = self.__title_font.render(f"Nível {level.value}", True, WHITE)
        width_margin, height_margin = self.__calculate_margin_for_title(
            background, title
        )

        self._surface.blit(
            title, (background.x + width_margin, background.y + height_margin)
        )
        return title

    def _render_background(self) -> pygame.rect.Rect:
        width = WIDTH / 3
        height = HEIGHT / 4
        rect = pygame.rect.Rect(
            WIDTH / 2 - width / 2, HEIGHT / 2 - height / 2, width, height
        )
        return pygame.draw.rect(self._surface, BLACK, rect)

    def __calculate_margin_for_title(
        self, rect: pygame.rect.Rect, title: pygame.surface.Surface
    ) -> Tuple[int, int]:
        width_margin = int((rect.width - title.get_width()) / 2)
        height_margin = int((rect.height - title.get_height()) / 8)
        return width_margin, height_margin

    def _calculate_margin_for_instructions(
        self, rect: pygame.rect.Rect, title: pygame.surface.Surface
    ) -> Tuple[int, int]:
        width_margin = int((rect.width - title.get_width()) / 2)
        height_margin = int((rect.height - title.get_height()) / 2)
        return width_margin, height_margin


class LevelOneTransition(LevelTransition):
    def __init__(self, surface: pygame.surface.Surface) -> None:
        super().__init__(surface)

    def render(self, level: Level) -> None:
        background, title = self._render(level)
        first_line = self.__render_first_line(background, title)
        self.__render_second_line(background, title, first_line)

    def __render_first_line(
        self, background: pygame.rect.Rect, title: pygame.surface.Surface
    ) -> pygame.surface.Surface:
        first_line = self._instructions_font.render(
            "Fuja das comidas não saudáveis",
            True,
            WHITE,
        )

        width_margin, height_margin = self._calculate_margin_for_instructions(
            background, first_line
        )

        self._surface.blit(
            first_line,
            (
                background.x + width_margin,
                background.y + height_margin + title.get_height() / 2,
            ),
        )

        return first_line

    def __render_second_line(
        self,
        background: pygame.rect.Rect,
        title: pygame.surface.Surface,
        first_line: pygame.surface.Surface,
    ):
        second_line = self._instructions_font.render(
            "Pegue as comidas saudáveis",
            True,
            WHITE,
        )

        width_margin, height_margin = self._calculate_margin_for_instructions(
            background, second_line
        )

        self._surface.blit(
            second_line,
            (
                background.x + width_margin,
                background.y
                + height_margin
                + title.get_height() / 2
                + first_line.get_height(),
            ),
        )

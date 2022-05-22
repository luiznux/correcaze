from enum import Enum

import pygame

from contants import BLACK, WIDTH


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

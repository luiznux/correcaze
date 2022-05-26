import pygame

from classes.button import Button
from classes.coodinates import Coordinates
from constants import *


class Rank:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self.__button_font = pygame.font.SysFont("Monaco", 40)
        self.__menu_button: Optional[Button] = None
        self. __scoreboard =

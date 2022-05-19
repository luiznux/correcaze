from typing import List, Tuple
from random import randint, choice
import pygame

from enum import Enum

from classes.caze import Caze
from classes.coodinates import Coordinates
from classes.elements import Hamburguer, LaneElement, Weight
from contants import BLACK, GREEN, HEIGHT, LANES_POSITION, RED, YELLOW


class GameState(Enum):
    Menu = 1
    Playing = 2
    Paused = 3
    Credits = 4


class StaminaBar:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self.__surface = surface
        self.__stamina_font = pygame.font.SysFont("Monaco", 30)

    def render(self, stamina: int) -> None:
        stamina_text = self.__stamina_font.render("Stamina:", True, BLACK)
        self.__surface.blit(stamina_text, (0, 0))

        # Renderiza a barra um pouco depois do texto da stamina
        stamina_bar = pygame.rect.Rect(
            stamina_text.get_width() + 10, 0, stamina, 22
        )

        if stamina >= 50:
            stamina_bar_color = GREEN
        elif stamina >= 25:
            stamina_bar_color = YELLOW
        else:
            stamina_bar_color = RED

        pygame.draw.rect(self.__surface, stamina_bar_color, stamina_bar)


class Game:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self.__caze = Caze(surface)
        self.__lanes = self.__initialize_lanes()
        self.__lane_elements: List[LaneElement] = []
        self.__stamina_bar = StaminaBar(surface)
        self.__stamina_font = pygame.font.SysFont("Monaco", 30)

    def render(self):
        self.__draw_lanes()
        # TODO: Mover isso para um método na classe cazé
        self.__caze.render(
            (LANES_POSITION[self.__caze.lane], HEIGHT - self.__caze.get_height())
        )

        self.__stamina_bar.render(self.__caze.stamina)

        for element in self.__lane_elements:
            element.render()

    def update() -> None:
        pass

    def play(self) -> None:
        for index, element in enumerate(self.__lane_elements):
            element.go_down()
            if element.is_over_screen():
                self.__lane_elements.pop(index)

        # Só renderiza um novo objeto se as lanes estiverem com um
        # elemento ou nenhum
        if len(self.__lane_elements) <= 1:
            if len(self.__lane_elements) == 0:
                self.__generate_weight_on_random_lane()
                self.__generate_hamburguer_on_random_lane()
            else:
                # Verifica qual tipo de elemento que está na lane e
                # gera o elemento contrário.
                if isinstance(self.__lane_elements[0], Hamburguer):
                    self.__generate_weight_on_random_lane()
                else:
                    self.__generate_hamburguer_on_random_lane()

        # TODO: Lógica de colisão para diminuir a stamina.
        self.__caze.decrease_stamina()

    def on_event(self, event: pygame.event.Event) -> GameState:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return GameState.Paused
            else:
                self.__move_caze(event)

        return GameState.Playing

    # TODO: Depois esse método deve ser movido pro Cazé, não faz
    # sentido estar exposto aqui.
    def __move_caze(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.__caze.change_lane("left")
            if event.key == pygame.K_RIGHT:
                self.__caze.change_lane("right")

    def __generate_hamburguer_on_random_lane(self):
        self.__generate_element_on_random_lane(Hamburguer)

    def __generate_weight_on_random_lane(self):
        self.__generate_element_on_random_lane(Weight)

    def __generate_element_on_random_lane(self, class_type):
        lanes_to_exclude = [i.position.x for i in self.__lane_elements]
        random_lane = choice(
            [i for i in range(3) if LANES_POSITION[i] not in lanes_to_exclude]
        )
        x = LANES_POSITION[random_lane]
        y = 20
        self.__lane_elements.append(class_type(self.__surface, Coordinates(x, y)))

    def __initialize_lanes(self) -> Tuple[pygame.Rect, pygame.Rect, pygame.Rect]:
        lanes_width = (self.__surface.get_width() - 200) / 3
        lanes_height = self.__surface.get_height() - 10
        return (
            pygame.Rect(100, 200, lanes_width, lanes_height),
            pygame.Rect(100 + lanes_width, 200, lanes_width, lanes_height),
            pygame.Rect(100 + lanes_width * 2 - 1, 200, lanes_width, lanes_height),
        )

    def __draw_lanes(self):
        pygame.draw.rect(self.__surface, color=(220, 20, 10), rect=self.__lanes[0])
        pygame.draw.rect(self.__surface, color=(180, 60, 160), rect=self.__lanes[1])
        pygame.draw.rect(self.__surface, color=(140, 80, 250), rect=self.__lanes[2])

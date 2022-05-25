from enum import Enum
from random import choice, randint, uniform
from typing import List, Tuple

import pygame
from constants import BLACK, GREEN, GREY, HEIGHT, LANES_POSITION, RED, WIDTH, YELLOW

from classes.caze import Caze
from classes.coodinates import Coordinates
from classes.elements import Hamburguer, LaneElement, Salad, Weight
from classes.level import (
    Level,
    LevelBar,
    LevelOneTransition,
    LevelThreeTransition,
    LevelTwoTransition,
)
from classes.sounds import Sounds


class GameState(Enum):
    Menu = 1
    Playing = 2
    Paused = 3
    Credits = 4
    LoserMenu = 5


class PointsBar:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self.__surface = surface
        self.__font = pygame.font.SysFont("Monaco", 30)

    def render(self, points: int) -> None:
        text = self.__font.render(f"Pontos: {points}", True, BLACK)
        # Renderiza a quantidade de pontos no centro do eixo x da
        # tela.
        self.__surface.blit(text, ((WIDTH / 2) - (text.get_rect().width / 2), 0))


class StaminaBar:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self.__surface = surface
        self.__font = pygame.font.SysFont("Monaco", 30)

    def render(self, stamina: int) -> None:
        text = self.__font.render("Stamina:", True, BLACK)
        self.__surface.blit(text, (0, 0))

        # Renderiza a barra um pouco depois do texto da stamina
        bar = pygame.rect.Rect(text.get_width() + 10, 0, stamina, 22)

        if stamina >= 50:
            stamina_bar_color = GREEN
        elif stamina >= 25:
            stamina_bar_color = YELLOW
        else:
            stamina_bar_color = RED

        max_bar = pygame.rect.Rect(text.get_width() + 10, 0, Caze.MAX_STAMINA, 22)

        pygame.draw.rect(self.__surface, BLACK, max_bar)
        pygame.draw.rect(self.__surface, stamina_bar_color, bar)


class Lane:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self._width = (self.__surface.get_width() - 200) / 3
        self._height = self.__surface.get_height()
        self._y_position = 0
        self._line_width = self._width / 8
        self.__line_max_height = self._height / 4
        self._BACKOFF = 100
        self.__line_y: float = uniform(self._y_position, HEIGHT)
        if self.__is_line_over_lane(self.__line_y):
            self.__line_height = self.__line_y
        else:
            self.__line_height = self.__line_max_height
        self.__SPEED = 5
        self.__MAX_SPEED = 10

    def render(self) -> None:
        pass

    def play(self, level: Level) -> None:
        if level == Level.Three:
            speed = self.__MAX_SPEED
        else:
            speed = self.__SPEED

        if self.__is_line_over_screen():
            self.__line_y = self._y_position - self.__line_max_height
            self.__line_height = 0
        elif self.__is_line_height_at_max():
            self.__line_y += speed
        else:
            self.__line_height += speed

    def _render(self, lane_x: float) -> None:
        asphalt = pygame.Rect(lane_x, self._y_position, self._width, self._height)
        pygame.draw.rect(self.__surface, color=GREY, rect=asphalt)

        line_x = asphalt.x + self._width / 2 - self._line_width
        line = pygame.Rect(line_x, self.__line_y, self._line_width, self.__line_height)
        pygame.draw.rect(self.__surface, color=YELLOW, rect=line)

    def __is_line_height_at_max(self) -> bool:
        return self.__line_height >= self.__line_max_height

    def __is_line_over_screen(self) -> bool:
        return self.__line_y >= HEIGHT

    def __is_line_over_lane(self, y: float) -> bool:
        return (y + self.__line_max_height) < (
            self._y_position + self.__line_max_height
        )


class LeftLane(Lane):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface)

    def render(self):
        self._render(self._BACKOFF)


class MiddleLane(Lane):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface)

    def render(self):
        self._render(self._width + self._BACKOFF)


class RightLane(Lane):
    def __init__(self, surface: pygame.surface.Surface):
        super().__init__(surface)

    def render(self):
        self._render(self._width * 2 - 1 + self._BACKOFF)


class Avenue:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self.__lanes = self.__initialize_lanes()

    def render(self):
        for lane in self.__lanes:
            lane.render()

    def play(self, level: Level):
        for lane in self.__lanes:
            lane.play(level)

    def __initialize_lanes(self) -> Tuple[Lane, Lane, Lane]:
        return (
            RightLane(self.__surface),
            MiddleLane(self.__surface),
            LeftLane(self.__surface),
        )


class Game:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface: pygame.surface.Surface = surface
        self.__caze: Caze = Caze(surface)
        self.__lane_elements: List[LaneElement] = []
        self.__stamina_bar: StaminaBar = StaminaBar(surface)
        self.__points_bar: PointsBar = PointsBar(surface)
        self.__level_bar: LevelBar = LevelBar(surface)
        self.__sounds: Sounds = Sounds()
        self.__over: bool = False
        self.__level: Level = Level.One
        self.__avenue = Avenue(surface)
        self.__is_transitioning_level = True
        self.__transition = LevelOneTransition(self.__surface)

    def render(self):
        self.__avenue.render()
        self.__caze.render(
            (LANES_POSITION[self.__caze.lane], HEIGHT - self.__caze.get_height())
        )

        self.__stamina_bar.render(self.__caze.stamina)
        self.__points_bar.render(self.__caze.points)
        self.__level_bar.render(self.__level)

        for element in self.__lane_elements:
            element.render()

        if self.__is_transitioning_level:
            self.__transition.render()
            return

    def update(self) -> None:
        pass

    def play(self) -> None:
        if self.__is_transitioning_level:
            return

        self.__sounds.play_background_music(self.__level)
        self.__avenue.play(self.__level)

        for index, element in enumerate(self.__lane_elements):
            element.go_down(self.__level)
            if element.is_over_screen():
                self.__lane_elements.pop(index)

            if element.collided_with(self.__caze.rendered_caze()):
                element.on_collision(self.__caze, self.__sounds)
                # Se o elemento colidiu com o usuário ele deve ser
                # removido da tela.
                self.__lane_elements.pop(index)

        # Só renderiza um novo objeto se as lanes estiverem com um
        # elemento ou nenhum
        if len(self.__lane_elements) <= 1:
            if len(self.__lane_elements) == 0:
                self.__generate_good_item_on_random_lane()
                self.__generate_hamburguer_on_random_lane()
            else:
                # Verifica qual tipo de elemento que está na lane e
                # gera o elemento contrário.
                if isinstance(self.__lane_elements[0], Hamburguer):
                    self.__generate_good_item_on_random_lane()
                else:
                    self.__generate_hamburguer_on_random_lane()

        if self.__caze.is_out_of_stamina():
            self.__sounds.stop_background_music(self.__level)
            self.__end_game()

        if self.__level == Level.One and self.__caze.points >= 250:
            self.__level = Level.Two
            self.__transition = LevelTwoTransition(self.__surface)
            self.__is_transitioning_level = True
            self.__sounds.stop_background_music(self.__level)
        elif self.__level == Level.Two and self.__caze.points >= 500:
            self.__level = Level.Three
            self.__transition = LevelThreeTransition(self.__surface)
            self.__is_transitioning_level = True
            self.__sounds.stop_background_music(self.__level)

        self.__caze.run()

    def is_over(self) -> bool:
        return self.__over

    def on_event(self, event: pygame.event.Event) -> GameState:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__sounds.pause_background_music()
                return GameState.Paused
            else:
                self.__caze.on_event(event)

            if self.__is_transitioning_level:
                if event.key == pygame.K_RETURN:
                    self.__is_transitioning_level = False

        return GameState.Playing

    def __end_game(self) -> None:
        self.__over = True

    def __generate_hamburguer_on_random_lane(self):
        self.__generate_element_on_random_lane(Hamburguer)

    def __generate_good_item_on_random_lane(self):
        if self.__level == Level.One or self.__caze.stamina < 150:
            self.__generate_salad_on_random_lane()
            return

        random = randint(0, 1)
        if random:
            self.__generate_weight_on_random_lane()
        else:
            self.__generate_salad_on_random_lane()

    def __generate_weight_on_random_lane(self):
        self.__generate_element_on_random_lane(Weight)

    def __generate_salad_on_random_lane(self):
        self.__generate_element_on_random_lane(Salad)

    def __generate_element_on_random_lane(self, class_type):
        lanes_to_exclude = [i.position.x for i in self.__lane_elements]
        random_lane = choice(
            [i for i in range(3) if LANES_POSITION[i] not in lanes_to_exclude]
        )
        x = LANES_POSITION[random_lane]
        y = 20
        self.__lane_elements.append(class_type(self.__surface, Coordinates(x, y)))

import pygame

from enum import Enum

from classes.caze import Caze
from classes.menu import Menu
from classes.credits import Credits
from contants import *

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.Surface((WIDTH, HEIGHT))
image = pygame.image.load("assets/caze_placeholder.png").convert_alpha()

pygame.font.init()


def initialize_lanes(surface: pygame.surface.Surface):
    lanes_width = (surface.get_width() - 200) / 3
    lanes_height = surface.get_height() - 100
    return (
        pygame.Rect(100, 200, lanes_width, lanes_height),
        pygame.Rect(100 + lanes_width, 200, lanes_width, lanes_height),
        pygame.Rect(100 + lanes_width * 2 - 1, 200, lanes_width, lanes_height),
    )


def prepare_lanes(surface: pygame.surface.Surface):
    lane1, lane2, lane3 = initialize_lanes(surface)
    pygame.draw.rect(surface, color=(220, 20, 10), rect=lane1)
    pygame.draw.rect(surface, color=(180, 60, 160), rect=lane2)
    pygame.draw.rect(surface, color=(140, 80, 250), rect=lane3)


def render_game():
    prepare_lanes(bg)
    bg.blit(cazezinho.image, (lanes[cazezinho.lane], cazezinho.image.get_height()))


def move_caze():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            cazezinho.change_lane("left")
        if event.key == pygame.K_RIGHT:
            cazezinho.change_lane("right")


menu = Menu(bg)
credits = Credits(bg)
cazezinho = Caze(bg, image)


class GameState(Enum):
    Menu = 1
    Playing = 2
    Paused = 3
    Credits = 4


state = GameState.Menu

if __name__ == "__main__":
    while True:
        clock.tick(FPS)
        bg.fill((255, 255, 255))

        if state == GameState.Menu:
            menu.render()
        elif state == GameState.Playing:
            render_game()
        elif state == GameState.Credits:
            credits.render()

        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                exit()

            if state == GameState.Menu:
                if menu.clicked_on_start_game(event):
                    state = GameState.Playing
                elif menu.clicked_on_credits(event):
                    state = GameState.Credits
                elif menu.clicked_on_quit(event):
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN and state == GameState.Playing:
                move_caze()

            if state == GameState.Credits and credits.clicked_on_menu(event):
                state = GameState.Menu

        window.blit(bg, (0, 0))
        pygame.display.flip()

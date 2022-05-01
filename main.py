import logging

import pygame

from classes.caze import Caze
from contants import *

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.Surface((WIDTH, HEIGHT))
bg.fill((255, 255, 255))
image = pygame.image.load('assets/caze_placeholder.png').convert_alpha()

pygame.font.init()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def initialize_lanes(surface):
    lanes_width = (surface.get_width() - 200) / 3
    lanes_height = surface.get_height() - 100
    return (pygame.Rect(100, 200, lanes_width, lanes_height),
            pygame.Rect(100 + lanes_width, 200, lanes_width, lanes_height),
            pygame.Rect(100 + lanes_width * 2 - 1, 200, lanes_width, lanes_height))


def prepare_lanes(surface):
    lane1, lane2, lane3 = initialize_lanes(surface)
    pygame.draw.rect(surface, color=(220, 20, 10), rect=lane1)
    pygame.draw.rect(surface, color=(180, 60, 160), rect=lane2)
    pygame.draw.rect(surface, color=(140, 80, 250), rect=lane3)


def render_main_menu(surface: pygame.surface.Surface):
    title_font = pygame.font.SysFont('Monaco', 60)
    title_surface = title_font.render('Corre Caze', False, (0, 0, 0))
    # Define o X como o meio da tela
    title_position_x = (WIDTH / 2) - (title_surface.get_width() / 2)
    surface.blit(title_surface, (title_position_x, 100))

    pygame.draw.rect(surface, (255, 0, 0),
                     pygame.Rect((title_position_x, 150, title_surface.get_width(), 100)))

    pygame.draw.rect(surface, (255, 0, 0),
                     pygame.Rect((title_position_x, 300, title_surface.get_width(), 100)))

    pygame.draw.rect(surface, (255, 0, 0),
                     pygame.Rect((title_position_x, 450, title_surface.get_width(), 100)))


# prepare_lanes(bg)
# cazezinho = Caze(bg, image)

if __name__ == '__main__':
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                exit()

            render_main_menu(bg)
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_LEFT:
            #        cazezinho.change_lane('left')
            #    if event.key == pygame.K_RIGHT:
            #        cazezinho.change_lane('right')
        window.blit(bg, (0, 0))
        #window.blit(cazezinho.image, (lanes[cazezinho.lane], cazezinho.image.get_height()))
        pygame.display.flip()


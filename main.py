import pygame

from classes.caze import Caze
from contants import *

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((HEIGHT, WIDTH))
bg = pygame.Surface((HEIGHT, WIDTH))
bg.fill((255, 255, 255))
image = pygame.image.load('assets/caze_placeholder.png').convert_alpha()


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


prepare_lanes(bg)
cazezinho = Caze(bg, image)

if __name__ == '__main__':
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cazezinho.change_lane('left')
                if event.key == pygame.K_RIGHT:
                    cazezinho.change_lane('right')
        window.blit(bg, (0, 0))
        window.blit(cazezinho.image, (lanes[cazezinho.lane], cazezinho.image.get_height()))
        pygame.display.flip()


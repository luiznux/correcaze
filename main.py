import pygame

from classes.caze import Caze

HEIGHT = 640
WIDTH = 480
FPS = 60

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((HEIGHT, WIDTH))
surface = pygame.Surface((HEIGHT, WIDTH))
caze_image = pygame.image.load('assets/caze_placeholder.jpeg').convert_alpha()
cazezinho = Caze(surface, caze_image, 1)

window.blit(cazezinho.image, (0, 0))
if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cazezinho.move_left()
                    print(f'moving left to {cazezinho.lane}')
                if event.key == pygame.K_RIGHT:
                    cazezinho.move_right()
                    print(f'moving right to {cazezinho.lane}')
        pygame.display.update()
        clock.tick(FPS)

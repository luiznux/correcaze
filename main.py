import pygame
HEIGHT = 640
WIDTH = 480

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((HEIGHT, WIDTH))

if __name__ == '__main__':
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                exit()

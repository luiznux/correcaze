import pygame

from enum import Enum

from classes.game import Game
from classes.menu import InitialMenu, PauseMenu
from classes.credits import Credits
from contants import *

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))

pygame.font.init()

menu = InitialMenu(background)
menu_pause = PauseMenu(background)
credits = Credits(background)
game = Game(background)


class GameState(Enum):
    Menu = 1
    Playing = 2
    Paused = 3
    Credits = 4


state = GameState.Menu

if __name__ == "__main__":
    while True:
        clock.tick(FPS)
        background.fill((255, 255, 255))

        if state == GameState.Menu:
            menu.render()
        elif state == GameState.Playing:
            game.render()
        elif state == GameState.Credits:
            credits.render()
        elif state == GameState.Paused:
            menu_pause.render()

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

            if state == GameState.Paused:
                if menu_pause.clicked_on_start_game(event):
                    state = GameState.Playing
                elif menu_pause.clicked_on_credits(event):
                    state = GameState.Credits
                elif menu_pause.clicked_on_quit(event):
                    pygame.quit()
                    exit()

            if state == GameState.Playing:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = GameState.Paused
                    else:
                        game.move_caze(event)

            if state == GameState.Credits and credits.clicked_on_menu(event):
                state = GameState.Menu

        window.blit(background, (0, 0))
        pygame.display.flip()

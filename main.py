import pygame

from classes.game import Game, GameState
from classes.menu import InitialMenu, LoserMenu, Menu, PauseMenu
from classes.credits import Credits
from contants import *

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))

pygame.font.init()

initial_menu = InitialMenu(background)
pause_menu = PauseMenu(background)
loser_menu = LoserMenu(background)
credits = Credits(background)
game = Game(background)

state = GameState.Menu


def menu_actions(menu: Menu, current_state: GameState):
    if menu.clicked_on_start_game(event):
        return GameState.Playing
    elif menu.clicked_on_credits(event):
        return GameState.Credits
    elif menu.clicked_on_quit(event):
        pygame.quit()
        exit()
    else:
        return current_state


if __name__ == "__main__":
    while True:
        clock.tick(FPS)
        background.fill((255, 255, 255))

        if game.is_over():
            state = GameState.LoserMenu

        if state == GameState.Menu:
            initial_menu.render()
        elif state == GameState.Playing:
            game.play()
            game.render()
        elif state == GameState.Credits:
            credits.render()
        elif state == GameState.Paused:
            pause_menu.render()
        elif state == GameState.LoserMenu:
            loser_menu.render()

        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                exit()

            if state == GameState.Menu:
                state = menu_actions(initial_menu, state)

            if state == GameState.Paused:
                state = menu_actions(pause_menu, state)

            if state == GameState.LoserMenu:
                state = menu_actions(loser_menu, state)

            if state == GameState.Playing:
                state = game.on_event(event)

            if state == GameState.Credits and credits.clicked_on_menu(event):
                state = GameState.Menu

        window.blit(background, (0, 0))
        pygame.display.flip()

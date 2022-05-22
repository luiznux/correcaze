import pygame

from classes.credits import Credits
from classes.game import Game, GameState
from classes.menu import InitialMenu, LoserMenu, Menu, PauseMenu
from classes.sounds import Sounds
from contants import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))

initial_menu = InitialMenu(background)
pause_menu = PauseMenu(background)
loser_menu = LoserMenu(background)
credits = Credits(background)
game = Game(background)
current_menu: Menu = initial_menu

state = GameState.Menu
background_music = Sounds()

if __name__ == "__main__":
    while True:
        clock.tick(FPS)
        background.fill((255, 255, 255))

        if game.is_over():
            game = Game(background)
            state = GameState.LoserMenu
            current_menu = loser_menu

        if state in [GameState.Menu, GameState.Paused, GameState.LoserMenu]:
            current_menu.render()
        elif state == GameState.Playing:
            game.play()
            game.render()
        elif state == GameState.Credits:
            credits.render()

        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                exit()

            if state in [GameState.Menu, GameState.Paused, GameState.LoserMenu]:
                if current_menu.clicked_on_start_game(event):
                    state = GameState.Playing
                elif current_menu.clicked_on_credits(event):
                    state = GameState.Credits
                elif current_menu.clicked_on_quit(event):
                    pygame.quit()
                    exit()

            if state == GameState.Credits and credits.clicked_on_menu(event):
                state = GameState.Menu

            if state == GameState.Playing:
                state = game.on_event(event)
                if state == GameState.Paused:
                    current_menu = pause_menu

        window.blit(background, (0, 0))
        pygame.display.flip()

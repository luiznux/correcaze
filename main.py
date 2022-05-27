import pygame

from classes.credits import Credits
from classes.game import Game, GameState
from classes.menu import InitialMenu, LoserMenu, Menu, PauseMenu, RankMenu
from classes.sounds import Sounds
from constants import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))
sound_mute = False
initial_menu = InitialMenu(background)
pause_menu = PauseMenu(background)
loser_menu = LoserMenu(background)
rank_menu = RankMenu(background)
credits = Credits(background)
game = Game(background)
current_menu: Menu = initial_menu

state = GameState.Menu
background_music = Sounds()

if __name__ == "__main__":
    while True:
        clock.tick(FPS)
        background.fill((255, 255, 255))

        if game.is_over() and state != GameState.LoserMenu:
            state = GameState.LoserMenu

        if state in [GameState.Menu, GameState.Paused]:
            current_menu.render()
        elif state == GameState.Playing:
            game.play(sound_mute)
            game.render()
        elif state == GameState.Credits:
            credits.render()
        elif state == GameState.Ranking:
            rank_menu.render()
        elif state == GameState.LoserMenu:
            loser_menu.render()

        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                exit()

            if state in [GameState.Menu, GameState.Paused]:
                if current_menu.clicked_on_start_game(event):
                    state = GameState.Playing
                elif current_menu.clicked_on_credits(event):
                    state = GameState.Credits
                elif current_menu.clicked_on_ranking(event):
                    state = GameState.Ranking
                elif current_menu.clicked_on_quit(event):
                    pygame.quit()
                    exit()
                elif current_menu.clicked_on_mute(event):
                    sound_mute = not sound_mute



            if state == GameState.Ranking:
                if rank_menu.clicked_on_menu(event):
                    state = GameState.Menu

            if state == GameState.LoserMenu:
                loser_menu.on_event(event)
                if loser_menu.clicked_on_menu(event):
                    state = GameState.Menu
                    current_menu = initial_menu
                    game = Game(background)
                elif loser_menu.clicked_on_save_ranking(event):
                    game.save_ranking(loser_menu.player_name)
                elif loser_menu.clicked_on_quit(event):
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

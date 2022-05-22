from typing import Dict
from pygame import mixer

from classes.level import Level


class Sounds:
    def __init__(self) -> None:
        self.__playing_background_music_control: Dict[Level, bool] = {
            Level.One: False,
            Level.Two: False,
            Level.Three: False,
        }
        self.__is_playing_sound_effect = False
        self.__background_volume = 0.08
        self.__effects_volume = 0.10
        mixer.music.set_volume(self.__background_volume)

    sound_effects_map = {
        "dentroo": "assets/sound-effects/dentrooo.mp3",
        "come-carne": "assets/sound-effects/ele-ta-dilacerando-a-carne.mp3",
        "meu-deus": "assets/sound-effects/meu-deus-que-isso.mp3",
    }

    background_music_map = {
        Level.One: "assets/background-music/hino-do-vasco.mp3",
        Level.Two: "assets/background-music/hino-do-flamengo.mp3",
        Level.Three: "assets/background-music/hino-do-corinthians.mp3",
    }

    def play_sound_effect(self, sound_effect_name: str):
        sound = mixer.Sound(self.sound_effects_map.get(sound_effect_name))
        sound.set_volume(self.__effects_volume)
        if self.__is_playing_sound_effect:
            sound.fadeout(1000)
            self.__is_playing_sound_effect = False
        else:
            sound.play()
            self.__is_playing_sound_effect = True

    def play_background_music(self, level: Level) -> None:
        if self.__is_playing_background_music_for_level(level):
            return

        # Verifica se alguma musica ja esta rondando em background
        if mixer.music.get_busy():
            mixer.music.unload()

        mixer.music.load(self.background_music_map[level])
        mixer.music.play(-1)
        self.__playing_background_music_control[level] = True

    def stop_background_music(self, level: Level) -> None:
        if mixer.music.get_busy():
            mixer.music.unload()
        self.__playing_background_music_control[level] = False

    def __is_playing_background_music_for_level(self, level: Level) -> bool:
        return self.__playing_background_music_control[level]

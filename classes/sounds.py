from pygame import mixer


class Sounds:

    sound_effects_map = {
        "dentroo": "assets/sound-effects/dentrooo.mp3",
        "come-carne": "assets/sound-effects/ele-ta-dilacerando-a-carne.mp3",
        "meu-deus": "assets/sound-effects/meu-deus-que-isso.mp3"
    }

    background_music_map = {
        "hino-do-vasco": "assets/background-music/hino-do-vasco.mp3",
        "hino-do-flamengo": "assets/background-music/hino-do-flamengo.mp3",
        "hino-do-corinthians":
        "assets/background-music/hino-do-corinthians.mp3"
    }

    def play_sound_effect(self, sound_effect_name: str):
        sound = mixer.Sound(self.sound_effects_map.get(sound_effect_name))
        return sound.play

    def play_background_music(self, music_name: str):
        # Verifica se alguma musica ja esta rondando em background
        if mixer.music.get_busy():
            mixer.music.unload()
            mixer.music.load(self.background_music_map[music_name])
            return mixer.music.play(-1)

        mixer.music.load(self.background_music_map[music_name])
        return mixer.music.play(-1)

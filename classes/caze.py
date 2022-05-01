import pygame


class Caze(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.surface.Surface, image: pygame.surface.Surface):
        pygame.sprite.Sprite.__init__(self)
        self._image = image
        self._surface = surface
        self._stamina = 100
        self._speed = 10
        self._lane = 1

    def change_lane(self, direction: str):
        if direction is "left":
            self.move_left()
        else:
            self.move_right()

    def move_left(self):
        if self._lane - 1 < 0:
            pass
        else:
            self._lane -= 1

    def move_right(self):
        if self._lane + 1 > 2:
            pass
        else:
            self._lane += 1

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def lane(self):
        return self._lane

import pygame


class Caze(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.surface,
                 image: pygame.image,
                 initial_lane: int):
        pygame.sprite.Sprite.__init__(self)
        self._surface = surface
        self._image = image
        self._lane = initial_lane

    @property
    def surface(self):
        return self._surface

    @property
    def lane(self):
        return self._lane

    @property
    def image(self):
        return self._image

    def move_right(self):
        if self._lane + 1 >= 2:
            self._lane = 2
        else:
            self._lane += 1

    def move_left(self):
        if self._lane - 1 <= 0:
            self._lane = 0
        else:
            self._lane -= 1

    @image.setter
    def image(self, value):
        self._image = value

    @surface.setter
    def surface(self, value):
        self._surface = value

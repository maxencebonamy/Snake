import random
import pygame
from enum import Enum
from config import *


class Direction(Enum):

    LEFT = "left", Vector2(-1, 0), pygame.K_q
    RIGHT = "right", Vector2(1, 0), pygame.K_d

    UP = "up", Vector2(0, -1), pygame.K_z
    DOWN = "down", Vector2(0, 1), pygame.K_s

    @classmethod
    def get_random(cls):
        return random.choice(list(cls))

    @classmethod
    def from_vector(cls, vector):
        for d in Direction:
            if d.vector == vector:
                return d
        return None

    @property
    def opposite(self):
        return self.from_vector(-self.vector)

    @property
    def name(self):
        return self.value[0]

    @property
    def vector(self):
        return self.value[1]

    @property
    def key(self):
        return self.value[2]
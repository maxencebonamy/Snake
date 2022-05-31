import random

import pygame
from config import *


class Apple:

    def __init__(self):
        self.set_random_position()

        self.image = pygame.image.load("assets/apple.png")
        self.image = pygame.transform.smoothscale(self.image, TILE_SIZE)

    def display(self, window):
        window.blit(self.image, self.rect)

    def set_random_position(self, forbidden=None):
        if forbidden is None:
            forbidden = []
        mx = int(WINDOW_SIZE.x / TILE_LENGTH) - 1
        my = int(WINDOW_SIZE.y / TILE_LENGTH) - 1
        cond = True
        while cond:
            self.position = Vector2(random.randint(0, mx), random.randint(0, my))
            cond = self.position in forbidden
        self.rect = pygame.Rect(self.position * TILE_LENGTH, TILE_SIZE)
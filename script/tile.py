import pygame
from config import *


class Tile:

    def __init__(self, position, color):
        self.position = position
        self.color = color

        self.rect = pygame.Rect(position * TILE_LENGTH, TILE_SIZE)

    def display(self, window):
        pygame.draw.rect(window, self.color, self.rect)
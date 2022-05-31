from script.tile import Tile
from config import *


class Grid:

    def __init__(self):
        self.tiles = []
        for y in range(int(WINDOW_SIZE.y / TILE_LENGTH)):
            self.tiles.append([])
            for x in range(int(WINDOW_SIZE.x / TILE_LENGTH)):
                self.tiles[-1].append(Tile(Vector2(x, y), TILE_COLORS[(x + y) % 2]))

    def display(self, window):
        for line in self.tiles:
            for tile in line:
                tile.display(window)
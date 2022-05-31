from pygame.math import Vector2


# the dimensions of the window (in pixels)
WINDOW_SIZE = Vector2(800, 800)
# the background color of the window
WINDOW_COLOR = (13, 22, 11)
# the window refresh rate (in frames per second)
WINDOW_FPS = 10

# the size of the side of a tile (in pixels)
TILE_LENGTH = 40
# the dimensions of a tile (do not modify)
TILE_SIZE = Vector2(TILE_LENGTH)
# the two different colors of the tiles
TILE_COLORS = (
    (173, 214, 68),
    (166, 209, 60)
)

# the initial length of the snake
SNAKE_LENGTH = 1
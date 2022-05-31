import pygame
import sys
from config import *
from script.apple import Apple
from script.direction import Direction
from script.grid import Grid
from script.snake import Snake

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Snake")

icon = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(icon)

grid = Grid()
apple = Apple()
snake = Snake()

while True:

    snake.update(apple)

    window.fill(WINDOW_COLOR)

    grid.display(window)
    apple.display(window)
    snake.display(window)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            for direction in Direction:
                if direction.key == event.key and snake.direction.opposite != direction and snake.canMove:
                    snake.direction = direction

    pygame.time.wait(1000 // WINDOW_FPS)
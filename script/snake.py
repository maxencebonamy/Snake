import random
import pygame
from config import *
from script.direction import Direction


class Snake:

    def __init__(self):
        mx = int(WINDOW_SIZE.x / TILE_LENGTH) - 1
        my = int(WINDOW_SIZE.y / TILE_LENGTH) - 1
        self.head_position = Vector2(random.randint(0, mx), random.randint(0, my))
        self.direction = Direction.get_random()

        self.tail_position = self.head_position - (SNAKE_LENGTH + 1) * self.direction.vector

        self.head_images = {d: pygame.transform.smoothscale(pygame.image.load(f"assets/head_{d.name}.png"), TILE_SIZE) for d in Direction}
        self.tail_images = {d: pygame.transform.smoothscale(pygame.image.load(f"assets/tail_{d.name}.png"), TILE_SIZE) for d in Direction}

        self.body_image = pygame.image.load("assets/body_horizontal.png")
        directions = ("horizontal", "vertical", "bottomleft", "bottomright", "topleft", "topright")
        self.body_image = {name: pygame.transform.smoothscale(pygame.image.load(f"assets/body_{name}.png"), TILE_SIZE) for name in directions}

        self.body = list(reversed([Vector2(self.head_position - i*self.direction.vector) for i in range(1, SNAKE_LENGTH + 1)]))

        self.canMove = True

    @staticmethod
    def is_in_bounds(position):
        return 0 <= position.x < WINDOW_SIZE.x / TILE_LENGTH and 0 <= position.y < WINDOW_SIZE.y / TILE_LENGTH

    def is_over_itself(self, position):
        return position in self.body + [self.tail_position]

    def update(self, apple):
        if not self.is_in_bounds(self.head_position + self.direction.vector)\
                or self.is_over_itself(self.head_position + self.direction.vector):
            self.canMove = False
        if self.canMove:
            if apple.position != self.head_position:
                self.tail_position = self.body[0].copy()
                for i in range(len(self.body) - 1):
                    self.body[i] = self.body[i + 1].copy()
                self.body[-1] = self.head_position.copy()
            else:
                self.body.append(self.head_position.copy())
                if len(self.body) + 2 == (WINDOW_SIZE.x * WINDOW_SIZE.y) // (TILE_LENGTH ** 2):
                    self.canMove = False
                else:
                    apple.set_random_position(self.body + [self.tail_position] + [self.head_position])
            self.head_position += self.direction.vector

    def display(self, window):
        vector = self.body[0] - self.tail_position
        window.blit(self.tail_images[Direction.from_vector(vector).opposite], self.get_rect(self.tail_position))

        for i, position in enumerate(self.body):
            if i == 0:
                a = position - self.tail_position
                if i == len(self.body) - 1:
                    b = self.head_position - position
                else:
                    b = self.body[i + 1] - position
            elif i == len(self.body) - 1:
                a = position - self.body[i - 1]
                b = self.head_position - position
            else:
                a = position - self.body[i - 1]
                b = self.body[i + 1] - position
            window.blit(self.get_body_image(a, b), self.get_rect(position))

        window.blit(self.head_images[self.direction], self.get_rect(self.head_position))

    @staticmethod
    def get_rect(position):
        return pygame.Rect(position * TILE_LENGTH, TILE_SIZE)

    def get_body_image(self, a, b):
        if a in [Vector2(1, 0), Vector2(-1, 0)] and b in [Vector2(1, 0), Vector2(-1, 0),]:
            return self.body_image["horizontal"]
        if a in [Vector2(0, 1), Vector2(0, -1)] and b in [Vector2(0, 1), Vector2(0, -1),]:
            return self.body_image["vertical"]

        if a in [Vector2(0, -1), Vector2(1, 0)] and b in [Vector2(0, 1), Vector2(-1, 0),]:
            return self.body_image["bottomleft"]
        if a in [Vector2(0, -1), Vector2(-1, 0)] and b in [Vector2(0, 1), Vector2(1, 0),]:
            return self.body_image["bottomright"]

        if a in [Vector2(0, 1), Vector2(1, 0)] and b in [Vector2(0, -1), Vector2(-1, 0),]:
            return self.body_image["topleft"]
        if a in [Vector2(0, 1), Vector2(-1, 0)] and b in [Vector2(0, -1), Vector2(1, 0),]:
            return self.body_image["topright"]
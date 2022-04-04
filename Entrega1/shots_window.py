import pygame
import sys
import os
from pygame import mixer
from pygame.locals import *
import math
import random


WIDTH = 800
HEIGH = 800
FPS = 60


ROWS, COL = 8, 8
SQUARE_SIZE = WIDTH//COL

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)


class Shot:
    PADDING = 15
    OUTLINE = 2

    def __init__(self):

        self.color = WHITE

    def draw(self, win, x, y):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, WHITE, (x, y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (x, y), radius)

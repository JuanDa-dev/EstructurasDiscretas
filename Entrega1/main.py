#BattleShip 

import pygame

from pygame.locals import *

def constructor():
    pygame.init()
    pygame.display.set_caption("BattleShip")
    screen = pygame.display.set_mode((850, 720))
    #setting an existing img for the background
    screen.blit(pygame.image.load("bg_1.jpg"), (0, 0))
    return screen
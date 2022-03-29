# BattleShip
import boat
import pygame
import os
from pygame import mixer
from pygame.locals import *
import math
import random

from board import battleship, shot


win_width = 850
win_heigh = 720

# Resource paths

current_path = os.path.dirname(__file__)  # Where your .py file is located
resource_path = os.path.join(current_path, '')  # The resource folder path
image_path = os.path.join(resource_path, 'Assets')  # The image folder path

# prepare the resources
battleship_IMGS = pygame.transform.scale2x(
    pygame.image.load(os.path.join(image_path, 'cruiser.png')))
BG = pygame.transform.scale(pygame.image.load(os.path.join(
    image_path, "bg_3.jpg")), (win_width, win_heigh))

WIN = pygame.display.set_mode((win_width, win_heigh))


# name of the game
pygame.display.set_caption("Battle Ship")
# icon
icon = pygame.image.load(os.path.join(image_path, 'destructor.png'))
pygame.display.set_icon(icon)


# defining the ships
# boat1 = boat.Boat(100, 100, 1, "Submarine")


'''def constructor():
    pygame.init()
    pygame.display.set_caption("BattleShip")
    screen = pygame.display.set_mode((850, 720))
    #setting an existing img for the background
    screen.blit(pygame.image.load("bg_1.jpg"), (0, 0))
    return screen'''


def draw_win(win, boat):

    win.blit(BG, (0, 0))

    boat.draw(win, battleship_IMGS)

    pygame.display.update()


def game_loop():
    #boat1 = boat.Boat(100, 100, 1, "Submarine")

    running = True
    while running:
        #draw_win(WIN, boat1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


game_loop()

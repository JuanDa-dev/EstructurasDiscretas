#from board import battleship, shot
from tkinter import Button
import boat
import pygame
import sys
import os
from pygame import mixer
from pygame.locals import *
import math
import random
from board import Board

# Resource paths

current_path = os.path.dirname(__file__)  # Where your .py file is located
resource_path = os.path.join(current_path, '')  # The resource folder path
image_path = os.path.join(resource_path, 'Assets')  # The image folder path


pygame.init()

mainClock = pygame.time.Clock()


WIDTH = 800
HEIGH = 800
FPS = 60


ROWS, COL = 8, 8
SQUARE_SIZE = WIDTH//COL

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)

# prepare the resources
BATTLESHIP_IMGS = pygame.transform.scale2x(
    pygame.image.load(os.path.join(image_path, 'cruiser.png')))

BG = pygame.transform.scale(pygame.image.load(os.path.join(
    image_path, "bg_3.jpg")), (WIDTH, HEIGH))

BG_MAIN_MENU = pygame.transform.scale(pygame.image.load(os.path.join(
    image_path, "mainWindows.jpg")), (WIDTH, HEIGH))


BUTTON_PLAY = pygame.transform.scale(pygame.image.load(os.path.join(
    image_path, "play_BTN.png")), (390, 130))

ICON = pygame.image.load(os.path.join(image_path, 'destructor.png'))

WIN = pygame.display.set_mode((WIDTH, HEIGH))


# name of the game
pygame.display.set_caption("BattleShip")
# icon
pygame.display.set_icon(ICON)


def draw_win(win, boat):

    win.blit(BG, (0, 0))

    #boat.draw(win, battleship_IMGS)

    pygame.display.update()


def main_menu():

    run = True
    while run:

        WIN.blit(BG_MAIN_MENU, (0, 0))

        mx, my = pygame.mouse.get_pos()
        print(mx, my)

        Button_play = WIN.blit(
            BUTTON_PLAY, (WIDTH/2 - 200, 500))
        '''button_1 = pygame.Rect(50, 100, 200, 50)

        pygame.draw.rect(WIN, (255, 0, 0), button_1)'''
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button_play.collidepoint((mx, my)):

                    game_loop()

    pygame.quit()


def game_loop():
    #boat1 = boat.Boat(100, 100, 1, "Submarine")

    running = True

    clock = pygame.time.Clock()

    board = Board()

    '''def redraw_window():
        WIN.blit(BG, (0, 0))
        #boat1.draw(WIN, battleship_IMGS)
        pygame.display.update()'''
    while running:
        #draw_win(WIN, boat1)
        # redraw_window()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit the screen
                running = False
                sys.exit()
        board.draw_board(WIN)
        pygame.display.update()

    # pygame.quit()


# game_loop()
main_menu()

#from board import battleship, shot
from tkinter import *
from tkinter import messagebox
import boat
import pygame
import sys
import os
from pygame import mixer
from pygame.locals import *
import math
import random
from board import Board
import window as win_


# Resource paths

current_path = os.path.dirname(__file__)  # Where your .py file is located
resource_path = os.path.join(current_path, '')  # The resource folder path
image_path = os.path.join(resource_path, 'Assets')  # The image folder path


pygame.init()

mainClock = pygame.time.Clock()


WIDTH = 800
HEIGH = 800
FPS = 60


ROWS, COL, n = 8, 8, 8
SQUARE_SIZE = WIDTH//COL

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)
CYAN = (0, 255, 255)

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


def calc_pos(x, y):
    px = SQUARE_SIZE * x + SQUARE_SIZE // 2
    py = SQUARE_SIZE * y + SQUARE_SIZE // 2
    return px, py


def draw_win(win, boat):

    win.blit(BG, (0, 0))

    #boat.draw(win, battleship_IMGS)

    pygame.display.update()


def main_menu():

    run = True
    while run:

        WIN.blit(BG_MAIN_MENU, (0, 0))

        mx, my = pygame.mouse.get_pos()

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

    board_2 = []
    boats = []
    boat_type = {"submarinos": 1, "destructores": 2,
                 "cruceros": 3, "portaaviones": 4}
    running = True

    clock = pygame.time.Clock()

    board = Board()

    win_.display_window()
    sw = 1
    sub, dest, cru, port = win_.setD()

    boats += board.addBoats(boat_type["submarinos"], sub, 1)
    boats += board.addBoats(boat_type["submarinos"], dest, 2)
    boats += board.addBoats(boat_type["cruceros"], cru, 3)
    boats += board.addBoats(boat_type["portaaviones"], port, 4)
    board_ = None
    board_ = board.battleship(boats, n)

    for i in range(len(board_)):
        board_2.append([])
        for j in range(len(board_)):
            board_2[i].append(board_[i][j])

    '''def redraw_window():
        WIN.blit(BG, (0, 0))
        #boat1.draw(WIN, battleship_IMGS)
        pygame.display.update()'''
    while not board.isEnd(boats):
        #draw_win(WIN, boat1)
        # redraw_window()
        mx, my = pygame.mouse.get_pos()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit the screen
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = board.determinate_quadrant(mx, my)
                Px, Py = calc_pos(x, y)

                if (0 <= x < len(board_)) and (0 <= y < len(board_)):
                    board.shot(board_, boats, x, y)

                shots = board.addShots(x, y)

        # shot_win.display_window()

        # draw the panel in white when we click
        board.draw_board(WIN)
        radius = SQUARE_SIZE//2 - 15
        for i in range(ROWS):
            for j in range(COL):
                if board.shots[i][j] == 1:

                    pygame.draw.circle(
                        WIN, WHITE, (SQUARE_SIZE * j + SQUARE_SIZE // 2, SQUARE_SIZE * i + SQUARE_SIZE // 2), radius + 2)

        pygame.display.update()
    Tk().wm_withdraw()  # to hide the main window
    messagebox.showinfo('You Win', 'OK')
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                sys.exit()
        board.draw_board(WIN)
        radius = SQUARE_SIZE//2 - 15

        for i in range(ROWS):
            for j in range(COL):
                if board_2[i][j] != 0:

                    pygame.draw.circle(
                        WIN, CYAN, (SQUARE_SIZE * j + SQUARE_SIZE // 2, SQUARE_SIZE * i + SQUARE_SIZE // 2), radius + 2)
        pygame.display.update()


    # pygame.quit()
# game_loop()
main_menu()

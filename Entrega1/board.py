from random import randint
from boat import Boat
import pygame
from pygame import mixer
from pygame.locals import *


WIDTH = 800
HEIGH = 800
FPS = 60


ROWS, COL, n = 8, 8, 8
SQUARE_SIZE = WIDTH//COL

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)


class Board:
    def __init__(self):
        #self.board = [[0 for j in range(n)] for i in range(n)]
        self.boats = []
        self.boat_type = {"submarines": 1, "destructorBoat": 2,
                          "cruises": 3, "aircraftCarrier": 4}

    def draw_board(self, win):
        win.fill(BLUE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, DARK_BLUE, (row * SQUARE_SIZE,
                                 col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Genera un posicion aleatoria en el tablero

    def random_position(self, n):
        return randint(0, n - 1), randint(0, n - 1)

    # Creo un tablero vacio

    def createBoard(self, n):
        return [[0 for j in range(n)] for i in range(n)]

    # Revisa cuantos lugares estan vacios

    def spaces(self, board):
        sum = 0
        for t in board:
            sum += t.count(0)

        return sum

    # cuanta los espacios que ocupan todos los barcos

    def num_positions(self, boats):
        counter = 0
        for b in boats:
            counter += b.getSize()
        return counter

    # posiciona los barcos en el tablero

    def position_ships(self, board, boats, counter):
        if counter == len(boats):
            return 1

        x, y = self.random_position(len(board))

        while board[x][y] != 0:
            x, y = self.random_position(len(board))

        if not boats[counter].locate(board, 0, x, y):
            return 0

        if self.position_ships(board, boats, counter + 1) == 1:
            return 1

    # Devuelve el tablero con los barcos posicionados (si es posible hacerlo)

    def battleship(self, boats, n):
        for b in boats:
            if n < b.getSize():
                return None

        counter = self.num_positions(boats)
        if counter > n**2:
            return None
        else:
            board = self.createBoard(n)
            self.position_ships(board, boats, 0)
            availables = self.spaces(board)

            while availables != n**2 - counter:
                board = self.createBoard(n)
                self.position_ships(board, boats, 0)
                availables = self.spaces(board)

            return board

    # Recibe una coordenada de disparo

    def shot(self, board, boats, x, y):
        if board[x][y] == -1:
            return False

        boat = None
        id = board[x][y]

        for b in boats:
            if b.getId() == id:
                boat = b
                break

        board[x][y] = -1

        if boat == None:
            return False

        if not boat.isDestroyed():
            boat.addPointDestroyed((x, y))
            return True

        return False

    # Revisa si queda algun barco sin destruir

    def isEnd(self, boats):
        for b in boats:
            if not b.isDestroyed():
                return False
        return True

    # genera el numero de barcos segun el tipo:
    # paremetros:
    # name = nombre del barco
    # n = numero de barcos de ese tipo

    def addBoats(self, name, n):
        self.boats = []
        m = self.boat_type[name]

        for i in range(n):
            self.boats.append(Boat(name, m, 10 * m + i + 1))

        return self.boats

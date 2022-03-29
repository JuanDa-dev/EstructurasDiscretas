from random import randint

def random_position(n):
    return randint(0, n - 1), randint(0, n - 1)


def createBoard(n):
    return [[0 for j in range(n)] for i in range(n)]


def spaces(board):
    sum = 0
    for t in board:
        sum += t.count(0)

    return sum


def num_positions(boats):
    counter = 0
    for b in boats:
        counter += b.getSize()
    return counter


def position_ships(board, boats, counter):
    if counter == len(boats):
        return 1

    x, y = random_position(len(board))

    while board[x][y] != 0:
        x, y = random_position(len(board))

    if not boats[counter].locate(board, 0, x, y):
        return 0

    if position_ships(board, boats, counter + 1) == 1:
        return 1


def battleship(boats, n):
    counter = num_positions(boats)
    if counter > n**2:
        return None
    else:
        board = createBoard(n)
        position_ships(board, boats, 0)
        availables = spaces(board)

        while availables != n**2 - counter:
            board = createBoard(n)
            position_ships(board, boats, 0)
            availables = spaces(board)

        return board


def shot(board, boats, x, y):
    boat = None
    id = board[x][y]

    for b in boats:
        if b.getId() == id:
            boat = b
            break

    if boat == None:
      return False

    if not boat.isDestroyed():
        boat.addPointDestroyed((x, y))
        return True

    return False


def isEnd(boats):
    for b in boats:
        if not b.isDestroyed():
            return False
    return True
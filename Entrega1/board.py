from random import randint
from boat import Boat

# Genera un posicion aleatoria en el tablero
def random_position(n):
    return randint(0, n - 1), randint(0, n - 1)

# Creo un tablero vacio
def createBoard(n):
    return [[0 for j in range(n)] for i in range(n)]

# Revisa cuantos lugares estan vacios
def spaces(board):
    sum = 0
    for t in board:
        sum += t.count(0)

    return sum

# cuanta los espacios que ocupan todos los barcos
def num_positions(boats):
    counter = 0
    for b in boats:
        counter += b.getSize()
    return counter

# posiciona los barcos en el tablero
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

# Devuelve el tablero con los barcos posicionados (si es posible hacerlo)
def battleship(boats, n):
    for b in boats:
      if n < b.getSize():
        return None

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

# Recibe una coordenada de disparo
def shot(board, boats, x, y):
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
def isEnd(boats):
    for b in boats:
        if not b.isDestroyed():
            return False
    return True

boat_type = {"submarines": 1,"destructorBoat": 2, "cruises": 3, "aircraftCarrier": 4}
# genera el numero de barcos segun el tipo:
# paremetros:
# name = nombre del barco
# n = numero de barcos de ese tipo
def addBoats(name, n):
  boats = []
  m = boat_type[name]

  for i in range(n):
    boats.append(Boat(name, m, 10 * m + i + 1))
  
  return boats
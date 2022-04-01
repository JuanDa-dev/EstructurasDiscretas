# Boats in the battleship

class Boat:

    # Submarine size onboard is 1
    # DestructorBoat size onboard is 2
    # Cruiser size onboard is 3
    # AircraftCarrier size onboard is 4

    def __init__(self, name : str, size : int, id : int):
        self._name = name
        self._size = size
        self._id = id
        self._destroyed = False
        self._damage = 0
        self._points_destroyed = []

    '''def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))'''

    def getName(self):
        return self._name

    def getSize(self):
        return self._size

    def getId(self):
        return self._id

    def isDestroyed(self):
        return self._destroyed

    def setDestroyed(self, destroyed):
        self._destroyed = destroyed

    def getDamage(self):
        return self._damage

    def setDamage(self, damage):
        self._damage = damage

    def addPointDestroyed(self, p):
        self._points_destroyed.append(p)
        self.setDamage(self.getDamage() + 1)
        if len(self._points_destroyed) == self.getSize():
            self.setDestroyed(True)

    def containsPoint(self, p):
        return p in self._points_destroyed

    # Ubicar un punto en el tablero
    def locate(self, board, counter, x, y, location=""):
        if counter == self._size:
            return True
        
        if (0 <= x < len(board)) and (0 <= y < len(board)) and board[x][y] == 0:
            board[x][y] = self._id

            if (location == "RIGHT" or len(location) == 0) and self.locate(board, counter + 1, x + 1, y, "RIGHT"):
                return True

            if (location == "LEFT" or len(location) == 0) and self.locate(board, counter + 1, x - 1, y, "LEFT"):
                return True

            if (location == "UP" or len(location) == 0) and self.locate(board, counter + 1, x, y + 1, "UP"):
                return True

            if (location == "DOWN" or len(location) == 0) and self.locate(board, counter + 1, x, y - 1, "DOWN"):
                return True

            board[x][y] = 0

        return False

    """def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, WIN, IMG):
        WIN.blit(IMG, (self.x, self.y))"""

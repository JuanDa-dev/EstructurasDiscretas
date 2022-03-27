# Boats in the battleship

class Boat:

    # Submarine size onboard is 1
    # DestructorBoat size onboard is 2
    # Cruiser size onboard is 3
    # aircraftCarrier size onboard is 4

    def __init__(self, x, y, size, name):
        self.x = x
        self.y = y
        self.size = size

        self.name = name

    '''def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))'''

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, WIN, IMG):
        WIN.blit(IMG, (self.x, self.y))

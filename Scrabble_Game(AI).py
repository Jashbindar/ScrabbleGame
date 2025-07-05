#Scrabble Game
'''
Things to do;
i) rack
ii) words
iii) bag (done)
iv) player
v) board
vi) tile (done)
'''

import random

LETTER_VALUES = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 1,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10,
    ' ': 0
}

class Tile:
    #initializing the tiles
    def __init__(self, letter, letter_value):
        self.letter = letter.upper()
        if self.letter in letter_value:
            self.score = letter_value[self.letter]
        else:
            self.score = 0

    #returns the letter
    def getLetter(self):
        return self.letter
    
    #returns the score
    def getScore(self):
        return self.score

class Bag:
    #initilizes a bag full of tiles
    def __init__(self):
        self.bag = []
        self.initialize_bag()

    def addToBag(self, tile, quantity):
        for i in range(quantity):
            self.bag.append(tile)
    
    def initialize_bag(self):
        global LETTER_VALUES
        self.addToBag(Tile("A", LETTER_VALUES), 9)
        self.addToBag(Tile("B", LETTER_VALUES), 2)
        self.addToBag(Tile("C", LETTER_VALUES), 2)
        self.addToBag(Tile("D", LETTER_VALUES), 4)
        self.addToBag(Tile("E", LETTER_VALUES), 12)
        self.addToBag(Tile("F", LETTER_VALUES), 2)
        self.addToBag(Tile("G", LETTER_VALUES), 3)
        self.addToBag(Tile("H", LETTER_VALUES), 2)
        self.addToBag(Tile("I", LETTER_VALUES), 9)
        self.addToBag(Tile("J", LETTER_VALUES), 1)
        self.addToBag(Tile("K", LETTER_VALUES), 1)
        self.addToBag(Tile("L", LETTER_VALUES), 4)
        self.addToBag(Tile("M", LETTER_VALUES), 2)
        self.addToBag(Tile("N", LETTER_VALUES), 6)
        self.addToBag(Tile("O", LETTER_VALUES), 8)
        self.addToBag(Tile("P", LETTER_VALUES), 2)
        self.addToBag(Tile("Q", LETTER_VALUES), 1)
        self.addToBag(Tile("R", LETTER_VALUES), 6)
        self.addToBag(Tile("S", LETTER_VALUES), 4)
        self.addToBag(Tile("T", LETTER_VALUES), 6)
        self.addToBag(Tile("U", LETTER_VALUES), 4)
        self.addToBag(Tile("V", LETTER_VALUES), 2)
        self.addToBag(Tile("W", LETTER_VALUES), 2)
        self.addToBag(Tile("X", LETTER_VALUES), 1)
        self.addToBag(Tile("Y", LETTER_VALUES), 2)
        self.addToBag(Tile("Z", LETTER_VALUES), 1)
        self.addToBag(Tile(" ", LETTER_VALUES), 2)
        
        random.shuffle(self.bag)

    def getTile(self):
        return self.bag.pop()
    
    def remainingTiles(self):
        return len(self.bag)


class Rack:
    def __init__(self, bag):
        self.rack = []
        self.bag = bag

    def addToRack(self):
        self.rack.append(self.bag.getTile())

    def initialize_rack(self):
        for i in range(7):
            self.addToRack()

    def removeTile(self, tile):
        return self.rack.remove(tile)
    
    def rackString(self):
        return ", ".join(tile.getLetter() for tile in self.rack)
    
bag = Bag()
rack = Rack(bag)
rack.initialize_rack()
output = rack.rackString()
print(output)
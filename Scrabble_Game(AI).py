#Scrabble Game
'''
Things to do;
i) rack (done)
ii) words
iii) bag (done)
iv) player (done)
v) board
vi) tile (done)
'''

import random
import itertools

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
        self.addToBag(Tile("*", LETTER_VALUES), 2)
        
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

    def removeTileByLetter(self, letter):
        for tile in self.rack:
            if tile.getLetter() == letter:
                self.rack.remove(tile)
                break
    
    def rackString(self):
        return ", ".join(tile.getLetter() for tile in self.rack)
    
    def rackArray(self):
        return self.rack
    
    def rackTotal(self):
        return len(self.rack)
    
    def restockRack(self):
        while self.rackTotal() < 7 and self.bag.remainingTiles() > 0:
            self.addToRack()

class Board:
    def __init__(self):
        self.board = []
        self.boardDesign()

    def add_premium_squares(self):
            TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
            DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
            TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
            DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

            for coordinate in TRIPLE_WORD_SCORE:
                self.board[coordinate[0]][coordinate[1]] = "TWS"
            for coordinate in TRIPLE_LETTER_SCORE:
                self.board[coordinate[0]][coordinate[1]] = "TLS"
            for coordinate in DOUBLE_WORD_SCORE:
                self.board[coordinate[0]][coordinate[1]] = "DWS"
            for coordinate in DOUBLE_LETTER_SCORE:
                self.board[coordinate[0]][coordinate[1]] = "DLS"    

    def boardDesign(self):
        for i in range(15):
            row = []
            for j in range(15):
                row.append("   ")
            self.board.append(row)

        self.board[7][7] = " * "
        self.add_premium_squares()

    def display_board(self):
        print("\n" + "="*50)
        print("             SCRABBLE BOARD")
        print("="*50)
        
        print("   ", end="")
        for col in range(15):
            print(f"{col:2d} ", end="")
        print()

        for row in range(15):
            print(f"{row:2d} |", end="")
            for col in range(15):
                cell = self.board[row][col]
                print(f"{cell}", end="")
            print(f"| {row}")

        print("   ", end="")
        for col in range(15):
            print(f"{col:2d} ", end="")
        print()
        print("="*50)

    def placeWord(self, word, location, direction, player):
        multiplierSpots = []
        direction = direction.upper()
        word = word.upper()
        row, col = location[0], location[1] + i

        if direction.upper() == "RIGHT":
            for i in range(len(word)):
            #check for multipliers
                if self.board[row][col] in ["TWS", "DWS", "TLS", "DLS"]:
                    multiplierSpots.append((word[i], self.board[row][col]))
                    self.board[location[0]][location[1]+i] = " " + word[i] + " "

            if direction.upper() == "DOWN":
                for i in range(len(word)):
                    if self.board[row][col] in ["TWS", "DWS", "TLS", "DLS"]:    
                        multiplierSpots.append((word[i], self.board[row][col]))
                    self.board[row][col] = " " + word[i] + " "

            return multiplierSpots


class Player:
    def __init__(self, bag):
        self.name = None
        self.rack = Rack(bag)
        self.score = 0

    def playerName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def getPlayerRack(self):
        return self.rack.rackString()
    
    def scoreIncrement(self, increase):
        self.score += increase

    def getScore(self):
        return self.score
    

class PlayerBot(Player):
    def __init__(self, bag):
        #calls in parent Player class
        super().__init__(bag)
        self.dictionary = self.loadDictionary()
    
    def loadDictionary(self):
        basic_words = {
            'CAT', 'BAT', 'RAT', 'HAT', 'SAT', 'MAT', 'PAT', 'FAT',
            'THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL',
            'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'OUT', 'DAY', 'GET',
            'RATE', 'TEAR', 'TIRE', 'RIOT', 'TONE', 'NOTE', 'RENT',
            'STUD', 'SLUG', 'GLUM', 'DUMP', 'PLUM', 'SLUM', 'GUST',
            'WORD', 'WORK', 'WENT', 'WANT', 'WALK', 'TALK', 'TAKE',
            'MAKE', 'LIKE', 'TIME', 'HAVE', 'GAME', 'CAME', 'NAME',
            'SAME', 'SOME', 'HOME', 'COME', 'DONE', 'GONE', 'TONE',
            'BONE', 'ZONE', 'HOPE', 'ROPE', 'COPE', 'DOPE', 'NOPE',
            'TAPE', 'CAPE', 'GAPE', 'SHAPE', 'GRAPE', 'PLACE', 'SPACE',
            'FACE', 'RACE', 'PACE', 'LACE', 'MACE', 'NICE', 'RICE',
            'DICE', 'MICE', 'VICE', 'TWICE', 'PRICE', 'SLICE', 'SPICE'
        }

        return basic_words
    
    def wordValidity(self, word):
        validity = word.upper() in self.dictionary
        return validity
    
    def possibleWords(self):
        rack_letters = []
        for tile in self.rack.rack:
            rack_letters.append(tile.getLetter())

        possible_Words = []

        max_length = min(8, len(rack_letters) + 1)

        for length in range(2, max_length):
            # generates all of the combination for word within the length
            for combination in itertools.combinations(rack_letters, length):
                # tries all of the letter arrangements of the given combination
                for arrangement in itertools.permutations(combination):
                    # joins the letters together to create a word
                    word = ''.join(arrangement)

                    if self.wordValidity(word) and word not in possible_Words:
                        possible_Words.append(word)

        return possible_Words


    def createWord(self, word, player):
        rack_letters = []
        for tile in player.rack.rack:
            rack_letters.append(tile.getLetter())

        word_letter = list(word.upper())
        
        for letter in word_letter:
            if letter in rack_letters:
                rack_letters.remove(letter)
            else:
                return False
            
        for letter in word_letter:
            player.rack.removeTileByLetter(letter)

        player.rack.restockRack()

        return True
            


        






# TEST THE AI
print("=== TESTING SCRABBLE AI ===\n")

# Create bag and AI player
bag = Bag()
ai_player = PlayerBot(bag)
ai_player.playerName("AI Bot")

# Initialize AI rack
ai_player.rack.initialize_rack()

# Show AI info
print(f"AI Player Name: {ai_player.getName()}")
print(f"AI Rack: {ai_player.getPlayerRack()}")
print(f"AI Score: {ai_player.getScore()}")
print(f"Remaining Tiles in Bag: {bag.remainingTiles()}")

# Test AI word finding
print("\n=== AI WORD FINDING TEST ===")
print("Finding all possible words from AI's rack...")

possible_words = ai_player.possibleWords()

if possible_words:
    print(f"AI found {len(possible_words)} possible words:")
    for i, word in enumerate(possible_words, 1):
        print(f"{i}. {word}")
        can_create = ai_player.createWord(word, ai_player)
        if can_create:
            print('Can create? -> YES')
        else:
            print('Can create? -> NO')

    print(ai_player.rack.rackString())
else:
    print("AI couldn't find any words with current rack.")
    print("This might happen if the rack has very few vowels or common letters.")

if __name__ == "__main__":
    board = Board()
    board.display_board()
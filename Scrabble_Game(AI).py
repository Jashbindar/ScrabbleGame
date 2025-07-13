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

import heapq
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
    '#': 0
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
    
    def rackArr(self):
        return self.rack
    
    def scoreIncrement(self, increase):
        self.score += increase

    def getScore(self):
        return self.score

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
        placed_tiles = []
        direction = direction.upper()
        word = word.upper()
        row, col = location

        if direction == "RIGHT":
            for i in range(len(word)):
                if self.board[row][col + i] in ["TWS", "DWS", "TLS", "DLS"]:
                    placed_tiles.append((word[i], self.board[row][col + i]))
                else:
                    placed_tiles.append((word[i], None))
                self.board[row][col + i] = " " + word[i] + " "

        elif direction == "DOWN":
            for i in range(len(word)):
                if self.board[row + i][col] in ["TWS", "DWS", "TLS", "DLS"]:
                    placed_tiles.append((word[i], self.board[row + i][col]))
                else:
                    placed_tiles.append((word[i], None))
                self.board[row + i][col] = " " + word[i] + " "

        for letter in word:
            player.rack.removeTileByLetter(letter)
        player.rack.restockRack()

        return placed_tiles

    def boardArray(self):
        return self.board




    
class Words:  
    def __init__(self, word, location, direction, board, player):
        self.word = word.upper()
        self.location = location
        self.direction = direction.upper()
        self.board = board
        self.player = player

    def calculateScore(self, words):
        score = 0
        for letter in words.upper():
            if letter in LETTER_VALUES:
                score += LETTER_VALUES[letter]
        return score
    
    '''
    def checkWord(self, direction, location):
        global roundNumber, players

        if 'roundNumber' not in globals():
            roundNumber = 1
        if 'players' not in globals():
            players = [self.player]

        universalTile = ""
        currentBoardLetter = ""
        neededTiles = ""

        if self.word != " ":
            if "#" in self.word:
                while universalTile != "":
                    universalTile = input(print("Please enter a letter into this tile: "))
                self.word = self.word.replace("#", universalTile.upper(), 1)

            if self.direction == "RIGHT":
                for i in range(len(self.word)):
                    if self.board[self.location[0]][self.direction[1] + i][1] == " " or self.board[self.location[0]][self.direction[1] + i] == "TLS" or self.board[self.location[0]][self.direction[1] + i] == "DLS" or self.board[self.location[0]][self.direction[1] + i] == "TWS" or self.board[self.location[0]][self.direction[1] + i] == "DWS" or self.board[self.location[0]][self.direction[1] + i] == "*":
                        currentBoardLetter += " "
                    else:
                        currentBoardLetter += self.board[self.location[0]][self.location[1]+i][1]
            elif self.direction == "DOWN":
                for i in range(len(self.word)):
                    if self.board[self.location[0] + i][self.direction[1]][1] == " " or self.board[self.location[0] + i][self.direction[1]] == "TLS" or self.board[self.location[0] + i][self.direction[1]] == "DLS" or self.board[self.location[0] + i][self.direction[1]] == "TWS" or self.board[self.location[0] + i][self.direction[1]] == "DWS" or self.board[self.location[0] + i][self.direction[1]] == "*":
                        currentBoardLetter += " "
                    else:
                        currentBoardLetter += self.board[self.location[0] + i][self.location[1]][1]
            else:
                print("Enter a valid direction.")

            for i in range(len(self.word)):
                if currentBoardLetter[i] == " ":
                    neededTiles += self.word[i]
                elif currentBoardLetter[i] != self.word[i]:
                    print(f"Current board letter: {currentBoardLetter}, Word: {self.word}, Needed tiles: {neededTiles}")
                    return print("Make sure that your words do not overlap other words on the board")
                
            if currentBoardLetter == " " * len(self.word):
                print(f"Current board letter: {currentBoardLetter}, Word: {self.word}, Needed tiles: {neededTiles}")
                return print("Make sure that your words do not overlap other words on the board")
            
            if roundNumber == 1 and players[0] == self.player and self.location != (7,7):
                return print("the first turn must always start that in the middle of the board.\n")
        else:
            ans = input(print("Are you sure you want to skip your turn? (Y/N): "))
            ans == ans.upper()

            if ans == "Y":
                if roundNumber == 1:
                    print("Unable to skip please enter a word since its the first round")
                return True
            else:
                return print("Please enter a word")
    '''
            
    def calculateWordScore(placed_tiles):
        word_multiplier = 1
        score = 0

        for letter, special in placed_tiles:
            letter_score = LETTER_VALUES[letter]
            if special == "TLS":
                letter_score *= 3
            elif special == "DLS":
                letter_score *= 2
            elif special == "TWS":
                word_multiplier *= 3
            elif special == "DWS":
                word_multiplier *= 2
            score += letter_score

        return score * word_multiplier
            
    def set_word(self, word):
        self.word = word.upper()

    def set_location(self, location):
        self.location = location

    def set_direction(self, direction):
        self.direction = direction
    
    def getWord(self):
        return self.word
        


            

class PlayerBot(Player):
    def __init__(self, bag):
        #calls in parent Player class
        super().__init__(bag)
        self.dictionary = self.loadLocalDictionary()

    def loadLocalDictionary(self):
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
    
    def calculateScore(self, word):
        return Words.calculateScore(self, word)

    def possibleWords(self):
        rack_letters = []
        visited = set()

        for tile in self.rack.rack:
            rack_letters.append(tile.getLetter())

        possible_words = []

        pq = [(0, "", set(range(len(rack_letters))))]

        while pq:
            negScore, current_word, availableLetters = heapq.heappop(pq)

            temp_Word = (current_word, tuple(availableLetters))
            if temp_Word not in visited:
                visited.add(temp_Word)
            
            if (len(current_word) >= 1 and self.wordValidity(current_word)):
                if current_word not in possible_words:
                    possible_words.append(current_word)

            for i in availableLetters:
                newWord = current_word + rack_letters[i]
                newAvailableLetter = availableLetters - {i}
                newScore = self.calculateScore(newWord)
                heapq.heappush(pq, (-newScore, newWord, newAvailableLetter))

        return possible_words
        
    def getBestWord(self):
        rack_letters = []
        visited = set()

        for tile in self.rack.rack:
            rack_letters.append(tile.getLetter())

        best_word = ""
        best_score = 0

        pq = [(0, "", set(range(len(rack_letters))))]

        while pq:
            neg_score, current_word, availableLetter = heapq.heappop(pq)
            current_score = -neg_score
            
            temp_Word = (current_word, tuple(availableLetter))
            if temp_Word not in visited:
                visited.add(temp_Word)

            if (len(current_word) >= 1 and self.wordValidity(current_word)):
                if current_score > best_score:
                    best_score = current_score
                    best_word = current_word

            for i in availableLetter:
                newWord = current_word + rack_letters[i]
                newAvailableLetter = availableLetter - {i}
                newScore = self.calculateScore(newWord)
                heapq.heappush(pq, (-newScore, newWord, newAvailableLetter))

        return best_word, best_score

    def exchangeTiles(self):
        self.bag = Bag
        for i in range(len(self.rack.rack)):
            self.rack.removeTileByLetter(i)
            self.bag.addToBag(7, 7)
        self.bag.restockRack()
        return


        






def play_scrabble_game():
    bag = Bag()
    board = Board()
    board.display_board()

    # Create players
    human = Player(bag)
    human.playerName(input("Enter your name: "))
    human.rack.initialize_rack()

    ai = PlayerBot(bag)
    ai.playerName("AI Bot")
    ai.rack.initialize_rack()

    players = [human, ai]
    current_turn = 0

    # === TEST SECTION: Exchange Tiles ===
    print("\n=== TESTING PlayerBot.exchangeTiles() ===")
    print("Before exchange:")
    print(f"AI Rack: {ai.getPlayerRack()}")
    ai.exchangeTiles()
    print("After exchange:")
    print(f"AI Rack: {ai.getPlayerRack()}")
    print("========================================\n")

    # === MAIN GAME LOOP ===
    while bag.remainingTiles() > 0 and human.rack.rackTotal() > 0:
        current_player = players[current_turn % 2]
        print(f"\n--- {current_player.getName()}'s Turn ---")
        board.display_board()
        print(f"{current_player.getName()} Rack: {current_player.getPlayerRack()}")

        if isinstance(current_player, PlayerBot):
            word, score = current_player.getBestWord()
            if not word:
                print(f"{current_player.getName()} skips turn (no valid words).")
            else:
                location = (7, 7) if current_turn == 0 else (random.randint(0, 14), random.randint(0, 14))
                direction = random.choice(["RIGHT", "DOWN"])

                print(f"{current_player.getName()} plays '{word}' at {location} going {direction}.")
                placed_tiles = placeWord(board, word, location, direction, current_player)
                word_score = Words.calculateWordScore(placed_tiles)
                current_player.scoreIncrement(word_score)
                print(f"{current_player.getName()} scored {word_score} points.")
        else:
            word = input("Enter a word to play (or 'skip'): ").upper()
            if word == "SKIP":
                print("Turn skipped.")
            else:
                location = tuple(map(int, input("Enter starting position (row col): ").split()))
                direction = input("Enter direction (RIGHT/DOWN): ").upper()

                try:
                    placed_tiles = placeWord(board, word, location, direction, current_player)
                    word_score = Words.calculateWordScore(placed_tiles)
                    current_player.scoreIncrement(word_score)
                    print(f"{current_player.getName()} scored {word_score} points.")
                except Exception as e:
                    print(f"Invalid move: {e}")
                    continue  # Let the player retry

        current_turn += 1
        print(f"Score - {human.getName()}: {human.getScore()} | {ai.getName()}: {ai.getScore()}")

    print("\n=== Game Over ===")
    board.display_board()
    print(f"Final Scores - {human.getName()}: {human.getScore()} | {ai.getName()}: {ai.getScore()}")
    if human.getScore() > ai.getScore():
        print(f"{human.getName()} wins!")
    elif human.getScore() < ai.getScore():
        print(f"{ai.getName()} wins!")
    else:
        print("It's a tie!")


# Start the game
play_scrabble_game()

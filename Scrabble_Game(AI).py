#Scrabble Game
'''
Things to do;
i) rack (done)
ii) words
iii) bag (done)
iv) player (done)
v) tile (done)

plan to remove board as it is difficult to allow the bot to analyse the board to place a continuing word
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

    #returns the letter
    def getLetter(self):
        return self.letter

class Bag:
    #initilizes a bag full of tiles
    def __init__(self):
        self.bag = []
        self.initialize_bag()

    def addToBag(self, letter, quantity):
        for i in range(quantity):
            self.bag.append(Tile(letter, LETTER_VALUES))
    
    def initialize_bag(self):
        self.addToBag("A", 9)
        self.addToBag("B", 2)
        self.addToBag("C", 2)
        self.addToBag("D", 4)
        self.addToBag("E", 12)
        self.addToBag("F", 2)
        self.addToBag("G", 3)
        self.addToBag("H", 2)
        self.addToBag("I", 9)
        self.addToBag("J", 1)
        self.addToBag("K", 1)
        self.addToBag("L", 4)
        self.addToBag("M", 2)
        self.addToBag("N", 6)
        self.addToBag("O", 8)
        self.addToBag("P", 2)
        self.addToBag("Q", 1)
        self.addToBag("R", 6)
        self.addToBag("S", 4)
        self.addToBag("T", 6)
        self.addToBag("U", 4)
        self.addToBag("V", 2)
        self.addToBag("W", 2)
        self.addToBag("X", 1)
        self.addToBag("Y", 2)
        self.addToBag("Z", 1)
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
    
    def getRack(self):
        return ", ".join(tile.getLetter() for tile in self.rack)
    
    def rackTotal(self):
        return len(self.rack)
    
    def numberOfTiles(self):
        return len(self.rack)
    
    def restockRack(self):
        while self.rackTotal() < 7 and self.bag.remainingTiles() > 0:
            self.addToRack()

    def exchangeTiles(self, tile_to_exchange=None):
        if self.bag.remainingTiles() <= 0:
            print("There is not enough tiles to exchange with.")
            return False

        tile_to_return = []

        if tile_to_exchange is None:
            #logic for AI to exchange tile
            if len(self.rack) > 0:
                tile_to_remove = random.choice(self.rack)
                self.rack.remove(tile_to_remove)
                tile_to_return.append(tile_to_remove)
        else:
            #original logic for player tile exchange
            letter_to_change = tile_to_exchange.upper()
            for letter in letter_to_change:
                found = False
                for tile in self.rack:
                    if tile.getLetter() == letter:
                        self.rack.remove(tile)
                        tile_to_return.append(tile)
                        found = True
                        break
                if not found:
                    print(f"Tile '{letter}' not found in rack. Cannot exchange.")
                    return False

        for tile in tile_to_return:
            self.bag.bag.append(tile)

        random.shuffle(self.bag.bag)

        self.restockRack()
        return True


class Player:
    def __init__(self, bag):
        self.name = None
        self.rack = Rack(bag)
        self.score = 0

    def playerName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def scoreIncrement(self, increase):
        self.score += increase

    def getScore(self):
        return self.score


   
class Words:  
    def __init__(self, word, player):
        self.word = word.upper()
        self.player = player
        self.dictionary = self.load_dictionary()
    
    def load_dictionary(self):
        dictionary = open("dic.txt").read().splitlines()
        return dictionary
    
    def calculateScore(self, words):
        score = 0
        for letter in words.upper():
            if letter in LETTER_VALUES:
                score += LETTER_VALUES[letter]
        return score
    
    def wordValidity(self, word):
        validity = word.upper() in self.dictionary
        return validity
      

class PlayerBot(Player):
    def __init__(self, bag):
        #calls in parent Player class
        super().__init__(bag)
        self.max_limit = 500
        
    def getBestWord(self):
        rack_letters = []
        visited = set()

        for tile in self.rack.rack:
            rack_letters.append(tile.getLetter())

        best_word = ""
        best_score = 0
        iterationCount = 0

        pq = [(0, "", set(range(len(rack_letters))))]

        while pq and iterationCount < self.max_limit:
            iterationCount += 1
            neg_score, current_word, availableLetter = heapq.heappop(pq)
            current_score = -neg_score
            
            temp_Word = (current_word, tuple(availableLetter))
            if temp_Word not in visited:
                visited.add(temp_Word)

            if (len(current_word) >= 1 and Words(current_word, self).wordValidity(current_word)):
                if current_score > best_score:
                    best_score = current_score
                    best_word = current_word

            for i in availableLetter:
                newWord = current_word + rack_letters[i]
                # Create a new set of available letters without the current letter
                newAvailableLetter = availableLetter.copy()
                #why discard()? -> because discard will not raise an error "KeyError" if the element is not found unlike remove()
                newAvailableLetter.discard(i)
                newScore = Words(current_word, self).calculateScore(newWord)
                heapq.heappush(pq, (-newScore, newWord, newAvailableLetter))

        return best_word, best_score



def play_game():
    bag = Bag()
    player = Player(bag)
    bot = PlayerBot(bag)

    player_name = input("\nEnter your name: ")

    player.playerName(player_name)
    bot.playerName("AI player")

    player.rack.initialize_rack()
    bot.rack.initialize_rack()

    rounds = int(input("\nHow many rounds do you wish to play?: "))

    for i in range(1, rounds + 1):
        print(f"\nRound {i}\n")
        print(f"{player.getName()}'s Rack: {player.rack.getRack()}")

        while True:
            try:
                choice = int(input("\nPlay a Word (1)\nExchange a word (2)\nOption: "))
                if choice in [1, 2]:
                    break
            except ValueError:
                print("Select the given options!")
    

        match choice:
            case 1:
                print(f"{player.getName()}'s Rack: {player.rack.getRack()}")
                temp_word = input("\nEnter the word you wish to play: ").upper()

                #will only allow the player to play a word if it is valid and within the rack limit
                #loop will only run if all the arguments stated are TRUE
                if all(temp_word.count(letter) <= player.rack.getRack().count(letter) for letter in temp_word):
                    word = Words(temp_word, player)
                    if word.wordValidity(temp_word):
                        word = Words(temp_word, player)
                        score = word.calculateScore(temp_word)
                        player.scoreIncrement(score)
                        
                        for letter in temp_word:
                            player.rack.removeTileByLetter(letter)
                        player.rack.restockRack()

                        print(f"{player.getName()} has created the word with the score of {score}.")
                    else:
                        print("Invalid word: Enter a word that is in the dictionary")
                else:
                    print("Invalid word: Enter a word that is within your rack limit")

            case 2:
                print(f"{player.getName()}'s Rack: {player.rack.getRack()}")
                tile_to_exchange = str(input("Enter the letter you wish to exchange: "))
                player.rack.exchangeTiles(tile_to_exchange)
                print(player.rack.getRack())

        print(f"\n{bot.getName()} is creating a word...")
        print(bot.rack.getRack())
        bot_word, bot_score = bot.getBestWord()
        if bot_word:
            for letter in bot_word:
                bot.rack.removeTileByLetter(letter)
            bot.rack.restockRack()
            bot.scoreIncrement(bot_score)
        else:
            bot.rack.exchangeTiles()
            print(f"{bot.getName()} skips their turn (no valid word)")
            if bot.rack.exchangeTiles():
                print(bot.rack.getRack())
            else:
                print("bot didnt exchange")

        print(f"{bot.getName()} has created the word {bot_word}")
        print(f"{bot.getName()} has created a word with the points of {bot_score}.")
        print("\n=== Final Scores ===")
        print(f"{player.getName()}: {player.getScore()} points")
        print(f"{bot.getName()}: {bot.getScore()} points")

    if player.getScore() > bot.getScore():
        print("🎉 You win!")
    elif player.getScore() < bot.getScore():
        print("🤖 Bot wins!")
    else:
        print("🤝 It's a tie!")

play_game()

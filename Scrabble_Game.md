# Scrabble Game (Python)

This project is a simplified Scrabble game implemented in Python. It supports a human player and an AI bot, with features for playing words, exchanging tiles, and scoring.

---

## Features

- **Tile, Bag, Rack, Player, and Words classes** for game logic.
- **AI Bot** that finds the best scoring word from its rack.
- **Word validation** using a dictionary file (`dic.txt`).
- **Tile exchange** and rack restocking.
- **Score calculation** based on standard Scrabble letter values.
- **Simple command-line interface** for gameplay.

---

## How to Play

1. **Start the game**:  
   Run the script.  
   ```
   python # Scrabble_Game(AI)
   ```

2. **Enter your name** and the number of rounds.

3. **Each round**:
   - View your rack.
   - Choose to play a word or exchange a tile.
   - If playing a word, enter a valid word using your rack letters.
   - If exchanging, specify the letter to exchange.

4. **AI bot** will play its turn automatically.

5. **Scores** are displayed after each round.

---

## Main Classes

- **Tile**: Represents a single letter tile.
- **Bag**: Holds all remaining tiles and manages drawing/shuffling.
- **Rack**: Holds a player's current tiles and manages exchanges.
- **Player**: Represents a human player.
- **PlayerBot**: Inherits from Player, implements AI logic.
- **Words**: Handles word validation and scoring.

---

## Example Game Flow

```
Enter your name: Alice
How many rounds do you wish to play?: 3

Round 1

Alice's Rack: T, D, S, A, R, E, R

Play a Word (1)
Exchange a word (2)
Option: 1

Enter the word you wish to play: READS
Alice has created the word with the score of 6.

AI player is creating a word...
AI player has created the word TEAR
AI player has created a word with the points of 4.

=== Final Scores ===
Alice: 6 points
AI player: 4 points
```

---

## Requirements

- Python 3.x
- A dictionary file named `dic.txt` in the same directory (one valid word per line, uppercase).

---

## Customization

- **Dictionary**: Replace `dic.txt` with your own word list.
- **Rounds**: Change the number of rounds as desired.
- **AI Difficulty**: Adjust `PlayerBot.max_limit` for more/less exhaustive AI word search.

---

## License

This project is for educational
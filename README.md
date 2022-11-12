# HiLo
HiLo is a game where a dealer will draw and display a card. The player will then make a guess if the next card will be higher or lower than the previously drawn card. Points are won or lost based on whether or not the player guessed correctly. This repeats until the game is over.

## Rules
---
Hilo is played according to the following rules.

- The player starts the game with 300 points.
- Individual cards are represented as a number from 1 to 13.
- The current card is displayed.
- The player guesses if the next one will be higher or lower.
- The the next card is displayed.
- The player earns 100 points if they guessed correctly.
- The player loses 75 points if they guessed incorrectly.
- If a player reaches 0 points the game is over.
- If a player has more than 0 points they decide if they want to keep playing.
- If a player decides not to play again the game is over.

## Design
---
The principle of abstraction is applied to represent a single player, a single card, and the game director. 

A class named Player will keep track of the players current points and current guess. It will have two attributes, self.current_points, which will be initialized with 300, self.current_guess which will store the users current guess, and self.play_again which will be initialized with 'y' to indicate the users desire to keep playing.

A class named Card will be used to represent a card drawn by the director. It will have one attribute, self.value, which will be initialized with a random value from 1 to 13.

A class named Director will control the flow of the game. It will have a primary method, self.start_game(), to start the game, initialize a player and first card, and control the main game loop. The loop will display the current card and get the players guess. A new card will be generated, displayed, and compared to players guess. Points are then updated. If the player still has points, the player will be asked if they want to play again. The loop will repeat as long as the player wants to keep playing and their points are above zero.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- hilo                (source code for game)
  +-- game              (game specific classes)
    +-- card.py         (class that impliments a single card)
    +-- director.py     (class that implements the dealer)
    +-- player.py       (class that implements the player)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8 or higher

## Authors
---
* M. Scott Reynolds (mscottreynolds+github@gmail.com)


# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python. You will practice string manipulation, loops, conditionals, and random selection by creating an interactive Hangman game where players guess letters to reveal a hidden word.

## 📝 Tasks

### 🛠️ Game Setup and Word Management

#### Description
Create the foundation of the Hangman game by setting up word selection and initializing the game state.

#### Requirements
Completed program should:

- Maintain a predefined list of words to choose from
- Randomly select a word at the start of the game
- Display the initial game state with blank spaces for each letter (_ _ _ format)
- Track the number of incorrect guesses remaining


### 🛠️ Game Loop and User Interaction

#### Description
Implement the main game loop that handles player guesses, updates the game state, and determines win/lose conditions.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Validate guesses and update the display to show correctly guessed letters
- Track incorrect guesses and decrement the remaining attempts
- Display current progress and guesses made so far
- End the game when the word is fully guessed (win) or attempts are exhausted (lose)
- Display appropriate win/lose messages with the final word revealed

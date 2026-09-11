#  Number Guessing Game
A simple **Number Guessing Game** built with Python. The computer randomly selects a number, and the player tries to guess it.

##  Description

The game generates a random number within a specified range. The player enters guesses until they correctly identify the hidden number.

After each guess, the program tells the player whether the guess is:

*  Too high
*  Too low
*  Correct

##  Technologies Used

* Python 3
* Python `random` module

##  How to Play

1. Run the Python program.
2. The computer generates a random number.
3. Enter your guess.
4. Follow the hints:

   * **Too high** → Try a smaller number.
   * **Too low** → Try a larger number.
   * **Correct** → You win!
5. The game may also count the number of attempts.

##  How to Run

Make sure Python is installed on your computer.

Open the terminal in the project folder and run:

```bash
python3 main.py
```

If your system uses `python` for Python 3, you can use:

```bash
python main.py
```

##  Project Structure

```text
number-guessing-game/
│
├── main.py
└── README.md
```

##  Example

```text
 Welcome to the Number Guessing Game!

Guess a number between 1 and 100: 50
 Too low!

Guess a number between 1 and 100: 75
 Too high!

Guess a number between 1 and 100: 63
 Correct! You won!
You guessed the number in 3 attempts.
```
##  Features

* Random number generation
* User input
* Guess validation
* Helpful hints
* Attempt counter
* Simple command-line interface

##  What I Learned

This project helps practice:

* Variables
* User input with `input()`
* Conditional statements (`if`, `elif`, `else`)
* Loops
* Functions
* Random number generation
* Basic Python programming logic

## Author
eDDie

Created as a beginner Python programming project.

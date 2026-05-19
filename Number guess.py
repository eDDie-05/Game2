import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

guessed = False

while not guessed:
    guess = int(input("Enter your guess: "))

    # Conditions
    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the correct number.")
        guessed = True
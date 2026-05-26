import random

secret = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

guesses = 0

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        print("You guessed it in", guesses, "attempts.")
        break

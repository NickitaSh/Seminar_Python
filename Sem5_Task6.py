import random

def guess_number(low, high, attempts):
    if attempts <= 0:
        print("You lose! The number was " + str(target_number))
        return

    guess = int(input("Guess a number between " + str(low) + " and " + str(high) + ": "))
    if guess == target_number:
        print("You guessed the number in " + str(10 - attempts + 1) + " attempts!")
    elif guess < target_number:
        print("Your guess is too low!")
        guess_number(guess + 1, high, attempts - 1)
    else:
        print("Your guess is too high!")
        guess_number(low, guess - 1, attempts - 1)

target_number = random.randint(0, 100)
guess_number(0, 100, 10)
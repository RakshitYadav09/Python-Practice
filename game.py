import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 10.")

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    attempts = 0

    while True:
        try:
            # Get the player's guess
            guess = int(input("Your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            else:
                print("Wrong guess. Try again!")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()

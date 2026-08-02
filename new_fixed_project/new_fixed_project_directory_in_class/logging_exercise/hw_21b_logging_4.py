import logging
import random

logging.basicConfig(
    level=logging.DEBUG,   # Change this to INFO or WARNING to see the difference
)

logging.info("Game started")

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number (1-100): "))

    logging.debug(f"Player guessed: {guess}")

    if guess < 1 or guess > 100:
        logging.warning("Guess is outside the range 1-100.")
        continue

    if guess == secret_number:
        logging.info("Player guessed the correct number!")
        print("🎉 You win!")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")
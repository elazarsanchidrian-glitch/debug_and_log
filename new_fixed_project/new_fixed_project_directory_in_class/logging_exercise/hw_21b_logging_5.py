import logging
import random

logging.basicConfig(
    filename="guess_number_debug.log",
    level=logging.INFO,
)

logging.info("Game started")

random_number = random.randint(1, 10)
logging.debug(f"Random number: {random_number}")

attempts = 0

while True:
    attempts += 1
    logging.debug(f"Attempts: {attempts}")

    guess = int(input("Guess a number (1-10): "))
    logging.info(f"User guessed: {guess}")

    if guess < 0 or guess > 10:
        logging.warning(f"Guess out of range: {guess}")
        continue

    if guess != random_number:
        print("Wrong guess. Try again.")
        continue

    logging.info(f"Player guessed correctly in {attempts} attempts")
    print(f"You guessed it in {attempts} attempts!")
    break
import logging

logging.basicConfig(
    filename="robot.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

x = 0
y = 0
move_counter = 0

TREASURE_X = 3
TREASURE_Y = 5

MIN = -5
MAX = 5

while True:
    command = input("Enter command (UP, DOWN, LEFT, RIGHT, QUIT): ").upper()

    if command == "QUIT":
        print(f"Final position: ({x}, {y})")
        logging.info("Game ended.")
        break

    elif command == "UP":
        y += 1

    elif command == "DOWN":
        y -= 1

    elif command == "LEFT":
        x -= 1

    elif command == "RIGHT":
        x += 1

    else:
        logging.error(f"Invalid command: {command}")
        print("Invalid command!")
        continue

    move_counter += 1

    print(f"Current position: ({x}, {y})")
    logging.debug(f"Robot moved to ({x}, {y})")

    # Check if robot left the maze
    if x < MIN or x > MAX or y < MIN or y > MAX:
        logging.warning(f"Robot left the maze at ({x}, {y})")
        print("You Lost, GAME OVER")
        logging.info("Game ended.")
        break

    # Check if robot found the treasure
    if x == TREASURE_X and y == TREASURE_Y:
        logging.info(f"Robot reached the treasure at ({x}, {y})")
        logging.info(f"Game finished after {move_counter} moves.")
        print("🎉 You found the treasure!")
        logging.info("Game ended.")
        break
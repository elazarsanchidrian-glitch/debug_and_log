import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,   # DEBUG is needed so debug messages are saved
)

def divide(num1, num2):
    logging.info("Division started")
    logging.debug(f"Numbers entered: {num1}, {num2}")

    if num2 == 0:
        logging.error("Cannot divide by zero")
        return None

    result = num1 / num2
    logging.info(f"Final answer: {result}")
    return result


# Test the function
print(divide(10, 2))
print(divide(8, 0))
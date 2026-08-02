import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
)

logging.info("Program started")
logging.warning("This is a warning")
logging.error("Something went wrong")
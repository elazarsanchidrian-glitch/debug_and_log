import logging

logging.basicConfig(
    filename="grade_analyzer.log",
    level=logging.DEBUG,
)

def grade_analyzer(grades):
    logging.info("Processing grades started")

    total = 0
    count = 0

    for grade in grades:
        logging.debug(f"Checking grade: {grade}")

        if grade < 0 or grade > 100:
            logging.error(f"Invalid grade: {grade}")

        elif grade < 60:
            logging.warning(f"Failing grade: {grade}")

        total += grade
        count += 1

    average = total / count
    logging.info(f"Average grade: {average}")


# Test the function
grades = [85, 92, 41, 100, -5]
grade_analyzer(grades)
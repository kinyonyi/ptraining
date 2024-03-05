import logging
#used for logging applications
logging.basicConfig(filename="log.txt", filemode="a", level=0)

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))

try:
    output = num1 / num2
    print(output)
    print(logging.info("Division successfull!"))
except ZeroDivisionError as e:
    logging.error(e)

logging.exception("exception")
logging.debug("debug")
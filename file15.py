#Exception Handling
import logging
import datetime
logging.basicConfig(filename="log.txt", filemode="a", level=0)

try:
    result = 5 / 0
except ZeroDivisionError as e:
    dateEvent = datetime.datetime.today()
    #Executes if the try was unsuccessfull
    logging.error(f"Error {e} happend at {dateEvent}")
else:
    #Executes if the try was successfull
    dateEvent = datetime.datetime.today()
    logging.info(f"The result of division is \
        {result} happend at {dateEvent}")
finally:
    #Always executes
    logging.info("End of division")

#try except minus else and finally
try:
    result = 5 / 0
except ZeroDivisionError as e:
    #Executes if the try was unsuccessfull
    print(f"Error {e}")
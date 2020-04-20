import logging

# debug, info, warning, error, critical
# info =>  working as normal
# default log level is warning.

# log level is set to DEBUG now so everything from debug above will be logged
# # to the file mentioned
# logging.basicConfig(filename='test.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(levelname)s:%(message)s')


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
FILE_HANDLER = logging.FileHandler('calculator.log')
FILE_HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(FILE_HANDLER)


def add(int_x, int_y):
    return int_x + int_y


def subtract(int_x, int_y):
    return int_x - int_y


def multiply(int_x, int_y):
    return int_x * int_y


def divide(int_x, int_y):
    return int_x / int_y


num_1 = 90
num_2 = 7
num_3 = 9
num_4 = 10
num_5 = 2
num_6 = 11

add_restult = add(num_1, num_2)
LOGGER.debug(f'Add: {num_1} + {num_2} = {add_restult}')

subtract_result = subtract(num_3, num_6)
LOGGER.debug(f'subtract: {num_3} - {num_6} = {subtract_result}')

multiply_restult = multiply(num_1, num_3)
LOGGER.debug(f'multiply: {num_1} * {num_3} = {multiply_restult}')

divide_restult = divide(num_4, num_5)
LOGGER.debug(f'divide: {num_4} / {num_5} = {divide_restult}')

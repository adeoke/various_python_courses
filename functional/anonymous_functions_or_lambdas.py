import time
import sys


# Lambdas will follow the format that you write lambda followed by the input
# Then colon and the body of the expression

# so the function hello function which takes a single input
def hello(name):
    return f'hello {name}'


# becomes
expression = lambda name: f'hello {name}'
print(expression('Adam'))

expression_print = lambda name: print(f'hello {name}!')

first_name_var = '      John   '
last_name_var = '  Doe   '


# multiple arg method
def full_name(first_name, last_name):
    return f'{first_name.strip()} {last_name.strip()}'


print(full_name(first_name_var, last_name_var))

# lambda version of multiple arg method
full_name_lambda = lambda first_name, \
                          last_name: f'{first_name.strip()} {last_name.strip()}'

print(full_name_lambda(first_name_var, last_name_var))

result = full_name_lambda(first_name_var, last_name_var) == \
         full_name(first_name_var, last_name_var)

print(result)

# lambdas have to be single expressions, CANNOT need muliple lines

list_of_names = ['Steve', 'Jill', 'Jack', 'Mark', 'Zack']
list_of_names.sort()
print(list_of_names)


def sort_name(list_names):
    list_names.sort()
    return list_names


print(sort_name(list_of_names))


# passing lambdas as arguments to methods/functions

def wait_then_say_hello(seconds, func):
    time.sleep(seconds)
    condition = callable(func) or False
    print(condition)
    func()


wait_then_say_hello(5, lambda: expression_print('Adam'))


# in the following case the method hello('Adam') will not work as an arg
# wait_then_say_hello(5, hello('Adam'))


# List comprehension
def multiply_comprehension(li):
    return [item * 2 for item in li]


print(multiply_comprehension([1, 2, 3, 4]))

LIST_0F_NUMBERS = [1, 2, 3, 4, 5, 6, 7]


# Map function

def multiply_by_2(number):
    """ multiply number param by 2 """
    return number * 2


print(list(map(multiply_by_2, LIST_0F_NUMBERS)))


# filter function

def only_odd(number):
    """return number that is odd"""
    return number % 2 != 0


print(list(filter(only_odd, LIST_0F_NUMBERS)))

first_names = ['Michael', 'Curtis', 'Jim', 'Tom', 'Idris']
last_names = ['Jordan', 'Jackson', 'Carey', 'Hanks', 'Elba']
last_names_tuple = ('Jordan', 'Jackson', 'Carey', 'Hanks', 'Elba')

print(list(zip(first_names, last_names)))
print(list(zip(first_names, last_names_tuple)))


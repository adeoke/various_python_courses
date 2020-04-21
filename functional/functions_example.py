import time


# remember that functions separate behaviour and data
# they have no affect on the outside world


def pure_function(data):
    new_list = []
    for item in data:
        new_list.append(item * 2)
    return new_list


the_list = [1, 2, 3]

print(pure_function(the_list))


# passing a function as an argument
# also this is not a pure function
def wait_then_execute(seconds, function):
    time.sleep(seconds)
    function()


# note that this is not a pure function as it involves the print keyword
def hello():
    print('Hello World')


# store the function in a variable
hello_func = hello

# check if the hello function variable is callable, if True then it is a func
callable(hello_func) == True

wait_then_execute(5, hello_func)

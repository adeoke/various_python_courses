def decorate_me(func):
    def inner_decor(*args, **kwargs):
        print("I'll be decorating")
        print('function name', func.__name__)
        print('function args', *args)
        print('function keyword args', **kwargs)
        result = func(*args, **kwargs)
        print('Result is: ', result)
        return result

    return inner_decor


@decorate_me
def multiply(int_x, int_y):
    return int_x * int_y


print(multiply(3,5))


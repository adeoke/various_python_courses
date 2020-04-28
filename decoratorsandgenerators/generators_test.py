class NumberTooLargeException(Exception):
    pass


the_range = range(1, 30, 1)

for item in the_range:
    print(item)

print('\n\n')


def custom_range(num):
    if num >= 100:
        raise NumberTooLargeException('Number is too large')

    print('value of number is: ', num)
    while num < 100:
        yield num
        num += 5


for num in custom_range(130):
    print(num)

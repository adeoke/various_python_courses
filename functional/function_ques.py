from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def cap_names(input):
    return input.capitalize()


print(list(map(cap_names, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def greater_than_50(item):
    return item > 50


print(list(filter(greater_than_50, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def adder(int_x, int_y):
    return int_x + int_y


print(reduce(adder, scores + my_numbers))
EXPECTED_TOTAL = 456

print(reduce(adder, scores + my_numbers) == EXPECTED_TOTAL)


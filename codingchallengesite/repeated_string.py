import math
import os
import random
import re
import sys


def repeated_strings(s, n):
    found_a_times = 0
    surplus_size = math.ceil(n / len(s))
    expanded_str = surplus_size * s
    list_of_chars = list(expanded_str)
    chars_width = list_of_chars[0:n]

    for char in chars_width:
        if char == 'a':
            print(char)
            found_a_times += 1

    return found_a_times


# string = 'abcac'
# letters = 10
# repeated_strings(string, letters)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeated_strings(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

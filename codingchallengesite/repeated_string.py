import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeated_strings(s, n):
    found_a_times = 0
    additional_finds = 0

    for char in s:
        if char == 'a':
            found_a_times += 1

    repititions_of_str = n // len(s)
    print('repetitions of str: ', repititions_of_str)
    no_remainder_total = repititions_of_str * found_a_times
    remainder = n % len(s)
    print('surplus', remainder)
    if remainder > 0:
        for letter in list(s)[:remainder]:
            if letter == 'a':
                print('theres extra of remainder:', remainder)
                additional_finds += 1

    return no_remainder_total + additional_finds


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeated_strings(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

import math
import os
import random
import re
import sys


def find_pairs(li, ar):
    pairs = 0
    asso_arr = {}
    res = list(set(ar))

    for item in res:
        count = ar.count(item)
        asso_arr[item] = count

    print(asso_arr)

    for value in asso_arr.values():
        pairs += int(value / 2)
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = find_pairs(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

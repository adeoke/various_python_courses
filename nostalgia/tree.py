"""
in the first class of my first year in computer science, this is the first thing
I did (but I did it in Java not Python).

"""


def print_tree(li):
    start_index = 0
    for item in range(start_index, len(li)):
        print((item + 1) * '*')


li = [1, 2, 3, 4, 5, 6, 7, 8]
print_tree(li)

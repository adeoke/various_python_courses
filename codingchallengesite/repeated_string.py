import math


def repeated_strings(s, n):
    found_a_times = 0
    surplus_size = math.ceil(n / len(s))
    expanded_str = surplus_size * s
    list_of_chars = list(expanded_str)
    chars_width = list_of_chars[0:n]
    print(chars_width)

    for char in chars_width:
        if char == 'a':
            print(char)
            found_a_times += 1

    print(found_a_times)


string = 'abcac'
letters = 10
repeated_strings(string, letters)

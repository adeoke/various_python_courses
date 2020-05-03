"""
Thought I'd give this one a go as its commonly asked in American style
interviews.
Given characters a through to z, if the letter a represents 1, and the letter
b 2, and so on to the letter z at 26. The given an input, for example 12,
list the word letters that this sequence represents.
In the case that 12 is inputted then we see:
"ab" and
"l"

as the results.
Lets write the algorithm.

"""


def morse_code(sequence):
    print(ord('a'))
    print(ord('z'))

    chars_range = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    new_dict = {value: char for char, value in enumerate(chars_range, 1)}



morse_code('')

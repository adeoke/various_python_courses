import sys

DICTIONARY = {'zero': '0',
              'one': '1',
              'two': '2',
              'three': '3',
              'four': '4',
              'five': '5',
              'six': '6',
              'seven': '7',
              'eight': '8',
              'nine': '9'
              }


def convert(s):
    try:
        number = ''
        for token in s:
            number += DICTIONARY[token]
        return int(number)
    except (KeyError, TypeError) as ex:
        print(f'Conversion error: {ex!r}', file=sys.stderr)
        return -1


numbers_list = ['five', 'six', 'seven']

print(convert(numbers_list))

print(convert(['this', 'should', 'fail']))

print(convert(512))
print(convert('512'))

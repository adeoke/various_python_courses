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
    int_x = -1

    try:
        number = ''
        for token in s:
            number += DICTIONARY[token]
        int_x = int(number)
        print(f'Conversion success x = {int_x}')
    except (KeyError, TypeError):
        print('conversion failed')
    return int_x


numbers_list = ['five', 'six', 'seven']

print(convert(numbers_list))

print(convert(['this', 'should', 'fail']))

print(convert(512))
print(convert('512'))

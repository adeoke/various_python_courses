"""
In this module we will attempt to find the second smallest number in an
unsorted array
"""
import sys


class NumberQuiz:
    """class usd to solve the second smallest number problem"""

    def __init__(self):
        self.lowest_val = sys.maxsize
        self.second_lowest_val = sys.maxsize

    def second_smallest_value_in_list(self, li):
        for value in li:
            if value < self.lowest_val:
                self.second_lowest_val = self.lowest_val
                self.lowest_val = value

        print('Lowest val is: ', self.lowest_val)
        print('second lowest is: ', self.second_lowest_val)
        return self.second_lowest_val


num = NumberQuiz()
li_numbers = [23, 8, 9, 0, 12, -1, -1, -3, -5, -5]
result = num.second_smallest_value_in_list(li_numbers)
print(result)

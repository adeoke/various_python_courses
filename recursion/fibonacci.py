"""This module will attempt to solve simple algorithms"""
from functools import lru_cache


class Algo:
    """algorithms class"""

    def __init__(self):
        self.first_term = 1
        self.second_term = 1

    def fibonacci_to_nth_term(self, nth_term):
        """This method returns the value of the nth term in fibonacci"""
        self.first_term = 1
        self.second_term = 1
        terms = [self.first_term, self.second_term]
        list_index = nth_term - 1
        if list_index < 2:
            print('value of nth term is: ', nth_term)
            return terms[list_index]

        count = 2
        while count < nth_term:
            print('this is terms list: ', terms)
            terms.append(terms[-2] + terms[-1])
            count += 1

        return terms[-1]

    # recursive implementation
    @lru_cache(1000)
    def fibonacci(self, nth_term):
        """recursive fibonacci example"""
        if nth_term in (1, 2):
            return 1

        return self.fibonacci(nth_term - 1) + self.fibonacci(nth_term - 2)


algo = Algo()
print(algo.fibonacci_to_nth_term(1))
print(algo.fibonacci_to_nth_term(2))
# print(algo.fibonacci_to_nth_term(3))
# print(algo.fibonacci_to_nth_term(4))
# print(algo.fibonacci_to_nth_term(5))
# print(algo.fibonacci_to_nth_term(6))
# print(algo.fibonacci_to_nth_term(33))
print(algo.fibonacci(1))
print(algo.fibonacci(2))
print(algo.fibonacci(3))
print(algo.fibonacci(4))
print(algo.fibonacci(5))
print(algo.fibonacci(6))

# fn = (fn-1) + (fn-2)
# where n > 2

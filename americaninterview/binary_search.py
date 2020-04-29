"""
In this module we will attempt to perform binary search on a given list
Note that this traditionally requires a sorted list, so the first thing that
will take place within the solution is to sort the list using python's built in
functions for sorting a list.
"""


class BinarySearch:
    """Binary search class"""

    def find_number_in_list(self, li, number, start_index=None,
                            end_index=None):
        """method could be static, but im not doign that."""
        sorted_list = sorted(li)

        if start_index is None and end_index is None:
            print('should happen once')
            start_index = 0
            end_index = len(sorted_list) - 1

        # problem mid point is not changing
        print('end index is: ', end_index)
        print('start index is: ', start_index)
        mid_point = start_index + ((end_index - start_index) // 2)

        first_half_list = sorted_list[:mid_point]
        last_half_list = sorted_list[(mid_point + 1):]

        print('current list is: ', sorted_list)
        print('mid point is: ', mid_point)
        print('mid point value is: ', sorted_list[mid_point])
        print('first part of list is: ', first_half_list)
        print('last part of list is: ', last_half_list)

        if start_index > end_index:
            print('not found')
            return False

        if number == sorted_list[mid_point]:
            print('found number at index position ', mid_point)
            return mid_point
        elif number < sorted_list[mid_point]:
            print(
                'number is lower than the largest number in the last element in the first list')
            print('end index needs to be altered to last index in this half')
            end_index = mid_point - 1
            self.find_number_in_list(sorted_list, number,
                                     start_index, end_index)
        elif number > sorted_list[mid_point]:
            print(
                'required number is greater than the first number in this half',
                number, last_half_list[0])
            print('changing the starting index for this case')
            print(
                'as zero based index, mid point is the initial index for this half')
            start_index = mid_point + 1
            self.find_number_in_list(sorted_list, number,
                                     start_index, end_index)


li = [32, 234, 1, 67, 90, 2, 15]

binary_search = BinarySearch()
binary_search.find_number_in_list(li, 30)

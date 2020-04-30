"""
in this module we shall address a common interview question about non
repeating integers in a collection
"""


def non_repeating(li):
    start_index = 0

    for index in range(start_index, len(li)):
        count = 0
        for inner_index in range(start_index, len(li)):
            # if index != inner_index and li[index] is li[inner_index]:
            #     pass
            # print(f'matched {li[index]} at position {index} with {li[inner_index]} at position {inner_index}')
            if index != inner_index and li[index] != li[inner_index]:
                count += 1
                if count is (len(li) - 1):
                    return li[index]


li = [2, 19, 24, 36, 47, 24, 19]

print(non_repeating(li))

"""
in this module we shall aim to address swapping the positive and negative elements
in a list so that the negative elments appear firs then the positive ones. No order is
required
"""


def rearrange_pos_neg_numbers_in_list(li):
    start_index = 0

    for index in range(start_index, len(li)):
        if li[index] > 0:
            for inner_index in reversed(range(start_index + 1, len(li))):
                if li[inner_index] < 0:
                    li[index], li[inner_index] = li[inner_index], li[index]
                if inner_index == index:
                    break

    return li


li = [-21, 9, -1, 2, -3, 13, -4, -17, 12]

print(rearrange_pos_neg_numbers_in_list(li))

# Binary Search
# number we are after

goal = 72
not_in_list = 92

# un ordered list
list_numbers = [90, 20, 30, 14, 21, 72, 27]

# step 1 sort to ordered list

sorted_list = sorted(list_numbers)

# find the mid point

mid_point = len(sorted_list) // 2
print(mid_point)
print(sorted_list[:mid_point])
print(sorted_list[mid_point:])

# is the number equal to the mid point?
# if not is the number greater than the last number in the first half
# if the desired number is greater than the mid number ignore left list, split right list in half
# else do opposite



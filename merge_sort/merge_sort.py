"""
Python insertion sort implementation
20210922
ProjectFullStack
"""

import random


def merge_lists(left, right):
    """
    O(n+m) where n = the size of left, and m = the size of right
    Note: we do not want to modify the left or right lists! We will create
    a new empty list and use that.
    :param left:
    :type left:
    :param right:
    :type right:
    :return:
    :rtype:
    """
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j] :
            # the value in the left is greater than the value in right
            # append the value in the left to the return array
            # and increment i
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            # the value in the right is greater than the value in left
            # append the value in the right to the return array
            # and increment j
            result.append(right[j])
            j += 1

    # once we get here, we have reached the end of one our lists
    # there are still elements remaining in the other list
    # so we need to check the lists and if they are not exhausted
    # then copy the remaining elements, in order, to the result array
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(the_list):
    """
    Sorts a list using recursive merge sort
    :param the_list:
    :type the_list:
    :return:
    :rtype:
    """
    if len(the_list) <= 1:
        return the_list
    list_divider_index = len(the_list) // 2
    left_list = merge_sort(the_list[:list_divider_index])
    right_list = merge_sort(the_list[list_divider_index:])
    return merge_lists(left_list, right_list)


# Test Case 1, list of 8 elements
unsorted = [17, 12, 37, 19, 20, 4, 15, 2]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = merge_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 2, list of 5 elements, include negative numbers
unsorted = [-5, -100, 3245, 10, 2532]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = merge_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 3, list of 0 elements
unsorted = []
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = merge_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 4, random list of 20 elements
unsorted = random.sample(range(0, 100), 20)
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = merge_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

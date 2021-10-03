"""
Python merge sort implementation
20210922
ProjectFullStack
"""

import random


def merge_lists(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

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


# Test Case 1, list of 8 unique elements
unsorted = [17, 12, 37, 19, 20, 4, 15, 2]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = merge_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 2, list of 8 elements with duplicate values
unsorted = [17, 12, 37, 12, 20, 4, 15, 2]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = merge_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 3, list of 5 elements, include negative numbers
unsorted = [-5, -100, 3245, 10, 2532]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = merge_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 4, list of 0 elements
unsorted = []
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = merge_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 5, random list of 20 elements
unsorted = random.sample(range(0, 100), 20)
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = merge_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

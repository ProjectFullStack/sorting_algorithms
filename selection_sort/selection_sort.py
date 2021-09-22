"""
Python selection sort implementation
20210919
ProjectFullStack
"""

import random


def swap(the_list, index_left, index_right):
    """
    Given a list, swaps the values at the two indices
    :param the_list: the list
    :type the_list: list
    :param index_left: the left index to swap
    :type index_left: int
    :param index_right: the right index to swap
    :type index_right: int
    """
    temp_placeholder = the_list[index_right]
    the_list[index_right] = the_list[index_left]
    the_list[index_left] = temp_placeholder


def selection_sort(the_list):
    """
    Sorts an unsorted list using selection sort algorithm
    Time Complexity: n = length of unsorted list
        Best Case: O(n^2)
        Average Case: O(n^2)
        Worst Case: O(n^2)
    Space Complexity:
        O(1)
    :param the_list: the unsorted list
    :type the_list: list
    :return: a sorted list
    :rtype: list
    """
    for i in range(len(the_list)):
        # set the minimum index to by the first unsorted element
        minimum_index = i

        # start searching from i + 1, until the end of the list
        # unlike bubble sort, we want to include the last element in
        # the list in the inner loop
        for j in range(i + 1, len(the_list)):
            # if the value at j is less than the value at minimum_index
            if the_list[j] < the_list[minimum_index]:
                # set the minimum index to be j
                minimum_index = j

        # now swap the minimum index and the i index, only if they are
        # different
        if minimum_index != i:
            swap(the_list, i, minimum_index)

    return the_list


# Test Case 1, list of 8 elements
unsorted = [17, 12, 37, 19, 20]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = selection_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 2, list of 5 elements, include negative numbers
unsorted = [-5, -100, 3245, 10, 2532]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = selection_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 3, list of 0 elements
unsorted = []
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = selection_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 4, random list of 20 elements
unsorted = random.sample(range(0, 100), 20)
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = selection_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

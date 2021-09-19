"""
Python bubble sort implementation
2020919
ProjectFullStack
"""

import random


def swap(the_list, index_left, index_right):
    """
    Swaps elements index_left and index_right in the the_list
    :param the_list: the list
    :type the_list: list
    :param index_left: the left index
    :type index_left: int
    :param index_right: the right index
    :type index_right: int
    :return: None
    :rtype: None
    """
    temp_placeholder = the_list[index_right]
    the_list[index_right] = the_list[index_left]
    the_list[index_left] = temp_placeholder


def simple_bubble_sort(the_list):
    """
    Sorts an unsorted list using bubble sort algorithm
    Time Complexity: n = length of unsorted list
        Best Case: O(n^2)
            - for this unoptimized solution, see the better_bubble_sort
              implementation for an O(n) best case
        Average Case: O(n^2)
        Worst Case: O(n^2)
    Space Complexity:
        O(1)
    :param the_list: the unsorted list
    :type the_list: list
    :return: a sorted list
    :rtype: list
    """
    # outer loop, for every element in unsorted list
    for i in range(len(the_list)):
        # inner loop, for every element up to, but NOT including,
        # the last element of the list
        for j in range(len(the_list) - 1):
            # for each element, check the current element against the next
            # element in the list, swap if the left element is greater than
            # than the right element
            if the_list[j] > the_list[j+1]:
                # call swap
                swap(the_list, j, j+1)
    # the list should be sorted by here, return it
    return the_list


# Test Case 1, list of 5 elements
unsorted_list = [17, 12, 37, 19, 20]
sorted_list = simple_bubble_sort(list(unsorted_list))
print(f"{unsorted_list} -> {sorted_list}")

# Test Case 2, list of 5 elements, include negative numbers
unsorted_list = [-5, -100, 3245, 10, 2532]
sorted_list = simple_bubble_sort(list(unsorted_list))
print(f"{unsorted_list} -> {sorted_list}")

# Test Case 3, list of 0 elements
unsorted_list = []
sorted_list = simple_bubble_sort(list(unsorted_list))
print(f"{unsorted_list} -> {sorted_list}")


def better_bubble_sort(the_list):
    """
    Sorts an unsorted list using bubble sort algorithm
    Includes
    Time Complexity: n = length of unsorted list
        Best Case: O(n)
        Average Case: O(n^2)
        Worst Case: O(n^2)
    Space Complexity:
        O(1)
    :param the_list: the unsorted list
    :type the_list: list
    :return: a sorted list
    :rtype: list
    """
    # create a variable did_swap, this will track if we performed any
    # swaps in our passes. If we did not perform any swaps, we know we have
    # a sorted list
    did_swap = False

    for i in range(len(the_list)):
        did_swap = False
        # the other change is here: len(the_list) - i - 1
        # because we know that everytime we go through the outer loop the
        # largest number "bubbles up" to the end of the list. So for each
        # outer loop iteration we can look at one less element than before.
        for j in range(len(the_list) - i - 1):
            if the_list[j] > the_list[j + 1]:
                did_swap = True
                swap(the_list, j, j + 1)

        if not did_swap:
            # no swaps occurred, this list must be sorted, no need to continue
            # with any other iterations
            break

    # the list should be sorted by here, return it
    return the_list


print("------- testing better_bubble_sort -------")
# Test Case 1, list of 5 elements
unsorted_list = [17, 12, 37, 19, 20]
sorted_list = better_bubble_sort(list(unsorted_list))
print(f"{unsorted_list} -> {sorted_list}")

print("------- testing better_bubble_sort -------")
# Test Case 2, list of 10 elements randomly generated
unsorted_list = random.sample(range(0, 100), 10)
sorted_list = better_bubble_sort(list(unsorted_list))
print(f"{unsorted_list} -> {sorted_list}")

"""
Python insertion sort implementation
20210920
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


def insertion_sort(the_list):
    """
    Sorts an unsorted list using insertion sort algorithm
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
    # outer loop, we start at index 1 because we always assume the
    # FIRST element in the_list is sorted. That is the basis of how
    # insertion sort works
    for i in range(1, len(the_list)):
        # "pull out" or store the value we are trying to insert
        insert_value = the_list[i]

        # inner WHILE loop, start at the last sorted index ( which is at j - 1)
        # and count DOWN check each value we find at j against the
        # value we are trying to insert
        j = i - 1
        while j >= 0 and the_list[j] > insert_value:
            # "move" the value we find a j to the right, which is the index
            # j + 1
            the_list[j + 1] = the_list[j]
            # decrement J, otherwise we will never break out of while loop!
            j -= 1
        # finally, when we get here j should be the first card that is
        # less than the insert value, so insert value needs to go
        # one to the right of j, or at index j + 1
        the_list[j+1] = insert_value

    # return the sorted list
    return the_list


# Test Case 1, list of 5 elements
unsorted_list = [17, 12, 37, 19, 20]
sorted_list = insertion_sort(list(unsorted_list))
print(f"{unsorted_list} -> {sorted_list}")

# Test Case 2, list of 5 elements, include negative numbers
unsorted_list = [-5, -100, 3245, 10, 2532]
sorted_list = insertion_sort(list(unsorted_list))
print(f"{unsorted_list} -> {sorted_list}")

# Test Case 3, list of 0 elements
unsorted_list = []
sorted_list = insertion_sort(list(unsorted_list))
print(f"{unsorted_list} -> {sorted_list}")

# Test Case 4, random list of 20 elements
unsorted_list = random.sample(range(0, 100), 20)
sorted_list = insertion_sort(list(unsorted_list))
print(f"{unsorted_list} -> {sorted_list}")


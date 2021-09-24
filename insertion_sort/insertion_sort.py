"""
Python insertion sort implementation
20210920
ProjectFullStack
"""

import random


def insertion_sort(the_list):
    # outer loop, we start at index 1 because we always assume the
    # FIRST element in the_list is sorted. That is the basis of how
    # insertion sort works
    for i in range(1, len(the_list)):
        # "pull out" or store the value we are trying to insert
        insert_value = the_list[i]

        # inner WHILE loop, start at the last sorted index ( which is at i - 1)
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


# Test Case 1, list of 6 elements
unsorted = [17, 12, 37, 19, 20]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = insertion_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 2, list of 5 elements with duplicate values
unsorted = [17, 12, 12, 19, 20]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = insertion_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 3, list of 5 elements, include negative numbers
unsorted = [-5, -100, 3245, 10, 2532]
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = insertion_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 4, list of 0 elements
unsorted = []
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = insertion_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")

# Test Case 5, random list of 20 elements
unsorted = random.sample(range(0, 100), 20)
python_sorted = list(unsorted)
python_sorted.sort()
our_sorted = insertion_sort(list(unsorted))
print(f"Passed: {python_sorted == our_sorted} : {unsorted} -> {our_sorted}")


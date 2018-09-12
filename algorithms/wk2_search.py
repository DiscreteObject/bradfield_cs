# -*- coding: utf-8 -*-
"""
Bradfield CS: Problem Solving with Algorithms and Data Structures
Fall 2018
Week 2
Taylor Hudson
@DiscreteObject

Prompt:
Binary search for a sorted array of integers
"""

def binary_search(array, search_value):
    start = 0
    end = len(array) - 1
    mid = end // 2

    count = 0

    if search_value < array[start] or search_value > array[end]:
        # out of bounds
        return None

    while True:
        count += 1
        mid = start + ((end - start) // 2)
        if array[mid] == search_value:
            return mid
        elif array[start] == search_value:
            return start
        elif array[end] == search_value:
            return end

        if start == mid or mid == end:
            # search_value is not present
            return None

        if array[start] < search_value and search_value < array[mid]:
            # in lower half
            end = start + ((end - start) // 2)
        elif array[mid] < search_value and search_value < array[end]:
            # in upper half
            start = mid


def main():
    array = [1,3,6,9,10,15,19,25,31,32,33,40,45]
   
    for n in array:
        print(binary_search(array, n)) # should print 0..len(array) - 1


if __name__ == '__main__':
    main()

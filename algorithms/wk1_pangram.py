# -*- coding: utf-8 -*-
"""
Bradfield CS: Problem Solving with Algorithms and Data Structures
Fall 2018
Week 1
Taylor Hudson
@DiscreteObject
"""

import time
from collections import defaultdict

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def is_pangram_1(string):
    # A pangram must contain every letter in the alphabet at least once
    # Count the number of occurances of each letter and see if any are 0
    # Time: n + 26 iterations = O(n)
    # Space: Creation of 26-entry dictionary = O(1)

    letters_dict = defaultdict(int)
    for letter in string:
        letters_dict[letter] += 1

    for letter in ALPHABET:
        if letters_dict[letter] == 0:
            return False
    return True

def is_pangram_2(string):
    # Add each letter in string to a set
    # See if the total length of the set is length of the alphabet
    # Time: O(n)
    # Space: Creation of up-to-26-entry set = O(1)

    letters = set()
    for letter in string:
        if letter != ' ':
            letters.add(letter)

    return len(letters) == len(ALPHABET)

def is_pangram_3(string):
    # Iterate through the alphabet, for each letter, see if present
    # in string. If any not, return.
    # Time: 26 * n = O(n)
    # Space: O(1)

    for letter in ALPHABET:
        if letter not in string:
            return False

    return True


def main():
    output_template = '{}("{}") = {} ({:8.7f} seconds)'
    test_string = 'the quick brown fox jumps over the lazy dog'

    start = time.time()
    result = is_pangram_1(test_string)
    end = time.time()
    print(output_template.format('is_pangram_1', test_string, result, end - start))

    start = time.time()
    result = is_pangram_2(test_string)
    end = time.time()
    print(output_template.format('is_pangram_2', test_string, result, end - start))

    start = time.time()
    result = is_pangram_3(test_string)
    end = time.time()
    print(output_template.format('is_pangram_3', test_string, result, end - start))

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""
Bradfield CS: Problem Solving with Algorithms and Data Structures
Fall 2018
Week 1
Taylor Hudson
@DiscreteObject

Prompt:
Write a function that uses a stack (you can use the stack implementation
in /algos) to return a reversed copy of a list.
"""


class Stack(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


def reverse_list(l):
    stack = Stack()
    for item in l:
        stack.push(item)

    reversed_list = []

    while not stack.is_empty():
        reversed_list.append(stack.pop())

    return reversed_list


def main():
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(reverse_list(list1))


if __name__ == '__main__':
    main()

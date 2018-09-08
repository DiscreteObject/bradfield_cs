# -*- coding: utf-8 -*-
"""
Bradfield CS: Problem Solving with Algorithms and Data Structures
Fall 2018
Week 1
Taylor Hudson
@DiscreteObject

Prompt:
Implement a queue using stacks. Your solution should have the same
interface as the queue implementation in algos, but use stacks instead
of a list in the implementation.
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

    def __repr__(self):
        return str(self._items)


class Queue(object):
    def __init__(self):
        self._items = Stack()

    def is_empty(self):
        return self._items.is_empty()

    def enqueue(self, item):
        self._items.push(item)

    def dequeue(self):
        # Construct stack in reverse order
        if self._items.is_empty():
            return None

        reversed_stack = Stack()
        while not self._items.is_empty():
            reversed_stack.push(self._items.pop())
        item_to_dequeue = reversed_stack.pop()

        # Reconstruct original without dequeued item
        while not reversed_stack.is_empty():
            self._items.push(reversed_stack.pop())

        return item_to_dequeue

    def size(self):
        return self._items.size()

    def __repr__(self):
        return self._items.__repr__()


def main():
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    queue.enqueue('e')

    print(queue.dequeue()) # 'a'
    print(queue.dequeue()) # 'b'
    print(queue.dequeue()) # 'c'
    print(queue.dequeue()) # 'd'
    print(queue.dequeue()) # 'e'

    print("-- Queue is empty now")
    print(queue.dequeue()) # None


if __name__ == '__main__':
    main()

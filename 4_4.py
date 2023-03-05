from collections import deque


class Stack(object):
    def __init__(self, size):
        self.__deque = deque(size)

    def push(self, item):
        self.__deque.insertRight(item)

    def pop(self):
        return self.__deque.removeRight()

    def peek(self):
        return self.__deque.peekRight()

    def isEmpty(self):
        return self.__deque.isEmpty()

    def isFull(self):
        return self.__deque.isFull()

    def __len__(self):
        return len(self.__deque)

    def __str__(self):
        return str(self.__deque)
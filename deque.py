class Deque:
    def __init__(self, size):
        self.__dequeList = [None] * size
        self.__size = size
        self.__front = 0
        self.__rear = 1

    def insertLeft(self, item):
        if self.isFull():
            raise Exception('Deque overflow')
        else:
            self.__dequeList[self.__front] = item
            self.__front = (self.__front - 1) % self.__size

    def insertRight(self, item):
        if self.isFull():
            raise Exception('Deque overflow')
        else:
            self.__dequeList[self.__rear] = item
            self.__rear = (self.__rear + 1) % self.__size

    def removeLeft(self):
        if self.isEmpty():
            raise Exception('Deque underflow')
        else:
            self.__front = (self.__front + 1) % self.__size
            return self.__dequeList[self.__front]

    def removeRight(self):
        if self.isEmpty():
            raise Exception('Deque underflow')
        else:
            self.__rear = (self.__rear - 1) % self.__size
            return self.__dequeList[self.__rear]

    def peekLeft(self):
        if self.isEmpty():
            return None
        else:
            return self.__dequeList[(self.__front + 1) % self.__size]

    def peekRight(self):
        if self.isEmpty():
            return None
        else:
            return self.__dequeList[(self.__rear - 1) % self.__size]

    def isEmpty(self):
        return (self.__front + 1) % self.__size == self.__rear

    def isFull(self):
        return self.__front == self.__rear % self.__size

    def __str__(self):
        if self.isEmpty():
            return '[]'
        else:
            result = '['
            index = (self.__front + 1) % self.__size
            while index != self.__rear:
                if index != (self.__front + 1) % self.__size:
                    result += ', '
                result += str(self.__dequeList[index])
                index = (index + 1) % self.__size
            result += ']'
            return result


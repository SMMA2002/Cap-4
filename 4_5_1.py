class PriorityQueue(object):
    def __init__(self):
        self.__queue = []  # Queue stored as a list
    
    def insert(self, item):
        self.__queue.append(item)  # Insert item at the end of the queue
        return True
    
    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        max_item = self.__queue[0]
        max_index = 0
        for i in range(1, len(self.__queue)):
            if self.__queue[i] > max_item:  # Compare items using '>' operator
                max_item = self.__queue[i]
                max_index = i
        del self.__queue[max_index]  # Remove item with highest priority
        return max_item
    
    def peek(self):
        return None if self.isEmpty() else max(self.__queue)
        
    def isEmpty(self):
        return len(self.__queue) == 0
    
    def __len__(self):
        return len(self.__queue)

    def __str__(self):
        return "[" + ", ".join(str(item) for item in self.__queue) + "]"

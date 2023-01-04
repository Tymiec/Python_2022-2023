import random

class RandomQueue:
    def __init__(self):
        self.size = 15
        self.count = 0
        self.queue = []
        
    def insert(self, element):
        if self.is_full():
            raise ValueError("Queue is full")

        self.queue.append(element)

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        ID = random.randint(0, len(self.queue) - 1)

        self.queue[ID], self.queue[-1] = self.queue[-1], self.queue[ID]
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def clear(self):
        self.queue = []
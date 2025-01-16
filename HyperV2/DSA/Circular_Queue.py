class Queue:
    def __init__(self, size):
        self.array = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size


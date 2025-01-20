class Queue:
    def __init__(self,size):
        self.size = size
        self.array = [None] * size
        self.front = 0
        self.rear = 0


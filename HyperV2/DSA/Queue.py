class Queue:
    def __init__(self,size):
        self.size = size
        self.array = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self,val):
        if self.rear < self.size:
            self.array[self.rear] = val
            self.rear += 1
        else:
            print("Queue is full")
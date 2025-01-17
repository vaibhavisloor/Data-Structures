class Queue:
    def __init__(self, size):
        self.array = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

        def enqueue(self, val):
            if (self.rear + 1) % self.size == self.front:  
                print("Queue is full")
            else:
                self.rear = (self.rear + 1) % self.size  
                self.array[self.rear] = val
                print(f"The value {val} has been appended")

                if self.front == -1:
                    self.front = 0
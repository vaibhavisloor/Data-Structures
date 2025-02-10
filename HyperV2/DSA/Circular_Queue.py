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

    def deque(self):
        if self.front == self.rear: 
            print("Queue is empty")
        else:
            print(f"The value {self.array[self.front]} is dequeued")
            self.array[self.front] = None
            self.front = (self.front + 1) % self.size

if __name__ == "__main__":
    q = Queue(5)  
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    print(q.array) 
    q.deque()
    q.deque()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    # q.deque()
    # q.enqueue(10)
    print(q.array) 
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
    
    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            print(f"The value {self.array[self.front]} is dequeued")
            self.array[self.front] = None
            self.front += 1
if __name__ == "__main__":
    q=Queue(5)
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    q.enqueue(1)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
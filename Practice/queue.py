front = 0
rear = 0
size = 5
queue = [None] * size

def enqueue(val):
    global rear
    if rear < size:
        queue[rear] = val
        rear+=1
        print(f"Value of {val} added to queue.")
    else:
        print("Queue is full")

def dequeue():
    global front,rear
    if front == rear:
        print("Queue is empty")
    else:
        val = queue[front]
        queue[front] = None
        front+=1
        print(f"Value of {val} has been dequeued")


dequeue()

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)
enqueue(60)

dequeue()
dequeue()
dequeue()
dequeue()
dequeue()

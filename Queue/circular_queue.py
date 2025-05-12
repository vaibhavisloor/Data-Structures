size = 5

front = rear = -1

queue = [None]*size

def enqueue(val):
    global rear,front
    if (rear+1)%size == front:
        print("Queue is full")
        return
    if front == -1:
        front = 0
    rear = (rear+1)%size  
    queue[rear] = val
    print(f"{val} has been added")

def dequeue():
    global rear,front
    if front == -1 or rear==front:
        print("Queue is empty")
    else:
        print(f"{queue[front]} is dequeued")
        queue[front] = None
        if front == rear:
            front = rear = -1 
        else:
            front = (front+1)%size

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)
enqueue(50)
dequeue()
print(queue)
enqueue(60)
print(queue)

print(front,rear)

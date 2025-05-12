size=5
queue = [None] * size
front = -1
rear = -1

def enqueue(val):
    global rear,front

    if (rear+1)%size == front:
        print("Queue full")
        return 
    rear = (rear+1)%size
    queue[rear] = val
    print(f"Appended {queue[rear]}")

    if front == -1:
        front = 0

def dequeue():
    global front,rear

    if front == -1:
        print("Queue is empty")
        return
    elif front == rear and front!=-1:
       print(f"Popped {queue[front]}")
       queue[front] = None
       front = rear = -1
       return
    else:
        print(f"Popped {queue[front]}")
        queue[front] = None
        front = (front+1)%size

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
dequeue()
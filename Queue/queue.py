size=5
queue = [None]*size
front = 0
end = 0

def enqueue(val):
    global end
    if end < size:
        queue[end] = val
        end+=1
        print(f"{val} has been added")
    else:
        print("Queue is full")    

def dequeue():
    global front,end
    if front == end:
        print("Queue is empty")
    else:    
        print(f"{queue[front]} has been removed")
        queue[front] = None
        front+=1

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)
enqueue(60)
print(queue)

dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
print(queue)




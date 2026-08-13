class Queue:
    def __init__(self,size):
        self.arr=[None]*size
        self.front=0
        self.rear=0
        self.size=size

    def enqueue(self,val):
        if self.rear == self.size:
            print("Queue is filled")
        else:
            self.arr[self.rear] = val    
            self.rear +=1

    def dequeue(self):
        if self.front == self.rear:
            print("The queue is empty")
        else:
            print("Dequeued element is :",self.arr[self.front])
            self.front +=1

    def display(self):
        temp=self.front
        while temp != self.rear:
            print(self.arr[temp],sep=" ")
            temp +=1


if __name__=='__main__':
    Q=Queue(5)
    while True:
        choice=int(input("1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n"))
        match choice:
            case 1:
                val=int(input("Enter value to be enqueued : "))
                Q.enqueue(val)
            case 2:
                Q.dequeue()   
            case 3:
                Q.display()
            case 4:
                exit()
            case _:
                print("Please enter a valid number")            
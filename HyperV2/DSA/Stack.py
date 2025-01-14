class Stack:
    def __init__(self,size):
        self.array = [None] * size
        self.top = -1
        self.size = size
    
    def push(self,data):
        self.top+=1
        if self.top < self.size:
            self.array[self.top] = data
        else:
            print("Stack is full")
    
    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(f"The popped element is {self.array[self.top]}")
            top-=1
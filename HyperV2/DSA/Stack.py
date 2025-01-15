class Stack:
    def __init__(self,size):
        self.array = [None] * size
        self.top = -1
        self.size = size
    
    def push(self,data):
        if self.top + 1 < self.size:
            self.top += 1
            self.array[self.top] = data
        else:
            print("Stack is full")
    
    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(f"The popped element is {self.array[self.top]}")
            self.top-=1

if __name__ == "__main__":
    s = Stack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.push(60)
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
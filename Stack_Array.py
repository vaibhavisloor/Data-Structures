class Stack:
    def __init__(self,size):
        self.arr=[None]*size
        self.top=-1
        self.size=size

    def push(self,val):
        if self.top == self.size - 1:
            print("Stack is filled")
        else:
            self.top += 1
            self.arr[self.top] = val  
             

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(f"{self.arr[self.top]}")
            self.top -= 1
            


    def display(self):
        temp = self.top
        while(temp >=0):
            print(f"{self.arr[temp]}")
            temp-=1       

if __name__ == '__main__':
    S=Stack(5)
    while(True):
        print("1.Push a value \n2.Pop the topmost value \n3.Display\n4.Exit")
        choice = int(input("Enter a number : "))
        match choice:
            case 1:
                val = int(input("Enter the value to be pushed : "))
                S.push(val)
            case 2:
                S.pop()
                print("Topmost value popped")
            case 3:
                S.display() 
            case 4:
                exit()     
            case _:
                print("Please enter a valid number")    



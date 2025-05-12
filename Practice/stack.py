stack = []

def display():
    print(stack)

def push(val):
    stack.append(val)

display()

push(5)
push(4)
push(3)
push(2)
push(1)
push(6)
push(7)
display()

stack.pop()
display()
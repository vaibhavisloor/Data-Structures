class Node:
    def __init__(self,val):
        self.prev = None
        self.data = val
        self.link=None

class CDLL:
    def __init__(self):
        self.head = None

    def addFirst(self,val):
        newNode=Node(val)
        if self.head == None:
            newNode.prev = newNode.link = self.head = newNode
        else:
            temp = self.head
            while(temp.link != self.head):
                temp = temp.link
            newNode.link=self.head
            self.head.prev=newNode
            newNode.prev = temp
            temp.link=newNode
            self.head=newNode
        self.print_list()    
 
    def addLast(self,val):
        newNode=Node(val)
        temp=self.head
        while(temp.link != self.head):
            temp = temp.link
        temp.link=newNode
        newNode.prev=temp
        newNode.link=self.head
        self.head.prev = newNode
        self.print_list()   

    def addMid(self,val,prev_node_val):
        newNode=Node(val)
        lastNode=self.head
        while(lastNode.link != self.head):
            lastNode = lastNode.link
        if lastNode.data == prev_node_val:
            lastNode.link=newNode
            newNode.prev = lastNode
            newNode.link = self.head
            self.head.prev=newNode
        else:
            temp=self.head
            while(temp.data != prev_node_val):
                temp = temp.link
            temp.link.prev = newNode
            newNode.link=temp.link
            newNode.prev=temp
            temp.link=newNode
        self.print_list()   


    def delete_node(self,val):
        lastNode = self.head
        while(lastNode.link != self.head):
            lastNode = lastNode.link
        if lastNode.data == val:
            self.head.prev = lastNode.prev
            lastNode.prev.link = self.head
        else:
            temp =self.head
            while(temp.data != val):
                temp = temp.link
            temp.prev.link = temp.link
            temp.link.prev = temp.prev
        self.print_list()       

    def print_list(self):
        temp = self.head
        while(temp):
            print(f"{temp.data} ->",end='')
            if (temp.link == self.head):
                break
            else:
                temp = temp.link            
        # print(f"{self.head.data}") 
        print("\n")           


LL=CDLL()
while(True):
    choice = int(input("1.Add Node at start of LL\n2.Add Node at end of LL\n3.Add after a value\n4.Delete node\n5.Print List\n6.Exit\n\n"))
    match choice:
        case 1:
            val=int(input("Enter the value : "))
            LL.addFirst(val)
        case 2:
            val=int(input("Enter the value : "))
            LL.addLast(val)
        case 3:
            val=int(input("Enter the value to be added : "))
            prev_node_val=int(input("Enter the value after which you want to add the node : "))
            LL.addMid(val,prev_node_val)    
        case 4:
            val=int(input("Enter the value to be deleted : "))
            LL.delete_node(val)
        case 5:
            LL.print_list()
        case 6:
            exit()
        case _:
            print("Please enter a valid number") 
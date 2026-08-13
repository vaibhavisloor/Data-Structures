class Node:
    def __init__(self,val) :
        self.data = val
        self.link = None

class CSLL:
    def __init__(self):
        self.head = None

    def addFirst(self,val):
        temp=self.head
        newNode=Node(val)
        if self.head == None:
            self.head=newNode
            newNode.link = self.head
        else:
            newNode.link=self.head
            while(temp.link != self.head):
                temp=temp.link
            temp.link = newNode
            self.head=newNode
        self.print_list()      

    def addLast(self,val):
        temp=self.head
        newNode=Node(val)
        while(temp.link != self.head):
            temp = temp.link
        temp.link = newNode
        newNode.link = self.head
        self.print_list() 


    def addMid(self,val,prev_node_val):
        temp = self.head  
        newNode = Node(val)
        while(temp.data != prev_node_val):
            temp = temp.link
        newNode.link = temp.link
        temp.link = newNode
        self.print_list()    

    def delete_node(self,val):
            
        if self.head.data == val:
            first_node = self.head

            self.head = self.head.link
            temp = self.head
            
            while(temp.link != first_node):
                temp = temp.link
            temp.link = self.head    

           

        else:
            temp = self.head
            while(temp.link.data != val):
                temp = temp.link
            temp.link = temp.link.link 
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


LL=CSLL()

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
            pass
            LL.print_list()
        case 6:
            exit()
        case _:
            print("Please enter a valid number") 
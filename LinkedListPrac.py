class Node:
    def __init__(self,val):
        self.data = val
        self.link=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def print_list(self):
        temp = self.head
        while(temp):
            print(f"{temp.data} -> ",end="")    
            temp = temp.link
        print("None\n\n")    
        
    def addFirst(self,val):
        node=Node(val)
        if self.head == None:
            self.head = node
        else:
            temp=self.head
            self.head=node
            node.link = temp
        self.print_list()    

    def addLast(self,val):
        node=Node(val)
        if self.head == None:
            self.head = node
        else:
            temp=self.head
            while(temp.link):
                temp = temp.link
            temp.link=node  
        self.print_list()      

    def addMid(self,val,prev_node_val):
        node=Node(val)
        temp = self.head
        while(temp.data != prev_node_val):
            temp = temp.link
        node.link = temp.link
        temp.link = node
        self.print_list()

    def delete_node(self,val):
        
        if self.head.data == val:
            self.head = self.head.link
        else:
            temp = self.head
            while (temp.link.data != val):
                temp = temp.link
            temp.link = temp.link.link    
        
        self.print_list()  


    


LL=LinkedList()

while(True):
    choice = int(input("1.Add Node at start of LL\n2.Add Node at end of LL\n3.Add after a value\n4.Delete node\n5.Print List\n6.Exit\n\n"))
    if choice == 1:
        val=int(input("Enter the value : "))
        LL.addFirst(val)
    elif choice == 2:
        val=int(input("Enter the value : "))
        LL.addLast(val)
    elif choice == 3:
        val=int(input("Enter the value to be added : "))
        prev_node_val=int(input("Enter the value after which you want to add the node : "))
        LL.addMid(val,prev_node_val)    
    elif choice == 4:
         val=int(input("Enter the value to be deleted : "))
         LL.delete_node(val)
    elif choice == 5:
        pass
        LL.print_list()
    elif choice == 6:
        exit()
    else:
        print("Please enter a valid number")


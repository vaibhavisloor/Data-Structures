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
    # def addLast(self,val):
    #     newNode=Node(val):
                   




LL=CDLL()



LL.addFirst(10)
LL.addFirst(20)
LL.addFirst(30)
LL.addFirst(40)
LL.addFirst(50)
# while(True):
    # choice = int(input("1.Add Node at start of LL\n2.Add Node at end of LL\n3.Add after a value\n4.Delete node\n5.Print List\n6.Exit\n\n"))
    # match choice:
    #     case 1:
    #         val=int(input("Enter the value : "))
    #         LL.addFirst(val)
    #     case 2:
    #         val=int(input("Enter the value : "))
    #         LL.addLast(val)
    #     case 3:
    #         val=int(input("Enter the value to be added : "))
    #         prev_node_val=int(input("Enter the value after which you want to add the node : "))
    #         LL.addMid(val,prev_node_val)    
    #     case 4:
    #         val=int(input("Enter the value to be deleted : "))
    #         LL.delete_node(val)
    #     case 5:
    #         pass
    #         LL.print_list()
    #     case 6:
    #         exit()
    #     case _:
    #         print("Please enter a valid number") 
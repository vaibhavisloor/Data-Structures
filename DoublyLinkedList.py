class Node:
    def __init__(self,val):
        self.prev = None
        self.data=val
        self.link = None

class DoublyLinkedList:        
    def __init__(self):
        self.head=None

    def addFirst(self,val):

        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.link = self.head
            self.head.prev = newNode
            self.head = newNode

    def addLast(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while(temp.link):
                temp = temp.link
            temp.link = newNode
            newNode.prev = temp

    def addMid(self,val,prev_node_val):
        temp = self.head
        newNode = Node(val)
        while(temp.data != prev_node_val):
            temp = temp.link
        newNode.link = temp.link
        temp.link.prev = newNode
        newNode.prev = temp
        temp.link=newNode   

    def delete(self,val):
        temp = self.head
        while(temp.data != val):
            temp = temp.link

        temp.prev.link = temp.link
        temp.link.prev = temp.prev 


    def search(self,val):
        temp = self.head
        while(temp):
            if temp.data == val:
                return True
            else:
                temp=temp.link
        return False  

               

    def display(self):
        temp =self.head
        while(temp):
            print(f"{temp.data} <=> ", end='')
            temp = temp.link
        print("None\n\n")   


if __name__== '__main__':
    DL=DoublyLinkedList()
    while(True):
        print("1.Add First\n2.Add Last\n3.Add Mid\n4.Delete\n5.Search\n6.Exit\n")
        choice = int(input("Enter Choice : \n\n"))
        if choice == 1:
            val = int(input("Enter value of the node : "))
            DL.addFirst(val)
            DL.display()
        elif choice == 2:
            val = int(input("Enter value of the node : "))
            DL.addLast(val)
            DL.display()
        elif choice == 3:
            val = int(input("Enter value of the node : "))
            prev_node_val = int(input("Enter value of the previous node : "))
            DL.addMid(val,prev_node_val) 
            DL.display()
        elif choice == 4:
            val = int(input("Enter value of the node : "))
            DL.delete(val)  
            DL.display()
        elif choice == 5:
            val = int(input("Enter value of the node : "))
            DL.search(val)
            DL.display()
        elif choice == 6:
            exit()   
        else:
            print("Please enter a valid number")             








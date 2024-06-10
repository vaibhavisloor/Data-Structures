class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_list(self):
        temp=self.head

        while(temp):
            print(f"{temp.data} -> ",end="")
            temp=temp.link
        print("None")



# Adding node to the start of the list
    def addFirst(self,val):
        newNode = Node(val)
        newNode.link = self.head
        self.head=newNode    



# Adding node at the end of the list
    def addLast(self,val):
        lastNode=Node(val)
        temp=self.head

        if self.head == None:
            self.head=lastNode
        else:    
            while(temp.link):
                temp=temp.link
            temp.link=lastNode

# Searching a list              
    def search(self,val):
        temp=self.head

        while(temp):
            if temp.data == val:
                return True
            else:
                temp=temp.link
        return False

#Deleting element from list
    def delete(self,val):
        temp = self.head
        if temp.data == val:
            head=head.link
        else:
               while(temp):
                   if temp.link.data == val:
                       temp.link = temp.link.link
                       break
                   else:
                        temp=temp.link



if __name__ == '__main__':
    list=LinkedList()
    node1=Node(10) 
    node2=Node(20) 
    node3=Node(30) 
    list.head=node1
    node1.link=node2
    node2.link=node3

    list.print_list()


    list.addFirst(100)
    list.print_list()
    list.addLast(200)
    list.print_list()
    print(list.search(20))
    print(list.search(21))
    list.delete(20)
    list.print_list()

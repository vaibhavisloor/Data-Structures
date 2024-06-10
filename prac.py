# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# c=[]
# for i in range(len(a)):
#     c.append(a[i]+b[i])

# # print(c)    
# a=[10,3,8,24,12]
# for i in range(0,len(a)):
#     for j in range(0,i)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# for row in a:
#     print(row)



class Node:
    def __init__(self,val):
        self.val=val
        self.link=None


class LinkedList:
    def __init__(self):
        self.head=None

    def addFirst(self,val):
        newnode=Node(val)
        if self.head == None:
            self.head=newnode
        else:
            newnode.link=self.head
            self.head=newnode

    def addLast(self,val):
        newnode=Node(val)
        temp=self.head
        if self.head == None:
            self.head=newnode
        else:    
            while temp.link != None:
                temp=temp.link
            temp.link = newnode

    def delete_node(self,val):
        try:
            if self.head.val == val:
                self.head = self.head.link
            else:
                temp=self.head
                while(temp.link.val != val):
                    temp=temp.link
                temp.link = temp.link.link
        except AttributeError:
            print("The value doesnt exist in the list")        

    def print_list(self):
        temp=self.head 
        while(temp):
            print(f"{temp.val}")
            temp=temp.link   





LL=LinkedList()

while(True):
    choice = int(input("1.Add Node at start of LL\n2.Add Node at end of LL\n4.Delete node\n5.Print List\n6.Exit\n\n"))
    if choice == 1:
        val=int(input("Enter the value : "))
        LL.addFirst(val)
    elif choice == 2:
        val=int(input("Enter the value : "))
        LL.addLast(val)
    
    elif choice == 4:
         val=int(input("Enter the value to be deleted : "))
         LL.delete_node(val)
    elif choice == 5:
        LL.print_list()
    elif choice == 6:
        exit()
    else:
        print("Please enter a valid number")
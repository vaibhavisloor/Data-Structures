class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Chain:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*self.size

    def insert(self,num):

        index=num%self.size

        newNode=Node(num)

        if self.arr[index] == None:
            self.arr[index] = newNode
        else:
            temp = self.arr[index]

            while temp.next != None:
                temp=temp.next
            temp.next = newNode
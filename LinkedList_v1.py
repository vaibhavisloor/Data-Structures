class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class LinkedList:
    def __init__(self):
        self.head=None

if __name__ == '__main__':
    list=LinkedList()
    node1=Node(10) 
    node2=Node(20) 
    node3=Node(30) 
    list.head=node1
    node1.link=node2
    node2.link=node3

    def print_list():
        temp=list.head

        while(temp):
            print(f"{temp.data} -> ",end="")
            temp=temp.link
        print("None")    

    print_list()

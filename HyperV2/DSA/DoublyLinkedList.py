class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head

        while temp != None:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")

    
    def add_first(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def add_last(self,data):
        newNode = Node(data)
        temp = self.head

        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp
    
    def delete(self,data):
        temp = self.head
        while temp.next.data != data:
            temp = temp.next
        temp.next = temp.next.next
        temp.next.prev = temp

if __name__ == "__main__":
    dll = DLL()

    dll.add_first(10)
    dll.add_first(20)
    dll.add_first(30)
    dll.add_first(40)
    dll.add_first(50)
    dll.add_last(5)
    dll.add_last(4)
    dll.add_last(3)
    dll.add_last(2)
    dll.add_last(1)
    dll.print_list()


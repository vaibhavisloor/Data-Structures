class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        temp = self.head

        while temp!=None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def add_first(self,data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
    
    def add_last(self,data):
        temp = self.head

        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)

    def delete(self,data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.data != data:
                temp = temp.next
            temp.next = temp.next.next
    def search(self,data):
        temp = self.head

        while temp!=None:
            if temp.data == data:
                return True
            temp = temp.next
        return False




if __name__== "__main__":
    llist = LinkedList()
    llist.head = Node(10)
    llist.head.next = Node(20)

    llist.print_LL()
    llist.add_first(30)
    llist.print_LL()
    llist.add_last(40)
    llist.print_LL()
    llist.add_last(50)
    llist.add_last(70)
    llist.print_LL()
    llist.delete(30)
    llist.delete(50)
    llist.print_LL()
    llist.delete(70)
    llist.print_LL()
    print(llist.search(20))
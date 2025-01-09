class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
    
    def add_first(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
            self.head = newNode

    def add_last(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("HEAD")

    def delete(self,data):
        if self.head is None:
            print("List is empty")
            return

        # If the node to delete is the head
        if self.head.data == data:
            if self.head.next == self.head:  # Only one node
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            return

        # Deleting other nodes
        prev = self.head
        curr = self.head.next
        while curr != self.head:
            if curr.data == data:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print(f"Node with data {data} not found.")


if __name__ == "__main__":
    cll= CLL()
    cll.add_first(10)
    cll.add_first(20)
    cll.add_first(30)
    cll.add_first(40)
    cll.add_first(50)
    cll.add_first(60)
    cll.print_list()
    cll.add_last(5)
    cll.add_last(4)
    cll.add_last(3)
    cll.add_last(2)
    cll.add_last(1)
    cll.print_list()
    cll.delete(60)
    cll.delete(40)
    cll.print_list()

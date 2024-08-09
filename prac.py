# 1.LinkedList

# class Node:
#     def __init__(self,val) :
#         self.val = val
#         self.next=None

# class LL:
#     def __init__(self):
#         self.head = None

#     def add_first(self,val):          
#         newNode = Node(val)
#         if self.head == None:
#             self.head=newNode
#         else:
#             newNode.next=self.head
#             self.head=newNode

#     def add_last(self,val):
#         newNode = Node(val)
#         if self.head == None:
#             self.head = newNode
#         else:    
#             temp = self.head
#             while temp.next!=None:
#                 temp=temp.next
#             temp.next = newNode

#     def show_list(self):
#         temp = self.head
#         while temp!= None:
#             print(f"{temp.val} --> ",end="")
#             temp=temp.next
#         print("None")
#     def delete_node(self,val):
#         if self.head.val == val:
#             self.head = self.head.next
#         else:
#             temp = self.head
#             while temp.next.val != val:
#                 temp = temp.next 
#             temp.next = temp.next.next    

#     def reverse_linked_list(self):
#         prev = None
#         cur_node = self.head

#         while cur_node != None:
#             next_node = cur_node.next
#             cur_node.next = prev
#             prev = cur_node
#             cur_node = next_node
#         self.head = prev    

# if __name__ == "__main__":
#     ll = LL()

#     ll.add_last(10)
#     ll.add_last(90)
#     ll.add_last(20)
#     ll.add_last(30)
#     ll.add_last(40)
#     ll.add_first(34)

#     # ll.delete_node(20)

#     ll.show_list()

#     ll.reverse_linked_list()

#     ll.show_list()

#DoublyLinkedList

class Node:
    def __init__(self,val) :
        self.prev = None
        self.val=val
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def add_first(self,val):
        newNode= Node(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def add_last(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp   

    def delete_element(self,val):
        if self.head.val == val:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.val != val:
                temp = temp.next
            temp.next = temp.next.next
            temp.next.next.prev = temp  

    def show_list(self):
        temp = self.head
        while temp:
            print(f"{temp.val} <=> ",end="")
            temp=temp.next
        print("None")    
if __name__ == "__main__":
    dll=DLL()

    dll.add_first(10)        
    dll.add_first(12)        
    dll.add_first(13)        
    dll.add_last(20)
    dll.add_last(28)
    dll.add_last(27)
    dll.add_last(22)


    dll.delete_element(20)

    dll.show_list()
    
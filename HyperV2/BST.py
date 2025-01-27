class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
def insert(root,val):
    if root is None:
        return Node(val)
    elif root.data < val:
        root.right = insert(root.right,val)
    elif root.data > val:
        root.left = insert(root.left,val)
    return root

def inorder(root):
    if root == None:
        return 
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def search(root,val):
    if root is None:
        return 0
    if root.data == val:
        return 1
    elif root.data > val:
        return search(root.left,val)
    elif root.data < val:
        return search(root.right,val)
        
    

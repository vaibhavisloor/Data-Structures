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


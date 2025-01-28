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
        
    
if __name__ == '__main__':
    root = None

    root=insert(root,10)
    root=insert(root,5)
    root=insert(root,90)
    root=insert(root,45)
    root=insert(root,30)
    root=insert(root,1)


    inorder(root)

    print(search(root,59))
    print(search(root,90))
    print(search(root,30))


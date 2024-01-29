class Node:
    def __init__(self,val):
        self.left = None
        self.key=val
        self.right = None

def insert(root,val):
    if root == None:
        return Node(val)
    elif root.key > val:
        root.left=insert(root.left,val)
    elif root.key < val:
        root.right = insert(root.right,val)
    return root

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.key,end=" ")
    inorder(root.right)


if __name__=='__main__':
    
    root = None

    root=insert(root,100)
    root=insert(root,50)
    root=insert(root,150)
    root=insert(root,15)
    root=insert(root,10)

    inorder(root)

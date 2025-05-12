class Node:
    def __init__(self,val):
        self.left = None
        self.val = val
        self.right = None

def addNode(val,root):
    if root == None:
        return Node(val)
    else:
        if val > root.val:
            root.right = addNode(val,root.right)
        elif val < root.val:
            root.left = addNode(val,root.left)
        return root
            
def inorder(root):
    if root == None:
        return None
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def search(root,val):
    if root == None:
        return False
    if val > root.val:
        return search(root.right,val)
    elif val < root.val:
        return search(root.left,val)
    else:
        return True
def getRightmin(root):
    while root.left != None:
        root=root.left
    return root.val

def deleteNode(root,val):
    if val > root.val:
        root.right = deleteNode(root.right,val)
    elif val < root.val:
        root.left = deleteNode(root.left, val)
    else:
        if root.left == None and root.right == None:
            return None
        elif root.left == None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            right_min = getRightmin(root.right)
            root.val = right_min
            root.right = deleteNode(root.right,right_min)
    return root

if __name__ == '__main__':
    root = None
    for val in [10, 5, 15, 2, 7, 12, 20]:
        root = addNode(val, root)

    print("Inorder before deletion:")
    inorder(root)

    print("\n\nDeleting 10...")
    root = deleteNode(root, 10)

    print("\nInorder after deletion:")
    inorder(root)


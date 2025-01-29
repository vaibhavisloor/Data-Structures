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
    print(root.data, end=" ")
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

def delete_node(root,val):
    if root is None:
        return None
    
    if root.data > val:
        root.left = delete_node(root.left,val)
    elif root.data < val:
        root.right = delete_node(root.right, val)
    else:
        if (root.left is None) and (root.right is None):
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            right_min = get_right_min(root)
            root.data = right_min
            root.right = delete_node(root.right,right_min)
    return root

def get_right_min(root):
    root = root.right

    while root.left != None:
        root = root.left
    print(f"Right min : {root.data}")
    return root.data


    
if __name__ == '__main__':
    root = None

    root=insert(root,10)
    root=insert(root,5)
    root=insert(root,90)
    root=insert(root,45)
    root=insert(root,30)
    root=insert(root,50)
    root=insert(root,48)
    root=insert(root,55)


    inorder(root)
    print("\n")
    # print(search(root,59))
    # print(search(root,90))
    # print(search(root,30))

    delete_node(root,45)

    inorder(root)
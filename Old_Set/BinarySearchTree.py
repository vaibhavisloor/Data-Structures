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
 
def search(root,val):
    if root == None:
        return False
    if root.key == val:
        return True
    if root.key > val:
        return search(root.left,val)
    else:
        return search(root.right,val)

def delete_node(root,val):
    if root == None:
        return None

    if root.key < val:
        root.right=delete_node(root.right,val)
    elif root.key > val:
        root.left=delete_node(root.left,val)
    else:
        if root.left == None and root.right == None:
            return None
        elif root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            right_min = getRightMin(root.right)
            root.key = right_min
            root.right = delete_node(root.right,right_min)
    return root        
 
def getRightMin(root): #Whenever a root has two children, the lowest value of the right subtree replaces it.
    temp = root
    while temp.left != None:
        temp = temp.left
    return temp.key    

if __name__=='__main__':
    
    root = None

    root=insert(root,100)
    root=insert(root,50)
    root=insert(root,150)
    root=insert(root,15)
    root=insert(root,10)
    
    inorder(root)

    print(search(root,20))
    print(search(root,10))

    delete_node(root,100)
    inorder(root)

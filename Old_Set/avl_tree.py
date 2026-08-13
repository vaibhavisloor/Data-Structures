class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Every new node starts with height 1

# Helper function to get the height of a node
def get_height(node):
    if not node:
        return 0
    return node.height

# Helper function to update the height of a node
def update_height(node):
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))

# Helper function to get the balance factor of a node
def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

# Left rotation
def left_rotate(z):
    y = z.right
    T2 = y.left

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    update_height(z)
    update_height(y)

    # Return the new root
    return y

# Right rotation
def right_rotate(z):
    y = z.left
    T3 = y.right

    # Perform rotation
    y.right = z
    z.left = T3

    # Update heights
    update_height(z)
    update_height(y)

    # Return the new root
    return y

# Insert a node into the AVL tree
def insert(root, value):
    # Step 1: Perform normal BST insertion
    if not root:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        # Duplicate values are not allowed in AVL
        return root

    # Step 2: Update the height of the ancestor node
    update_height(root)

    # Step 3: Get the balance factor to check whether this node became unbalanced
    balance = get_balance(root)

    # Case 1: Left Left (LL)
    if balance > 1 and value < root.left.value:
        return right_rotate(root)

    # Case 2: Right Right (RR)
    if balance < -1 and value > root.right.value:
        return left_rotate(root)

    # Case 3: Left Right (LR)
    if balance > 1 and value > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Case 4: Right Left (RL)
    if balance < -1 and value < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Function to get the node with minimum value
def get_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Delete a node from the AVL tree
def delete(root, value):
    # Step 1: Perform standard BST delete
    if not root:
        return root

    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp

        temp = get_min_value_node(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)

    if root is None:
        return root

    # Step 2: Update the height of the current node
    update_height(root)

    # Step 3: Get the balance factor
    balance = get_balance(root)

    # Case 1: Left Left (LL)
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)

    # Case 2: Left Right (LR)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Case 3: Right Right (RR)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)

    # Case 4: Right Left (RL)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Function to do an inorder traversal of the tree
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Example usage
if __name__ == "__main__":
    avl_tree = None

    # Inserting nodes into the AVL tree
    values_to_insert = [10, 20, 30, 40, 50, 25]
    for value in values_to_insert:
        avl_tree = insert(avl_tree, value)

    # Print the tree structure using inorder traversal
    print("Inorder Traversal of the AVL Tree: ")
    inorder_traversal(avl_tree)  # Should print the sorted order

    # Deleting a node
    avl_tree = delete(avl_tree, 40)

    print("\n\nInorder Traversal after deleting 40: ")
    inorder_traversal(avl_tree)

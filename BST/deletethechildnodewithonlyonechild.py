from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Insert into BST
def insert(root, key):
    if not root:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Function to delete node using queue (level order traversal)
def delete_node_with_one_child(root, key):
    if not root:
        return None

    # Special case: root is the target
    if root.data == key:
        if root.left and not root.right:
            return root.left
        elif root.right and not root.left:
            return root.right
        else:
            print("Cannot delete root: it has zero or two children.")
            return root

    queue = deque([(root, None)])  # (current_node, parent_node)

    while queue:
        node, parent = queue.popleft()

        if node.data == key:
            # Check if node has only one child
            if (node.left and not node.right) or (node.right and not node.left):
                child = node.left if node.left else node.right

                # Connect parent to the child
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child

                print(f"Node {key} deleted. It had one child.")
                return root
            else:
                print(f"Node {key} does not have exactly one child. Not deleted.")
                return root

        if node.left:
            queue.append((node.left, node))
        if node.right:
            queue.append((node.right, node))

    print(f"Node {key} not found.")
    return root

# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Example usage
if __name__ == "__main__":
    root = None
    values = [20, 10, 30, 5, 15, 25]  # BST
    for val in values:
        root = insert(root, val)

    print("Inorder before deletion:")
    inorder(root)

    key_to_delete = 10  # Node 10 has one child (15)
    root = delete_node_with_one_child(root, key_to_delete)

    print("\nInorder after deletion:")
    inorder(root)

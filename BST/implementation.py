from collections import defaultdict, deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert into BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Level-order traversal with horizontal distance
def print_horizontal_distances(root):
    if root is None:
        return

    hd_map = defaultdict(list)
    queue = deque([(root, 0)])  # (node, horizontal_distance)

    while queue:
        node, hd = queue.popleft()
        hd_map[hd].append(node.data)

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Printing the horizontal distances in sorted order
    print("Nodes at each Horizontal Distance:")
    for hd in sorted(hd_map):
        print(f"HD {hd}: {' '.join(map(str, hd_map[hd]))}")

# Example usage
if __name__ == "__main__":
    root = None
    values = [10, 6, 15, 3, 8, 12, 18]
    for val in values:
        root = insert(root, val)

    print_horizontal_distances(root)

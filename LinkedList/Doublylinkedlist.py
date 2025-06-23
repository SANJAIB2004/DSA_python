class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> " if curr.next else " -> None\n")
            curr = curr.next

    def alternative_merge(self, head1, head2):
        temp1 = head1
        temp2 = head2

        while temp1 and temp2:
            ptr1 = temp1.next
            ptr2 = temp2.next

            temp1.next = temp2
            temp2.prev = temp1

            if ptr1:
                temp2.next = ptr1
                ptr1.prev = temp2

            temp1 = ptr1
            temp2 = ptr2

        return head1  # Return merged head


# === Testing ===
dll1 = DoublyLinkedList()
dll2 = DoublyLinkedList()

# Append to both lists
for val in [1, 2, 3, 4]:
    dll1.append(val)
for val in [5, 6, 7]:
    dll2.append(val)

print("List 1:")
dll1.print_list()

print("List 2:")
dll2.print_list()

# Merge alternatively
merged_head = dll1.alternative_merge(dll1.head, dll2.head)

# Print result
print("Merged List (alternating):")
merged_list = DoublyLinkedList()
merged_list.head = merged_head
merged_list.print_list()

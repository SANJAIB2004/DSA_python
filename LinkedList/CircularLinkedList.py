class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def delete_node(self, key):
        if not self.head:
            return

        curr = self.head
        prev = None

        while True:
            if curr.data == key:
                if prev:
                    prev.next = curr.next
                else:  # Deleting head node
                    if curr.next == self.head:
                        self.head = None
                        return
                    else:
                        # Move to last node to fix circular link
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = self.head.next
                        self.head = self.head.next
                return

            prev = curr
            curr = curr.next

            if curr == self.head:
                break

    def display(self):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Usage
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.display()
cll.delete_node(2)
cll.display()

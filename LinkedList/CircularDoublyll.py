class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        tail = self.head.prev

        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

    def delete_node(self, key):
        if not self.head:
            return

        curr = self.head
        while True:
            if curr.data == key:
                if curr.next == curr:  # Only one node
                    self.head = None
                    return
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if curr == self.head:
                        self.head = curr.next
                    return
            curr = curr.next
            if curr == self.head:
                break




    def display_forward(self):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    def display_backward(self):
        if not self.head:
            print("List is empty")
            return

        temp = self.head.prev
        head = temp.next
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.prev
            if temp.next == head:
                break
        print("(tail)")

# Usage
cdll = CircularDoublyLinkedList()
cdll.insert_at_end(10)
cdll.insert_at_end(20)
cdll.insert_at_end(30)
cdll.display_forward()
cdll.display_backward()
cdll.delete_node(20)
cdll.display_forward()
cdll.display_backward()

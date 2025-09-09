class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def inserAtEnd(self,data):
        last = Node(data)
        if self.head is None:
            self.head = last
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next =last

    def insertAtPosition(self,data,position):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp =self.head
        for i in range(position-1):
            temp = temp.next
            newNode.next = temp.next
            temp.next =newNode


    def deleteAtBegin(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next.next and temp.next:
            temp =temp.next
        temp.next =None

    def deletespecificAtPosition(self,position):
        if self.head is None:
            return
        temp = self.head
        for i in range(position-1):
            temp =temp.next
        temp.next =temp.next.next

    def display(self):
        temp =self.head
        print("The Elements in the LinkedList are:")
        while temp:
            print(temp.data)
            temp = temp.next

    def counter(self):
        temp =self.head
        count =0
        while temp:
            count+=1
            temp =temp.next
        return count

    def reverse(self):
        prev =None
        current =self.head
        while current:
            next = current.next
            current.next =prev
            prev = current
            current = next
        self.head = prev








ll = LinkedList()


ll.insertAtBegin(10)
ll.insertAtBegin(20)
ll.insertAtBegin(30)
ll.insertAtBegin(40)
ll.insertAtPosition(23,2)
ll.display()
ll.deletespecificAtPosition(3)
print("After Deleting the specific element")
ll.display()
ll.inserAtEnd(50)
ll.deleteAtBegin()
print("After Deleting the first element")
ll.display()
ll.deleteAtEnd()
print("After Deleting the last element")
ll.display()
print("The Number of elements in the LinkedList are:",ll.counter())
ll.reverse()
print("After Reversing the LinkedList")
ll.display()


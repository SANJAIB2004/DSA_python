class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size  # Fixed-size array
        self.top = -1  # Stack is empty initially

    def push(self, value):
        if self.top >= self.size - 1:
            print("Stack Overflow: Cannot push", value)
        else:
            self.top += 1
            self.arr[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack Underflow: Stack is empty")
            return None
        else:
            popped = self.arr[self.top]
            self.arr[self.top] = None  # Optional: clear the slot
            self.top -= 1
            return popped

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack (top to bottom):")
            for i in range(self.top, -1, -1):
                print(self.arr[i])


# Example usage:
stk = Stack(3)
stk.pop()           # Underflow
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)        # Overflow
stk.display()       # 30, 20, 10 (top to bottom)
stk.pop()
stk.display()       # 20, 10

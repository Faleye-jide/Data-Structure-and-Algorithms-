class Stack:
    def __init__(self):
        self.items = []

    def insert(self, val):
        self.items.append(val)

    def isEmpty(self):
        return self.items == []

    def remove(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def get_size(self):
        return len(self.items)

s = Stack()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
s.insert(5)
print(f"The element in the stack is {s.items}")
print(f"The length of the stack is {s.get_size()}")
print(f"Top of the stack is {s.peek()}")
print(f"The number removed is {s.remove()}")
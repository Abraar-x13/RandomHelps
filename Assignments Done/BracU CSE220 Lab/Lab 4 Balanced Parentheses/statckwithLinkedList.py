class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LLStack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        currnt = self.head.next
        out = ""
        while currnt:
            out += str(currnt.value) + "->"
            currnt = currnt.next
        return out[:-3]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

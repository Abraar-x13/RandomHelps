class ArStack:
    def __init__(self):
        self.items = []

    def getSize(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        return self.items[len(self.items) - 1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        return self.items.pop()

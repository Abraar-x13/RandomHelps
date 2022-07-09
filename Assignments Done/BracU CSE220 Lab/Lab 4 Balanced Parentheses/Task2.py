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


LLstack = LLStack()

open_brackets = ["(", "{", "["]
closed_brackets = [")", "}", "]"]


def checkBalance(inputString):
    LLstack = []
    for i in inputString:
        if i in open_brackets:
            LLstack.append(i)
        elif i in closed_brackets:
            ps = closed_brackets.index(i)
            if ((len(LLstack) > 0) and
                    (open_brackets[ps] == LLstack[len(LLstack) - 1])):
                LLstack.pop()
            else:
                return "This expression is NOT correct."
    if len(LLstack) == 0:
        return "This expression is correct."
    else:
        return "This expression is NOT correct."


# Driver code
string = input("Enter string: ")
print(string, "\n", checkBalance(string))

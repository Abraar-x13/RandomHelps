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


Arstack = ArStack()

open_brackets = ["(", "{", "["]
closed_brackets = [")", "}", "]"]


def checkBalance(inputString):
    Arstack = []
    for i in inputString:
        if i in open_brackets:
            Arstack.append(i)
        elif i in closed_brackets:
            ps = closed_brackets.index(i)
            if ((len(Arstack) > 0) and
                    (open_brackets[ps] == Arstack[len(Arstack) - 1])):
                Arstack.pop()
            else:
                return "This expression is NOT correct."
    if len(Arstack) == 0:
        return "This expression is correct."
    else:
        return "This expression is NOT correct."


# Driver code
string = input("Enter string: ")
print(string, "\n", checkBalance(string))

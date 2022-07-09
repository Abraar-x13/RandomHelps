# QUESTION 5: Sort a DOUBLY linked sequential list using insertion sort algorithm.
class DNode:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class insertionSort:
    def __init__(self):
        self.head, self.tail = None, None

    def addDNode(self, data):
        newDNode = DNode(data)
        if (self.head == None):
            self.head = self.tail = newDNode
            self.head.previous, self.tail.next = None, None
        else:
            self.tail.next = newDNode
            newDNode.previous = self.tail
            self.tail, self.tail.next = newDNode, None

    def sortList(self):
        if (self.head != None):
            current = self.head
            while (current.next != None):
                index = current.next
                while (index != None):
                    if (current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
        else:
            return

    def printdLL(self):
        current = self.head
        if (self.head != None):
            while (current != None):
                print(current.data, end = " "),
                current = current.next
        else:
            print("Empty List.")
            return
        print()


if __name__ == '__main__':

    dLL = insertionSort()
    dLL.addDNode(-7), dLL.addDNode(11), dLL.addDNode(6), dLL.addDNode(0)
    dLL.addDNode(-3), dLL.addDNode(5), dLL.addDNode(10), dLL.addDNode(2)
    print("Original list: ")
    dLL.printdLL()
    dLL.sortList()
    print("Sorted list: ")
    dLL.printdLL()
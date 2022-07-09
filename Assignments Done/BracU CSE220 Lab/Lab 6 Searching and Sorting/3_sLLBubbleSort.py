# QUESTION 3: Sort a singly linked sequential list using bubble sort algorithm.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class bubbleSortLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = Node(data)
        if self.head != None:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def sortList(self):
        curr = self.head
        index = None
        if self.head != None:
            while curr != None:
                index = curr.next
                while index != None:
                    if curr.data > index.data:
                        temp = curr.data
                        curr.data = index.data
                        index.data = temp
                    index = index.next
                curr = curr.next
        else:
            return

    def printLL(self):
        curr = self.head
        if self.head != None:
            while curr != None:
                print(curr.data, end=" ")
                curr = curr.next
        else:
            print("Empty list")
            return

if __name__ == '__main__':
    sLL = bubbleSortLL()
    sLL.addNode(-7), sLL.addNode(11), sLL.addNode(6), sLL.addNode(0)
    sLL.addNode(-3), sLL.addNode(5), sLL.addNode(10), sLL.addNode(2)
    print("Original list: ")
    sLL.printLL(), sLL.sortList()
    print("\nSorted list: ")
    sLL.printLL()
# QUESTION 4: Sort a singly linked sequential list using selection sort algorithm.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class selectionSortLL:
    def swapNodes(self, nowX, nowY, lastY):
        self, lastY.next, temp= nowY, nowX, nowY.next
        nowY.next = nowX.next
        nowX.next = temp
        return self

    def recurSelectionSort(head):
        if (head.next == None):
            return head
        min, beforeMin, ptr= head, None, head
        while (ptr.next != None):
            if (ptr.next.data < min.data):
                min, beforeMin = ptr.next, ptr
            ptr = ptr.next
        if (min != head):
            head = selectionSortLL.swapNodes(head, head, min, beforeMin)
        head.next = selectionSortLL.recurSelectionSort(head.next)
        return head

    def sort(self):
        if (self == None):
            return None
        self = selectionSortLL.recurSelectionSort(self)
        return self

    def addNode(self, new_data):
        new_node, new_node.data, new_node.next,  = Node(0), new_data, self
        self = new_node
        return self

    def printList(head):
        while (head != None):
            print(head.data, end=" ")
            head = head.next


if __name__ == '__main__':
    head = None
    head = selectionSortLL.addNode(head, -7)
    head = selectionSortLL.addNode(head, 11)
    head = selectionSortLL.addNode(head, 6)
    head = selectionSortLL.addNode(head, 0)
    head = selectionSortLL.addNode(head, -3)
    head = selectionSortLL.addNode(head, 5)
    head = selectionSortLL.addNode(head, 10)
    head = selectionSortLL.addNode(head, 2)
    print("Original list: ")
    selectionSortLL.printList(head)
    head = selectionSortLL.sort(head)
    print("\nSorted list: ")
    selectionSortLL.printList(head)


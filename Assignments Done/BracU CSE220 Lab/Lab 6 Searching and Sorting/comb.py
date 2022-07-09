# QUESTION 1: Sort an array RECURSIVELY using selection sort algorithm.
def recurSelectionSort(A, i, n):
    min = i
    for j in range(i + 1, n):
        if A[j] < A[min]:
            min = j
    temp = A[min]
    A[min] = A[i]
    A[i] = temp
    if i + 1 < n:
        recurSelectionSort(A, i + 1, n)


# QUESTION 2: Sort an array RECURSIVELY using insertion sort algorithm.
def recurInsertionSort(A, n):
    if n <= 1:
        return
    recurInsertionSort(A, n - 1)
    tail, j = A[n - 1], n - 2
    while (j >= 0 and A[j] > tail):
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = tail


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

# QUESTION 6: Implement binary search algorithm RECURSIVELY
def binary_search(A, low, high, x):
    if high >= low:
        mid = low + (high - low)//2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return binary_search(A, low, mid - 1, x)
        elif A[mid] < x:
            return binary_search(A, mid + 1, high, x)
    else:
        return -1

# Question 7: Implement a recursive algorithm to
# find the n-th Fibonacci number using memoization.
def fib(num):
    if (num <= 1):
        return num
    F, S = 0, 0
    x=1
    if (A[num-x] != -1):
        F = A[num-x]
    else:
        F = fib(num-x)
    y=2
    if (A[num-y] != -1):
        S = A[num-y]
    else:
        S = fib(num-y)
    return F+S


if __name__ == '__main__':

    # Q1 start
    A = [-7, 11, 6, 0, -3, 5, 10, 2]
    print(f"Original array : {A}")
    recurSelectionSort(A, 0, len(A))
    print(f"After using recursive SELECTION sort : {A}")
    print("\n")
    # Q1 end

    # Q2 start
    A = [-7, 11, 6, 0, -3, 5, 10, 2]
    print(f"Original array : {A}")
    recurInsertionSort(A, len(A))
    print(f"After using recursive INSERTION sort : {A}")
    print("\n")
    # Q2 end

    # Q3 start
    sLL = bubbleSortLL()
    sLL.addNode(-7), sLL.addNode(11), sLL.addNode(6), sLL.addNode(0)
    sLL.addNode(-3), sLL.addNode(5), sLL.addNode(10), sLL.addNode(2)
    print("Original Linked List: ")
    sLL.printLL(), sLL.sortList()
    print("\nLL after Bubble sort: ")
    sLL.printLL()
    print("\n")
    # Q3 end

    # Q4 start
    head = None
    head = selectionSortLL.addNode(head, -7)
    head = selectionSortLL.addNode(head, 11)
    head = selectionSortLL.addNode(head, 6)
    head = selectionSortLL.addNode(head, 0)
    head = selectionSortLL.addNode(head, -3)
    head = selectionSortLL.addNode(head, 5)
    head = selectionSortLL.addNode(head, 10)
    head = selectionSortLL.addNode(head, 2)
    print("Original Linked List: ")
    selectionSortLL.printList(head)
    head = selectionSortLL.sort(head)
    print("\nLL after Selection sort: ")
    selectionSortLL.printList(head)
    print("\n")
    # Q4 end

    # Q5 start
    dLL = insertionSort()
    dLL.addDNode(-7), dLL.addDNode(11), dLL.addDNode(6), dLL.addDNode(0)
    dLL.addDNode(-3), dLL.addDNode(5), dLL.addDNode(10), dLL.addDNode(2)
    print("Original Doubly Linked List: ")
    dLL.printdLL()
    dLL.sortList()
    print("DLL after Insertion sort: ")
    dLL.printdLL()
    print("\n")
    # Q5 end

    # Q6 start
    A = [-7, -3, 0, 1, 2, 5, 9, 11]
    element = 9
    idx = binary_search(A, 0, len(A) - 1, element)
    print(f"Binary search on {A}")
    print(f"{element} is present at index {str(idx)}" if idx != -1 else f"{element} is not present in Array")
    print("\n")
    # Q6 end

    # Q7 start
    A = [-1 for i in range(50)]
    n = 20
    print(f" {n}th fibonacchi number is {fib(n)}")
    # Q7 end
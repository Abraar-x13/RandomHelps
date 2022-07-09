# QUESTION : Implement a recursive algorithm
# to add all the elements of a non-dummy headed
# singly linked linear list. Only head of the list
# will be given as parameter where you may assume
# every node can contain only integer as its element.
# Note: you’ll need a Singly Node2b class for this code.


class Node2b:
    def __init__(self, data):
        self.data = data
        self.next = None

def newNode2b(data):
    new_node = Node2b(data)
    new_node.data = data
    new_node.next = None
    return new_node

# Function to insert a new node at the end of linked list using recursion.
def insertEnd(head, data):
    if (head == None):
        return newNode2b(data)
    else:
        head.next = insertEnd(head.next, data)
    return head

# A Recursive funtion to traverse the LL, finding the sum along the way
def Rtraverse(head):
    global L
    if (head == None):
        return
    L+= head.data
    print(head.data, end=" ")
    Rtraverse(head.next)


# Driver code
if __name__ == '__main__':

    L = 0 # L is a varible to store the sum
    head = None
    head = insertEnd(head, 1)
    head = insertEnd(head, 2)
    head = insertEnd(head, 3)
    Rtraverse(head)
    print()
    print(f"The sum of all the nodes is {L}")

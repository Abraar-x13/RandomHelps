class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Inorder(root):
        if root is not None:
            Node.Inorder(root.left)
            print(root.data),
            Node.Inorder(root.right)

    def isSame(root1, root2):
        if (root1 is None and root2 is None):
            return 1 # trivial case
        elif (root1 is not None and root2 is None):
            return 0
        elif (root2 is not None and root1 is None):
            return 0
        else:
            if (not(root1.data == root2.data and
                    Node.isSame(root1.left, root2.left) and
                    Node.isSame(root1.right, root2.right))):
                return 0
            else:
                return 1

if __name__ == '__main__':

    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(8)
    root1.left.left = Node(2)
    root1.left.right = Node(4)

    root2 = Node(5)
    root2.left = Node(3)
    root2.right = Node(8)
    root2.left.left = Node(2)
    # root2.left.left = Node(9)
    root2.left.right = Node(4)

    if (Node.isSame(root1, root2)):
        print("Both BSTs are identical")
    else:
        print("BSTs are not identical")

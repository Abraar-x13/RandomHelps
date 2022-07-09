class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Q1 : RECURSIVELY calculate the height of a tree.
    def height(node):
        if node is None:
            return 0
        else:
            leftHeight, rightHeight = Node.height(node.left), Node.height(node.right)
            if leftHeight > rightHeight:
                return leftHeight+1
            else:
                return rightHeight+1
# /Q1

# Q2 : RECURSIVELY calculate the level of a Node in a tree.
    def findLevel(node, data, level):
        if node is None:
            return 0
        if node.data == data:
            return level
        downLevel = Node.findLevel(node.left, data, level + 1)
        if downLevel != 0:
            return downLevel
        downLevel = Node.findLevel(node.right, data, level + 1)
        return downLevel
# /Q2

# Q3 : Print elements of all the Nodes of a tree using Pre-order Traversal.
    def PreorderTravarsal(root):
        if root is not None:
            print(root.data, end=" ")
            Node.PreorderTravarsal(root.left)
            Node.PreorderTravarsal(root.right)
# /Q3

# Q4 : Print elements of all the Nodes of a tree using In-order Traversal.
    def InorderTraversal(root):
        if root is not None:
            Node.InorderTraversal(root.left)
            print(root.data, end=" ")
            Node.InorderTraversal(root.right)
# /Q4

# Q5 : Print elements of all the Nodes of a tree using Post-order Traversal.
    def PostorderTravarsal(root):
        if root is not None:
            Node.PostorderTravarsal(root.left)
            Node.PostorderTravarsal(root.right)
            print(root.data, end=" ")
# /Q5

# Q6 : Write a method which will evaluate whether two trees are exactly same or not.
    def isSame(root1, root2):
        if root1 is None and root2 is None:
            return 1  # trivial case
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
# /Q6

# Q7 : Write a method which will return a copy (new tree) of a given tree.
    def mirror(node):
        if node is not None:
            Node.mirror(node.left), Node.mirror(node.right)
            node.left, node.right = node.right, node.left
    def copyTree(self):
        mirror = Node(self.data)
        if self.right is not None:
            mirror.left = self.right.copyTree()
        if self.left is not None:
            mirror.right = self.left.copyTree()
        return mirror
# /Q7


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(0)
    root.left.left = Node(6)
    root.left.right = Node(9)
    root.left.right.left = Node(7)

    # Q1 Start
    print(f"Height of tree is {Node.height(root)}\n")
    # Q1 end

    # Q2 Start
    array = [4, 2, 0, 6, 9, 7]
    for x in array:
        level = Node.findLevel(root, x, 1)
        if level:
            print(f"Level of {x} is {Node.findLevel(root, x, 1)}")
        else:
            print(f"Element {x} is absent in tree")
    # Q2 end

    # Q3 Start
    print("\nPreorder traversal of binary tree is")
    Node.PreorderTravarsal(root)
    # Q3 end

    # Q4 Start
    print("\nInorder traversal of binary tree is")
    Node.InorderTraversal(root)
    # Q4 end

    # Q5 Start
    print("\nPostorder traversal of binary tree is")
    Node.PostorderTravarsal(root)
    # Q5 end

    # Q6 Start
    root2 = Node(4)
    root2.left = Node(2)
    root2.right = Node(0)
    root2.left.left = Node(6)
    root2.left.right = Node(9)
    # root2.left.right = Node(7)  # To make the tree different.
    root2.left.right.left = Node(7)

    if Node.isSame(root, root2):
        print("\n\nTwo trees are exactly same\n")
    else:
        print("\n\nTwo trees are not same\n")
    # Q6 end

    # Q7 Start
    print("Inorder traversal of the original tree")
    Node.InorderTraversal(root)
    Node.mirror(root)  # We have to mirror the tree before we copy it
    print("\nInorder traversal of the copied tree")
    Node.InorderTraversal(Node.copyTree(root))
    Node.mirror(root)  # We have to mirror the tree Again to have the original one back.
    # Q7 end

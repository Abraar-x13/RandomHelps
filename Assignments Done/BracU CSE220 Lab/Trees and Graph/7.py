class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def Inorder(root):
        if root is not None:
            Node.Inorder(root.left)
            print(root.data, end=" "),
            Node.Inorder(root.right)

    def mirror(node):
        if node is not None:
            temp = node, Node.mirror(node.left), Node.mirror(node.right)
            node.left, node.right = node.right, node.left
    def copyTree(self):
        mirror = Node(self.data)
        if self.right is not None:
            mirror.left = self.right.copyTree()
        if self.left is not None:
            mirror.right = self.left.copyTree()
        return mirror


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(0)
    root.left.left = Node(6)
    root.left.right = Node(9)
    root.left.right.left = Node(7)

    print("Inorder traversal of the original tree")
    Node.Inorder(root)
    Node.mirror(root) # We have to mirror the tree before we copy it
    print("\nInorder traversal of the copied tree")
    Node.Inorder(Node.copyTree(root))
    Node.mirror(root) # We have to mirror the tree Again to have the original one bacl.
    Node.Inorder(root)



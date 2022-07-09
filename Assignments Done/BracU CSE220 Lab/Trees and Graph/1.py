class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def maxDepth(node):
        if node is None:
            return 0
        else :
            lDepth = Node.maxDepth(node.left)
            rDepth = Node.maxDepth(node.right)

            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1





if __name__ == '__main__':

    root = Node(4)
    root.left = Node(2)
    root.right = Node(0)
    root.left.left = Node(6)
    root.left.right = Node(9)
    root.left.right.left = Node(7)

    print (f"Height of tree is {Node.maxDepth(root)}")





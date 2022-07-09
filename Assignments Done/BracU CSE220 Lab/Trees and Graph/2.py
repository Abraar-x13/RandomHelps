class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getLevelUtil(node, data, level):
        if node is None:
            return 0
        if node.data == data:
            return level
        downlevel = Node.getLevelUtil(node.left, data, level + 1)
        if downlevel != 0:
            return downlevel
        downlevel = Node.getLevelUtil(node.right, data, level + 1)
        return downlevel

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(0)
    root.left.left = Node(6)
    root.left.right = Node(9)
    root.left.right.left = Node(7)

    array = [4,2,0,6,9,7]
    for x in array:
        level = Node.getLevelUtil(root, x, 1)
        if level:
            print(f"Level of {x} is {Node.getLevelUtil(root, x, 1)}")
        else:
            print(x, "is not present in tree")

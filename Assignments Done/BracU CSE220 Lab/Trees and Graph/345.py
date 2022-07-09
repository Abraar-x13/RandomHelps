class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def InorderTraversal(root):
		if root is not None:
			Node.InorderTraversal(root.left)
			print(root.data, end = " ")
			Node.InorderTraversal(root.right)

	def PostorderTravarsal(root):
		if root is not None:
			Node.PostorderTravarsal(root.left)
			Node.PostorderTravarsal(root.right)
			print(root.data, end = " ")

	def PreorderTravarsal(root):
		if root is not None:
			print(root.data, end = " ")
			Node.PreorderTravarsal(root.left)
			Node.PreorderTravarsal(root.right)



if __name__ == '__main__':
	root = Node(4)
	root.left = Node(2)
	root.right = Node(0)
	root.left.left = Node(6)
	root.left.right = Node(9)
	root.left.right.left = Node(7)
	print ("Preorder traversal of binary tree is")
	Node.PreorderTravarsal(root)

	print("\nInorder traversal of binary tree is")
	Node.InorderTraversal(root)

	print ("\nPostorder traversal of binary tree is")
	Node.PostorderTravarsal(root)


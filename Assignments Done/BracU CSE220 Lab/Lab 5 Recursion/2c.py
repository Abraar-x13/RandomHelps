# QUESTION : Implement a recursive algorithm which will
# print all the elements of a non-dummy headed singly
# linked linear list in reversed order.
# NOTE from Abraar:
# Write your own class. Or cite GfG

class Node2c:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList2c:
	def __init__(self):
		self.head = None

	def reverse(self, head):
		if head is None or head.next is None:
			return head
		rest = self.reverse(head.next)
		head.next.next = head
		head.next = None
		return rest

	def __str__(self):
		linkedListStr = ""
		temp = self.head
		while temp:
			linkedListStr = (linkedListStr + str(temp.data) + " ")
			temp = temp.next
		return linkedListStr

	def push(self, data):
		temp = Node2c(data)
		temp.next = self.head
		self.head = temp



if __name__ == '__main__':

	linkedList = LinkedList2c()
	linkedList.push(10)
	linkedList.push(20)
	linkedList.push(30)
	linkedList.push(40)

	print("Original linked list : ")
	print(linkedList)

	linkedList.head = linkedList.reverse(linkedList.head)

	print("Reversed linked list : ")
	print(linkedList)


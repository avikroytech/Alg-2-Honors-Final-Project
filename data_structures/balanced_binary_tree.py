class Node():
	def __init__(self, left=None, right=None):
		if not left:
			left = Node()
		if not right:
			right = Node()
		self.left = left
		self.right = right

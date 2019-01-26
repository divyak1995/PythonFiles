class Node:
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

def depth(root):
	if root is None:
		return 0
	else:
		leftDepth=depth(root.left)
		rightDepth=depth(root.right)
		maxDepth=max(leftDepth,rightDepth)+1
		return maxDepth

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.left.left.left.left=Node(7)
print depth(root)

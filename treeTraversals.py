class Node:
  def __init__(self, value):
    self.value=value
    self.left=None
    self.right=None


#      1
#    2     3
#4     5


#tree traversals
# Inorder traversal -> L Root R
# 4 2 5 1 3
# Preorder traversal -> Root L R
#1 2 4 5 3
# Post order Traversal -> L R Root
# 4 5 2 3 1

def inorderTraversal(root):
  if root is not None:
    inorderTraversal(root.left)
    print(root.value,end=' ')
    inorderTraversal(root.right)

def preorderTraversal(root):
  if root is not None:
    print(root.value,end=' ')
    preorderTraversal(root.left)
    preorderTraversal(root.right)

def postorderTraversal(root):
  if root is not None:
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.value,end=' ')

#Level order Traversal
# 1 2 3 4 5

def levelOrderTraversal(root):
  queue=[]
  if root is None:
    return
  queue.append(root)
  while len(queue)>0:
    node=queue.pop(0)
    print(node.value,end=' ')
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)



root= Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

inorderTraversal(root)
print()
preorderTraversal(root)
print()
postorderTraversal(root)
print()
levelOrderTraversal(root)
print()

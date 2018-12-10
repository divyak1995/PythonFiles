class Node:
  def __init__(self, value):
    self.value=value
    self.left=None
    self.right=None

def traversal(root):
  if root is not None:
    traversal(root.left)
    print(root.value, end=' ')
    traversal(root.right)

def insert(root,node):
  if root is None:
    root=node
  else:
    if root.value < node.value:
      if root.right is None:
        root.right=node
      else:
        insert(root.right,node)
    if root.value > node.value:
      if root.left is None:
        root.left=node
      else:
        insert(root.left,node)

def minValueNode(node):
  current=node
  while current.left is not None:
    current=current.left
  return current

def deleteNode(root,key):
  if root is None:
    return None
  if key < root.value:
    root.left=deleteNode(root.left,key)
  elif key>root.value:
    root.right=deleteNode(root.right,key)
  else:
    if root.left is None:
      temp=root.right
      root=None
      return temp
    elif root.right is None:
      temp=root.left
      root=None
      return temp
    temp=minValueNode(root.right)
    root.value=temp.value
    root.right=deleteNode(root.right, temp.value)
  return root

root=Node(15)
root.left=Node(12)
root.right=Node(27)
root.left.left=Node(9)
root.left.right=Node(14)
root.right.left=Node(20)
root.right.right=Node(29)
traversal(root)
insert(root,Node(1))
print()
traversal(root)
deleteNode(root,1)
print()
traversal(root)

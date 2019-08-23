# Node is a class that has a constructor
# containing value of node, left and right rodes.
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class LinkedList:
  def __init__(self,head= None):
    self.head = head
    self.nxt = None

  def insertGivenNode(self, ll, new_node):
    if ll.head is None:
      new_node.nxt = new_node
      self.head  = new_node
      return ll

    elif ll.head.val > new_node.val:
      current = self.head
      while(current.nxt != self.head):
        # print(current.val)
        current = current.nxt
      last_node = current
      # print('last node is {}'.format(last_node.val))
      new_node.nxt = self.head
      last_node.nxt = new_node
      self.head = new_node
      return ll
    
    else:
      current = self.head
      while current.nxt.val < new_node.val:
        current = current.nxt
      next_node = current.nxt
      current.nxt = new_node
      new_node.nxt = next_node
      return ll

  def traverse(self, ll):
    current = self.head.nxt
    print(self.head.val)
    while(current != self.head):
      print(current.val)
      current = current.nxt
    print(current.val)


# Node and linkedlist are working.
# n1 = Node(7)
# n2 = Node(9)

# ll = LinkedList(n1)
# ll.nxt = n2
# print(ll.head.val)
# print(ll.nxt.val)


# Problem: Insert a given node into a sorted linked list

# Prerequisite: LL is already sorted list

# ll = LinkedList()
# new_node = Node(4)
# ll.insertGivenNode(ll, new_node)
# print(ll.head.val)


ll = LinkedList()
ll.head = Node(7)
ll.head.nxt = Node(9)
ll.head.nxt.nxt = Node(11)
ll.head.nxt.nxt.nxt = ll.head
new_node = Node(10)

output = ll.insertGivenNode(ll, new_node)
ll.traverse(output)

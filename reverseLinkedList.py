#Find middle node in a linked list:

class Node:
  def __init__(self,value):
    self.value=value
    self.nextl=None

class LinkedList:
  def __init__(self):
    self.head=None

  def traversal(self):
    temp=self.head
    if temp is None:
      return
    while(temp is not None):
      print(temp.value,end=' ')
      temp=temp.nextl

  def middleNode(self):
    a=self.head
    b=self.head
    while b and b.nextl:
      a=a.nextl
      b=b.nextl.nextl

    return a

  def reverse(self):
    prev=None
    current=self.head
    while(current is not None):
      nextNode=current.nextl
      current.nextl=prev
      prev=current
      current=nextNode
    self.head=prev

llist=LinkedList()
llist.head=Node(1)
llist.head.nextl=Node(2)
llist.head.nextl.nextl=Node(3)
llist.head.nextl.nextl.nextl=Node(4)
llist.traversal()
print()
mNode=llist.middleNode()
print(mNode.value)
llist.reverse()
llist.traversal()

  

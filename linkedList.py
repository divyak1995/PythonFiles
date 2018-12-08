#Linked list
# 1. create a linked list
# 2. Traverse a linked list
# 3. Add an element to a linked list
# 4. Remove an element from the linked list.
# 5. Remove duplicates from linked list

class Node:
  def __init__(self,value):
    self.value=value
    self.nextl=None

class linkedList:
  def __init__(self):
    self.head=None

  def traversal(self):
    temp=self.head
    while temp:
      print(temp.value,end=' ')
      temp=temp.nextl

  def append(self,element):
    last=self.head
    if self.head is None: 
        self.head = Node(element) 
        return
    while(last.nextl):
      last=last.nextl
    last.nextl=Node(element)
  
  def deleteNode(self, key):
    temp=self.head
    if temp.value==key:
      self.head=temp.nextl
      temp=None
    
    while(temp is not None):
      if temp.value== key:
        break
      prev=temp
      temp=temp.nextl

    if(temp==None):
      return

    prev.nextl=temp.nextl

llist = linkedList() 

llist.head  = Node(1) 
second = Node(2) 
third  = Node(3) 
llist.head.nextl = second; 
second.nextl = third; 
llist.traversal() 
print()
llist.append(4)
llist.traversal()
llist.deleteNode(1)
print()
llist.traversal()
llist.deleteNode(3)
print()
llist.traversal()


# Node class 
class Node: 
	def __init__(self, val): 
		self.val = val 
		self.next = None 

# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print temp.val, 
            temp = temp.next
  
		
    def middleElement(self):
        a=self.head
        b=self.head
        while b and b.next:
            a=a.next
            b=b.next.next
        return a.val
        
    def insert(self, newNode):
        last=self.head
        while last.next:
            last=last.next
        last.next= newNode
        
    def delete(self, deleteNode):
        n=self.head
        if n==deleteNode:
            self.head=n.next
        else:
            while n.next is not None:
                if deleteNode==n.next:
                    n.next=n.next.next
                    break
                

llist = LinkedList() 
llist.head = Node(1) 
second = Node(2) 
third = Node(3) 
fourth = Node(4)

llist.head.next = second;
second.next=third

print llist.middleElement()

llist.printList()

llist.insert(fourth)

print ''

llist.printList()

llist.delete(second)

print ''

llist.printList()





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


llist = LinkedList() 
llist.head = Node(1) 
second = Node(2) 
third = Node(3) 

llist.head.next = second;
second.next=third

print llist.middleElement()

llist.printList()




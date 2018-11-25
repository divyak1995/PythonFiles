class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def isSame(a,b):
    if a is None and b is None:
        return True
    elif a is not None and b is not None:
        return a.val==b.val and isSame(a.left,b.left) and isSame(a.right,b.right)
    else:
        return False
        
root1=Node(1)
root1.left=Node(2)
root1.right=Node(3)

root2=Node(1)
root2.left=Node(2)
root2.right=Node(5)

print isSame(root1,root2)

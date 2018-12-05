def mergeTwoSortedLists(a,b):
    n=len(a)
    m=len(b)
    res=[0]*(n+m)
    i=0
    j=0
    k=0
    while i < n and j < m: 
        if (a[i] <= b[j]): 
            res[k] = a[i] 
            i += 1
            k += 1
        else: 
            res[k] = b[j] 
            j += 1
            k += 1
              
    while (i < n):  
        res[k] = a[i] 
        i += 1
        k += 1
          
    while (j < m):  
        res[k] = b[j] 
        j += 1
        k += 1
    return res
    
def mergeKLists(li):
    n=len(li)
    if n==0:
        return None
    elif n==1:
        return li[0]
    elif n==2:
        return mergeTwoSortedLists(li[0],li[1])
    else:
        mid=n/2
        return mergeKLists([mergeKLists(li[:mid]), mergeKLists(li[mid:])])
        
        
# a=map(int,raw_input().split())
# b=map(int,raw_input().split())
k=int(raw_input())
li=[]
for i in range(k):
    li.append(map(int,raw_input().split()))

print mergeKLists(li)

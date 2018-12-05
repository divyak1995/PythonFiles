def mergeTwoSortedLists(a,b):
    if len(a)==0:
        return b
    elif len(b)==0:
        return a
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
            
    
a=map(int,raw_input().split())
b=map(int,raw_input().split())
c=mergeTwoSortedLists(a,b)
print c

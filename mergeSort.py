def mergeSort(li):
  if len(li)>1:
    mid=len(li)//2
    l=li[:mid]
    r=li[mid:]
    mergeSort(l)
    mergeSort(r)

    i=j=k=0
    while i< len(l) and j< len(r):
      if l[i]<r[j]:
        li[k]=l[i]
        i+=1
      else:
        li[k]=r[j]
        j+=1
      k+=1
        
    while i<len(l):
      li[k]=l[i]
      i+=1
      k+=1
    
    while j< len(r):
      li[k]=r[j]
      j+=1
      k+=1

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 

li=list(map(int,input().split()))
mergeSort(li)
printList(li)

  

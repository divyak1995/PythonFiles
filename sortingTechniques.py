#bubble sort
#Complexity O(N*N)
def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1]:
				temp=arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=temp

	return arr

#Selection sort
#Complexity O(N*N)
def selectionSort(arr):
	for i in range(len(arr)-1):
		for j in range(i+1,len(arr)):
			if arr[i] > arr[j]:
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp
	return arr

#merge sort
#complexity O(N*logN)
def mergeSort(arr):
	if len(arr)>1:
		mid=len(arr)/2
		left= arr[0:mid]
		right=arr[mid:]
		mergeSort(left)
		mergeSort(right)

		i=0
		j=0
		k=0
		while i< len(left) and j<len(right):
			if left[i] <= right[j]:
				arr[k]=left[i]
				i+=1
			else:
				arr[k]=right[j]
				j+=1
			k+=1

		if i<len(left):
			arr[k]=left[i]
			i+=1
			k+=1

		if j<len(right):
			arr[k]=right[j]
			j+=1
			k+=1
	return arr

def quickSort(arr):
	lesser=[]
	greater=[]
	equal=[]
	if len(arr)>1:
		pivot=arr[0]
		for i in arr:
			if i < pivot:
				lesser.append(i)

			elif i == pivot:
				equal.append(i)

			else:
				greater.append(i)

		return quickSort(lesser)+equal+quickSort(greater)
	else:
		return arr

def insertionSort(arr):
	for i in range(1,len(arr)):
		key=arr[i]
		for j in range(i-1,0,-1):
			if key < arr[j]:
				arr[i]=temp
				temp=arr[j]
				arr[j]=temp

	return arr



arr=[19,7,3,1,3,24]
b=bubbleSort(arr)
s=selectionSort(arr)
print 'Bubble sort is '
print b
print 'Selection sort is'
print s
print 'merge sort is'
m=mergeSort(arr)
print m
print 'quick sort is'
q=quickSort(arr)
print q
print 'Insertion sort is '
i=insertionSort(arr)
print i

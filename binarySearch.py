# 2 4 5 6 7 8 10
# Search 5

def binarySearch(arr,searchElement):
	low=0
	high=len(arr)-1
	while low <=high:
		mid=low+(high-low)/2
		if arr[mid]==searchElement:
			return mid
		elif searchElement > arr[mid]:
			low=mid+1
		else:
			high=mid-1

	return -1



print 'Enter the list of elements'
array= map(int,raw_input().split())
array.sort()
print 'Enter the element that is to be searched'
searchElement=int(raw_input())
result=binarySearch(array, searchElement)
if result==-1:
	print 'Element not found'
else:
	print '%d is at postion %d' %(searchElement,result)

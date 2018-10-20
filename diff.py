def dictFun(A):
	dictA={}
	for element in A:
		if element not in dictA:
			dictA[element]=1
		else:
			dictA[element]+=1
			
	return dictA
		
def diff(A,B):
	dictA=dictFun(A)
	dictB=dictFun(B)
	dictCopy={}
	a=list()
	b=list()
	print dictA
	print dictB
	
	setA=set(A)
	setB=set(B)
	for key in setA:
		if key not in dictB.keys():
			a.append(key)
		else:
			diffValue=dictA[key]-dictB[key]
			if diffValue>0:
				for i in range(diffValue):
					a.append(key)
		
	print a
			
			
	for key in setB:
		if key not in dictA.keys():
			b.append(key)
		else:
			diffValue=dictB[key]-dictA[key]
			if diffValue>0:
				for i in range(diffValue):
					b.append(key)
					
	print b
	
A=["apple","apple","banana"]
B=["apple","banana","orange","grapes"]
diff(A,B)
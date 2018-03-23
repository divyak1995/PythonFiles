class Rectangle:
	def __init__(self,width,length):
		self.__width=width
		self.__length=length
		self.__area=self.__width*self.__length

	def __add__(self,rectangle):
		return Rectangle(self.__width+rectangle.__width,self.__length+rectangle.__length)

	def __str__(self):
		return "The Area is %d" %self.__area;

r1=Rectangle(1,3)
r2=Rectangle(1,5)
r2=r1+r2

print(r1)
print(r2)
print(r3)
print('Enter a string:')
st=input()
uniqueChars=set(st)
li=[]
for char in st:
  li.append(char)
if sorted(li) == sorted(list(uniqueChars)):
  print('The characters of string are unique')
else:
  print('The characters of string are not unique')

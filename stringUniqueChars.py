# CHECK THAT THE STRING HAS ALL UNIQUE CHARS

s=raw_input()
d={}
for char in s:
    if char not in d:
        d[char]=1
    else:
        d[char]+=1
        
for value in d.values():
    if value > 1:
        print False
        exit()
        
print True

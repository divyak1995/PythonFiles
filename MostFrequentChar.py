def MostFrequentChar(s):
    if len(s)>0:
        d=dict()
        for char in s:
            if char not in d:
                d[char]=1
            else:
                d[char]=d[char]+1
        val=list(d.values())
        k=list(d.keys())
        maxValue=max(val)
        lis=list()
        for i in k:
            if d[i]==maxValue:
                lis.append(i)

        filt=dict()
        for char in lis:
            
            filt[char]=s.index(char)
        
        v=min(filt.values())
        for k in filt.keys():
            if filt[k]==v:
                return k


while True:
    st = str(raw_input('String>> ').strip())
    if len(st)==0:
        print 'Please enter a string'
    else:
        break
        

print 'Most Frequent Character in '+st+' is '+MostFrequentChar(st)



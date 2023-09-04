d={'A':1,'D':2,'C':3}
tup=sorted(d.items())
print(tup)

#Clean Print without parenthesis
for k,v in sorted(d.items()):
    print(k,v)
#sorted by values instead of key
d={'A':1,'D':2,'C':3}
tmp=list()

for k,v in d.items():
    tmp.append( (v,k))
print('result using append : ',tmp)

#sorted tmp
tmp=sorted(tmp,reverse=True)
print(tmp)
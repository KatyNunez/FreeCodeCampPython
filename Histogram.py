count={}
names=['katy','yeika','yoel','katy','yeika']



for name in names:
    if name not in count:
        count[name]=1
    else:
        count[name]=count[name]+1

for name in names:
 x= count.get(name,0)

print(count)
print('Result using get: ',x)


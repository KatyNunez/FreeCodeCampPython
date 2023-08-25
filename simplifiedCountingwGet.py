counts=dict()
names=['katy','yeika','yoel','yoel']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))
n=5 #interaction variable
while n>0:
    print(n)
    n=n-1
print('blastoff')
print (n)

# break an infinite loop
while True:
    line= input('>')
    if line=='done' :
        break
    print(line)
print ('done')
#infinite loop with continue

while True:
    line = input('>')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('done!')

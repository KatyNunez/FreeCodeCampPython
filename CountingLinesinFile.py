FileAccess=open('stuff.txt')
LineCounter=0

for line in FileAccess:
    if '\n' in line:
        LineCounter+=1
print("There are : ",LineCounter, " Lines")

OpenFile=open('stuff.txt')
for line in OpenFile:
    if not '1' in line: # scan each line to find the ones that contains '1'
        continue
    print(line.rstrip())
# this program look the lines that starts with 'l' in a file
OpenFile=open('stuff.txt')
for line in OpenFile:
    line=line.rstrip()# this is to avoid white space and the \n
    if line.startswith('l'):
        print(line)
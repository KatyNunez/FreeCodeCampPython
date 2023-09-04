
import re # libreria de regular expresion
OpenFile=open('stuff.txt')
for line in OpenFile:
    line=line.rstrip()
    if re.search('^From:',line):
        print(line)


"""""""""
OpenFile=open('stuff.txt')
for line in OpenFile:
    line=line.strip()
    if line.find('From:')>=0:
        print(line)
"""""""""""
import re # libreria de regular expresion
OpenFile=open('stuff.txt')
for line in OpenFile:
    line=line.strip()
    if re.search('From:',line):
        print(line)
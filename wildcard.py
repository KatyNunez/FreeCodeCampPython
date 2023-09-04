import re
OpenFile=open('stuff.txt')
for line in OpenFile:
    line=line.strip()
    if re.search('^X-Sieve*',line):
        print(line)

for line in OpenFile:
    line=line.strip()
                     #match any non-whitespace character
    if re.search('^X.-\S+:',line):
        print(line)
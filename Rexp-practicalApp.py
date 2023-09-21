# Regular expression practical application
import re
openFile=open('stuff.txt')
numlist=list()
for line in openFile:
    line=line.rstrip()
    Search=re.findall('^X-DSPAM-Result: ([0-9.]+)',line)

    if len(Search)!=1: continue
    num=float(Search[0])
    numlist.append(num)
print('maximum', max(numlist))
print('minimum', min(numlist))
     
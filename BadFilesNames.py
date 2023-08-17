FileName=input("Enter a file name : ")
try:
    OpenFile=open(FileName)

except:
    print('File cannot be openned : ',FileName)
count=0
for line in OpenFile:
    if line.startswith('P'):
        count+=1
print('There were ', count, 'p lines in ', FileName)
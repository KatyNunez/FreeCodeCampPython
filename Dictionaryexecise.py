counts =dict()
print('enter a line of text: ')
line=input('')
print(line) #string 
words=line.split() #dictionario divide into word

print('Counting')
for word in words:
    counts[word]=counts.get(word,0)+1
print('counts', counts)
#it is not recommended to have a string variable with a lot of data in it

OpenFile= open('stuff.txt')
ReadFile=OpenFile.read()# go to the whole file and put it all on the variable.
print(ReadFile)
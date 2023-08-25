Num=list()

while True:
    option=input('Enter Number : ') # this is a str type
    if option=='done': break
    value=float(option) #convert str to float
    Num.append(value)
average=sum(Num)/len(Num)
print(average)

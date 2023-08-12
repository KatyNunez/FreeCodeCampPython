"""""""""
print('before')
for thing in [1,2,3,4,5,6,7,8,9]:
    print(thing)
print('after')
"""""""""""
#find the largest/ smaller number 

print('before')
High_Num=None
Low_Num=None

for thing in [1000,2,3,4,5,6,7,8,9,100]: 
    if High_Num is None or thing> High_Num:
        High_Num=thing

    if Low_Num is None or thing< Low_Num:
        Low_Num=thing
       
    
print('The largest number is : ',High_Num)
print('The lower number is   : ',Low_Num) 

print('after')



def sum(a,b):
    suma=int(a)+int(b)

    return suma

dic=dict()
op=None

while True:
    if op==None or op=='c':
        key=input('Enter key: ')
        value=input('Enter value: ')
        op=input('salir(s)/(c)')
        dic[key]=value
        continue
    if op=='s':
        print('close')
        break
print(dic)
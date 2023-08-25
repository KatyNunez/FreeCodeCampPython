a=[]
cond=""
name=""
while True:
        if cond!='s':
         name=input("Nombre : ")
         a+=[name] 
         cond=input('desea salir presiona s')

        if cond=='s': break
print(a)
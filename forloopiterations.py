"""""""""
print('before')
for thing in [1,2,3,4,5,6,7,8,9]:
    print(thing)
print('after')
"""""""""""

def saberSiEsPrimo(num):

    resultado = None 
    cont=0
    for i in range(1,num+1):
        if num % i==0:
            cont=cont+1
    if cont==2:
     resultado=elNumEsPrimo = "El numero ",num," es primo"
    else:
     resultado=elNumNoEsPrimo = "El numero",num," NO es primo" 

    #Implementar logica para usando for, saber si mi numero se encuentra en el array

    return resultado

def encuentraNumero(array,numeroAbuscar):
    numeroEncontrado = None
    #Implementar logica para usando for, saber si mi numero se encuentra en el array
    for a in array:
        if numeroAbuscar==a:
            numeroEncontrado=True
    
    return numeroEncontrado
        



print("----------------------------")
print("Verifica si es primo")
print(saberSiEsPrimo(4))

print("----------------------------")
print("Verifica si el numero esta dentro del array:")
print(encuentraNumero([10,8,56,8,7,9],15))


#find the largest/ smaller number 

"""""""""
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

"""""






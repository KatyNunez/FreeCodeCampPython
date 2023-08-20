#FUNCION PARA ENCRIPTAR y DESENCRIPTAR
"""""
Debes de crear la logica para la funcion encriptar y desencriptar.

Para eso recibiras el texto, y la clave para encriptarlo.

el resultado debe de ser un texto completamente diferente al original, y que solo se pueda leer con la clave.

ejemplo: texto: "Hola shaiza" ---> "x4w4 x14gg" ---> clave "12345"

para desecriptarlo seria: textoEncriptado: "x4w4 x14gg" ----> clave "12345" ---> resultado "Hola shaiza"

"""""
import os
#clean screen
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



def ENCRIPTAR(texto, clave):
# Variables 
    textoascii=[]
    claveascii=[]
    sumclave=0
    claveop=0
    txtenc=[]

# Process 
    textosp=""
    for i in texto:
     textoascii.append(ord(i)) # converted text to ascii code

    for x in clave:
     claveascii.append(ord(x)) # converted clace to ascii code
     
    for m in claveascii:
       sumclave+=m            # sum of the ascci clave
    
    for k in textoascii:
      claveop=k+sumclave     # sum each text-code-ascii with the sum of clave
      txtenc.append(chr(claveop)) # save the encrypted text
      cleartxt = ''.join(txtenc)

# Output    
    return cleartxt
  
       

def DESENCRIPTAR(textoEncriptado, clave):

#declaration
    suma=0
    resta=0
    clavede=0
    txtdec=0
    txtencascii=[]
    resultados = []
# process
    for x in clave:
     clavede=ord(x)
     suma+=clavede
    
    for t in textoEncriptado:
       txtencascii.append(ord(t)) # arreglo para convertir a ascii
    
#descencriptado
    for x in txtencascii:
     resta = x - suma
     resultados.append(chr(resta))
 
    cleartext = ''.join(resultados)
  
    return cleartext    

 


#ENCRIPTAR

texto=input("texto : ")
clave=input("Clave : ")
clear()
print("Texto encriptado: ",ENCRIPTAR(texto, clave))

#DESENCRYPTAR"
textoEncriptado=input("Texto encriptado : ")

clave_prueba=input("Clave : ")
print("Texto desencriptado: ",DESENCRIPTAR(textoEncriptado,clave_prueba,))


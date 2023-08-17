#FUNCION PARA ENCRIPTAR y DESENCRIPTAR
"""""
Debes de crear la logica para la funcion encriptar y desencriptar.

Para eso recibiras el texto, y la clave para encriptarlo.

el resultado debe de ser un texto completamente diferente al original, y que solo se pueda leer con la clave.

ejemplo: texto: "Hola shaiza" ---> "x4w4 x14gg" ---> clave "12345"

para desecriptarlo seria: textoEncriptado: "x4w4 x14gg" ----> clave "12345" ---> resultado "Hola shaiza"

"""""


def ENCRIPTAR(texto, clave):
    textoEncriptado= ""
    if 'a' in texto:
        texto=texto.replace('a','!11')
    if 'e' in texto:
        texto=texto.replace('e','@22')

    if 'i' in texto:
        texto=texto.replace('i','#33')
    if 'o' in texto:
        texto=texto.replace('o','$44')

    if 'u' in texto:
        texto=texto.replace('u','%55')

    for i in range (len(texto)-1,-1,-1): # change the order of the string
        textoEncriptado+=(texto[i].strip())

        
    return textoEncriptado


def DESENCRIPTAR(textoEncriptado,clave_prueba, clave,TextoOriginal):
    textoDesencritpado= ""
    
    for i in range (len(textoEncriptado)-1,-1,-1): #Change the order of the string,; back to normal 
      textoDesencritpado+=(textoEncriptado[i].strip())

    if clave_prueba==clave:
        if '!11' in textoDesencritpado:
             textoDesencritpado=textoDesencritpado.replace('!11','a')
        if '@22' in textoDesencritpado:
              textoDesencritpado=textoDesencritpado.replace('@22','e')

        if '#33' in textoDesencritpado:
              textoDesencritpado=textoDesencritpado.replace('#33','i')

        if '$44' in textoDesencritpado:
              textoDesencritpado=textoDesencritpado.replace('$44','o')

        if '%55' in textoDesencritpado:
             textoDesencritpado=textoDesencritpado.replace('%55','u')
    else:
       print("wrong password, Run the program again") 
       quit() #it stops the program from running
       
      
    if textoDesencritpado!=TextoOriginal:
        textoDesencritpado= ''.join(TextoOriginal) # join the differences between both string in this case the spaces
    
    
    return textoDesencritpado


#ENCRIPTAR
texto=input("texto : ")
clave=input("Clave : ")
TextoOriginal=texto
print("Texto encriptado: ",ENCRIPTAR(texto, clave))

#DESENCRYPTAR
textoEncriptado=input("texto : ")
clave_prueba=input("Clave : ")

print("Texto desencriptado: ",DESENCRIPTAR(textoEncriptado,clave_prueba,clave,TextoOriginal))


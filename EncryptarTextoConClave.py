#FUNCION PARA ENCRIPTAR y DESENCRIPTAR
"""""
Debes de crear la logica para la funcion encriptar y desencriptar.

Para eso recibiras el texto, y la clave para encriptarlo.

el resultado debe de ser un texto completamente diferente al original, y que solo se pueda leer con la clave.

ejemplo: texto: "Hola shaiza" ---> "x4w4 x14gg" ---> clave "12345"

para desecriptarlo seria: textoEncriptado: "x4w4 x14gg" ----> clave "12345" ---> resultado "Hola shaiza"

"""""

def ENCRIPTAR(texto, clave):
    textoEncritpado= ""

    return textoEncritpado


def DESENCRIPTAR(textoEncriptado, clave):
    textoDesencritpado= ""

    return textoDesencritpado

#ENCRIPTAR
texto=input("texto : ")
clave=input("Clave : ")

print("Texto encriptado: ",ENCRIPTAR(texto, clave))

#DESENCRYPTAR
textoEncriptado=input("texto : ")
clave=input("Clave : ")

print("Texto desencriptado: ",DESENCRIPTAR(textoEncriptado, clave))


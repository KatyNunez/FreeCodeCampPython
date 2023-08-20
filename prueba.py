numeros="1 2 3"
p=1
b=0
# Divide la cadena en una lista de números usando la coma como separador
for x in numeros:
 numeros = numeros.split(" ")
 print(numeros)

# Inicializa una lista vacía para almacenar los resultados
resultados = []

for x in numeros:
    b = int(x) + p
    resultados.append(b)

print(resultados)  # Esto imprimirá [2, 3, 4]
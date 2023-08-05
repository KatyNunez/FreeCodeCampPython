temp = "5 degrees"
cel = 0

try:
    # Código que puede generar una excepción
    fahr = float(temp) 
    cel = (fahr - 32.0) * 5.0 / 9.0

except Exception as e:
    # Este bloque se ejecutará si ocurre cualquier otra excepción
    print("Se ha producido un error no esperado.")
    print(f"Detalles del error: {e}")
finally :
    print(cel)

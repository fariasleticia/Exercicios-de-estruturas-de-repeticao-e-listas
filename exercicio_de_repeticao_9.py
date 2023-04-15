lista_numeros_impares = []

for numero in range(1, 50):
    if numero%2 != 0:
        lista_numeros_impares.append(numero)

print("Números ímpares de 1 a 50: " + str(lista_numeros_impares))

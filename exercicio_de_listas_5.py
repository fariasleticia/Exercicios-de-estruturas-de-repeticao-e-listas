todos_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numeros_pares = []
numeros_impares = []

for valor in todos_numeros:
    if valor%2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

print('Todos os números:', todos_numeros)
print('Números pares:', numeros_pares)
print('Números ímpares:', numeros_impares)

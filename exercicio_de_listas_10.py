letras_bacanas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numeros_bacanas = [2, 4, 6, 8, 1, 3, 5, 7, 9, 0]
letras_e_numeros = []

for elemento in range(10):
    letras_e_numeros.append(letras_bacanas[elemento])
    letras_e_numeros.append(numeros_bacanas[elemento])

print("Letras bacaníssimas:", letras_bacanas)
print("Números legaizinhos:", numeros_bacanas)
print("Listas intercaladas:", letras_e_numeros)

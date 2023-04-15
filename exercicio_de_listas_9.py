numeros_super_legais = [7, 8, 4, 10, 28, 4, 9, 11, 2, 13]
numeros_ao_quadrado = []

for numero in numeros_super_legais:
    n_quadrado = numero ** 2
    numeros_ao_quadrado.append(n_quadrado)

soma = sum(numeros_ao_quadrado)

print("Números legais:", numeros_super_legais)
print("Números ao quadrado:", numeros_ao_quadrado)
print("Soma dos quadrados:", soma)
numeros_bonitos = [3, 6, 33, 66, 999]
soma = 0
media = 0

for numero in numeros_bonitos:
    soma = soma + numero
    media = soma / len(numeros_bonitos)

print("Meus números de arrasar:", numeros_bonitos)
print("Soma bunita = " + str(soma))
print("Média lindinha = " + str(media))

numero_inserido1 = int(input("Ei!\nDigita um número aí: "))
numero_inserido2 = int(input("Agora digita mais um: "))
print("Valeu <3\nEsses são seus números: " + str(numero_inserido1) + " e " + str(numero_inserido2) + ".")

numeros_entre = []

while numero_inserido2 != numero_inserido1:
    if numero_inserido1 < numero_inserido2:
        numero_inserido1 = numero_inserido1 + 1
        numeros_entre.append(numero_inserido1)
    elif numero_inserido1 > numero_inserido2:
        numero_inserido2 = numero_inserido2 + 1
        numeros_entre.append(numero_inserido2)
numeros_entre.pop()

print("Esses são os números existentes entre os valores inseridos:", numeros_entre)

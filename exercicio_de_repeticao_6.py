numero = 0
lista_de_numeros = []

print("Lista em pé:")
for numero in range (0, 20):
    numero = numero + 1
    print(numero)

print("Lista deitada:")
for numero in range (0, 20):
    numero = numero + 1
    lista_de_numeros.append(numero)

print(lista_de_numeros)

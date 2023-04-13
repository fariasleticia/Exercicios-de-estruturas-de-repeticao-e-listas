idade_dos_carinhas = []
idade_invertida = []

altura_dos_carinhas = []
altura_invertida = []

print("Insira 5 idades legais abaixo:")
for idade in range(0,5):
    idade_dos_carinhas.append(input())

for i in range (0, 5):
    idade_invertida.append(idade_dos_carinhas.pop())
print("Lista de idades (ao contrário):", idade_invertida)

print("Insira 5 alturas mais legais ainda abaixo:")
for altura in range (0, 5):
    altura_dos_carinhas.append(input())

for i in range (0, 5):
    altura_invertida.append(altura_dos_carinhas.pop())
print("Lista de alturas (ao contrário também):", altura_invertida)

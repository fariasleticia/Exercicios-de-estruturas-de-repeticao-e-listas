notas = [7, 8, 9, 10]
print('Notas da galerinha:', notas)

quantidade = len(notas)
soma = 0

for valores in notas:
    soma = soma + valores

print('Média das notas da galerinha:', soma/quantidade)

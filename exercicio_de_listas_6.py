notas_da_turminha = [['Aluna 1', [2, 5, 7, 9]], ['Aluna 2', [4, 6, 8, 8.5]], ['Aluna 3', [7, 7.5, 8, 9]], ['Aluna 4', [9, 9.5, 10, 10]], ['Aluna 5', [9.5, 8.5, 7, 9]], ['Aluna 6', [10, 7, 9, 9.5]], ['Aluna 7', [10, 10, 9, 8]], ['Aluno 8', [5, 6, 4, 4]], ['Aluna 9', [6, 8, 8.5, 7]], ['Aluna 10', [3.5, 6, 2, 8]]]

soma = 0

for alunas in notas_da_turminha:
    for nota_individual in alunas:
        soma = soma + nota_individual
    media = soma/len(alunas)

#aaaaaaaaaaaaaaaahhhhhhhhhhhh
#falta imprimir *apenas* os valores acima de 7.0

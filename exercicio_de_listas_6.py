notas_da_turminha = [['Aluna 1', [2, 5, 7, 9]], ['Aluna 2', [4, 6, 8, 8.5]], ['Aluna 3', [7, 7.5, 8, 9]], ['Aluna 4', [9, 9.5, 10, 10]], ['Aluna 5', [9.5, 8.5, 7, 9]], ['Aluna 6', [10, 7, 9, 9.5]], ['Aluna 7', [10, 10, 9, 8]], ['Aluna 8', [5, 6, 4, 4]], ['Aluna 9', [6, 8, 8.5, 7]], ['Aluna 10', [3.5, 6, 2, 8]]]
aprovadas = []

def calcular_medias (notas_da_turminha, aprovadas):
    media = 0
    for aluna in notas_da_turminha:
        media = sum(aluna[1]) / len(aluna[1])
        if media >= 7.0:
            aprovadas.append(media)
            print(aluna[0], "aprovada com média:", media)
        else:
            print(aluna[0], "reprovada com média:", media)

calcular_medias(notas_da_turminha, aprovadas)

print("Número de aprovadas:", len(aprovadas))
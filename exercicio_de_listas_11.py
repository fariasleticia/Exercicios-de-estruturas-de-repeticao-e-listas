numeros_bacanas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
letras_bacanas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
palavras_bacanas = ["amor", "baixinho", "coração", "docinho", "elefante", "feijão", "gente", "humano", "igualdade", "juventude"]
letras_e_numeros_e_palavras = []

for elemento in range(10):
    letras_e_numeros_e_palavras.append(numeros_bacanas[elemento])
    letras_e_numeros_e_palavras.append(letras_bacanas[elemento])
    letras_e_numeros_e_palavras.append(palavras_bacanas[elemento])


print("Números legaizinhos:", numeros_bacanas)
print("Letras bacaníssimas:", letras_bacanas)
print("Palavras maneiríssimas:", palavras_bacanas)
print("Listas intercaladas:", letras_e_numeros_e_palavras)

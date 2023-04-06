palavra_maneira = ['m', 'e', 'l', 'a', 'n', 'c', 'o', 'l', 'i', 'a']
vogais = ['a', 'e', 'i', 'o', 'u']

numero_consoantes = 0

for letras in palavra_maneira:
    if letras not in vogais:
        numero_consoantes = numero_consoantes + 1
        print(letras)

print('Total de consoantes:', numero_consoantes)

validade_nota = False

while validade_nota == False:
    print ("Insira uma nota de 0 a 10:")
    entrada_numero = float(input())
    if entrada_numero >= 0 and entrada_numero <= 10:
        print ("Valeu carinha :)")
        validade_nota = True        
    else:
        print ("Eu disse de 1 a 10 carinha >:(")

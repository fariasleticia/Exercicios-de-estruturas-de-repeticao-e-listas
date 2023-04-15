def calculos_irados_competicao_cresc_paises():
    validade_paisA = False
    while validade_paisA == False:
        print("Insira o número total da população do país Abacate:")
        entrada_paisA = float(input())
        if entrada_paisA > 0:
            print ("Ok!")
            validade_paisA = True        
        else:
            print ("Este não é um valor válido.")

    validade_taxaA = False
    while validade_taxaA == False:
        print("Insira a taxa de crescimento da população abacateira (em decimais):")
        entrada_taxaA = float(input())
        if entrada_taxaA > 0:
            print ("Ok!")
            validade_taxaA = True        
        else:
            print ("Este não é um valor válido.")

    validade_paisB = False
    while validade_paisB == False:
        print("Insira o número total da população do país Bolinho:")
        entrada_paisB = float(input())
        if entrada_paisB > 0:
            print ("Ok!")
            validade_paisB = True        
        else:
            print ("Este não é um valor válido.")

    validade_taxaB = False
    while validade_taxaB == False:
        print("Insira a taxa de crescimento da população bolinhos (em decimais):")
        entrada_taxaB = float(input())
        if entrada_taxaB > 0:
            print ("Ok!")
            validade_taxaB = True
        else:
            print ("Este não é um valor válido.")

    ano = 0
    while entrada_paisB > entrada_paisA:
        ano = ano + 1
        entrada_paisA = entrada_paisA * (entrada_paisA + 1)
        entrada_paisB = entrada_paisB * (entrada_paisB + 1)
    print("Estes são os anos necessários para que a população abacate ultrapasse a bolinho:", ano)

parar_programa = False

while parar_programa == False:
    print("Olá viajante (que só dificulta minha vida)!")
    calculos_irados_competicao_cresc_paises()
    print("Legal! Quer fazer isso de novo? Insira 'sim' ou 'não'.\n(fala não)")
    repetir_processo = input()
    if repetir_processo == 'não' or repetir_processo == 'nao':
        print("MUITO OBRIGADA! :D")
        parar_programa = True

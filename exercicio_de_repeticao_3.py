print("Olá! Por favor, insira as seguintes informações.")

validade_nome = False
while validade_nome == False:
    print("Insira seu nome (mais de 3 letras):")
    entrada_nome = input()
    if len(entrada_nome) > 3:
        print ("Maneiro ;)")
        validade_nome = True        
    else:
        print ("Opa! Siga as instruções novamente.")

validade_idade = False
while validade_idade == False:
    print("Insira sua idade:")
    entrada_idade = float(input())
    if entrada_idade > 0 and entrada_idade < 150:
        print ("Okay!")
        validade_idade = True        
    else:
        print ("Esse número é impossível coleguinha. Tente novamente!")

validade_salario = False
while validade_salario == False:
    print("Insira seu salário:")
    entrada_salario = float(input())
    if entrada_salario > 0:
        print ("Joinha :)")
        validade_salario = True        
    else:
        print ("Só finge que você tem dinheiro cara.")

validade_genero = False
generos = ["F", "M", "N", "O", "f", "m", "n", "o"]
while validade_genero == False:
    print("Insira seu gênero ('F' para feminino, 'M' para masculino, 'N' para não-binário e ou 'O' para vários/outros):")
    entrada_genero = input()
    if entrada_genero in generos:
        print ("Legal <3")
        validade_genero = True        
    else:
        print ("Por favor, escolha uma das opções disponíveis.")

validade_estado_civil = False
estado_civil = ["S", "C", "V", "D", "s", "c", "v", "d"]
while validade_estado_civil == False:
    print("Insira seu estado civil ('S' para solteira/o, 'C' para casada/o, 'V' para viúva/o e ou 'D' para divorciada/o):")
    entrada_estado_civil = input()
    if entrada_estado_civil in estado_civil:
        print ("Isso aí <3")
        validade_estado_civil = True        
    else:
        print ("Não sei pra que essa informação serve, mas POR FAVOR, tente de novo.")

print("Seus dados foram registrados com sucesso! Cuidado :)")

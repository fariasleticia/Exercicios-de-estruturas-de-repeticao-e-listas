validade_senha = False

while validade_senha == False:
    print("Insira um usuário maneiro:")
    entrada_usuario = input()
    print("Beleza!")
    print("Insira uma senha maneira (não pode ser igual ao usuário):")
    entrada_senha = input()
    if entrada_usuario != entrada_senha:
        print ("Isso aí carinha :)")
        validade_senha = True        
    else:
        print ("Tá errado! Siga as instruções novamente.")

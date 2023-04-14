paisA = 80000
taxaA = 0.03

paisB = 200000
taxaB = 0.015

ano = 0

while paisB > paisA:
    ano = ano + 1
    paisA = paisA * (taxaA + 1)
    paisB = paisB * (taxaB + 1)

print("São precisos", ano, "anos.")

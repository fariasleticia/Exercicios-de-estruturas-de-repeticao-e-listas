listinha_show = [-51, -999, -6, -23, -47]
numero_grande = listinha_show[0]
quantd = 0

while quantd < len(listinha_show):
    if listinha_show[quantd] > numero_grande:
        numero_grande = listinha_show[quantd]
    quantd = quantd + 1

print("Saca só a listinha show:" + str(listinha_show))
print ("O maior número é", numero_grande)

#ou, do jeito mais simples: print(max(listinha_show))
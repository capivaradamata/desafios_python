lista = ("Lápis", 1.50, "Borracha", 3.00, "Caderno", 10.00, "Tesoura", 15.00, "Apontador", 6.50, "Caneta" , 3.50)
#print(f"------------------------------------ \ndadasd", sep="\n"  )
contagem = 0
preço = 1
tamanho = int(len(lista))
for c in range(40):
    print("-", end="")
print("")
for x in lista:
    print(f"{lista[int(contagem)]}", end="" )
    for z in range(0, 40 - (len(lista[int(contagem)]))):
        print(".", end="")
    print(f"R$ {lista[preço]}")
    contagem += 2
    preço += 2
    if contagem > 10:
        break

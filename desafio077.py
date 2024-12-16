
lista = ("Caneta", "Mochila", "Apagador", "lapis", "Caderno")
contagem = 0
print(f"A palavra ", end="")

for c in lista:
    print(f"{c} tem as vogais", end=" ")
    if c.find("a") != -1:
        letra_a = "A"
        print(f"{letra_a}", end=" ")

    if c.find("e")!= -1:
       letra_e = "E"
       print(letra_e, end=" ")

    if c.find("i")!= -1:
        letra_i = "I"
        print(letra_i, end=" ")

    if c.find("o")!= -1:
        letra_o = "O"
        print(letra_o, end=" ")

    if c.find("u")!= -1:
        letra_u = "U"
        print(letra_u)
    print(sep="/n")
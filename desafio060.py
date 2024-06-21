nun = int(input("informe o numero que deseja saber o fatorial:"))
inicial = nun
contagem = nun
resultado = nun
fator = nun - 1
while contagem != 0:
    contagem = contagem - 1
    print(contagem)
    resultado = resultado * (fator)
    fator = fator -1
    if fator == 0:
        fator = 1
    print(resultado)
print(f"o Fatorial de {inicial} é {resultado}")
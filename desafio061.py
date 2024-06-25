print("informa os primeiro termo e a razão da progressão aritimética")
resultado = int(input("Primeiro termo:"))
razão = int(input("Razão:"))
contagem = 0
while contagem != 10:
    contagem += 1
    resultado = resultado + razão
    print(f"{resultado}", end=";")
print("Você gostaria de ver mais termos? S/N")
resposta = str(input("Você gostaria de ver mais termos? Digite S/N")).upper()
quantidade = int(input("Quanto termos a mais?"))
total = 0
if resposta == "S":
    print("Esse são os proximos termos")
    while total != quantidade:
        total += 1
        resultado = resultado + razão
        print(f"{resultado}", end=":")
else:print("Obriado!")
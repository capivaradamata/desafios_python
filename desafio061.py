print("informa os primeiro termo e a razão da progressão aritimética")
resultado = int(input("Primeiro termo:"))
razão = int(input("Razão:"))
contagem = 0
while contagem != 10:
    contagem += 1
    resultado = resultado + razão
    print(f"{resultado}", end=";")

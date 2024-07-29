print("Cadastre o produto")
total = maior = 0
barato = 1000000000
while True:
    produto = str(input("Nome do produto:"))
    preço = int(input("Preço: R$"))
    total += preço
    if preço > 1000:
        maior += 1
    if preço < barato:
        barato = preço
    seguir = str(input("Quer continuar?S/N")).upper()
    while True:
        if seguir != "N" and seguir != "S":
            seguir = str(input("Quer continuar?S/N")).upper()
        else: break
    if seguir == "N":
        break
print(f"O total da compra foi {total}, existem {maior} produtos de mais de R$1000,00 , o produto mais barato custa {barato}")
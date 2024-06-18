print("Você informara 5 pesos para saber quais são o maior e o menor peso")
menor = 10000
maior = 0
cont= 0
for c in range(0,5,1):
    cont += 1
    peso = float(input(f"Informe o peso da {cont}° pessoa:"))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print(f"o maior peso é {maior} e o menor peso é {menor}")
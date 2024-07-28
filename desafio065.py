print("Informe os numeros que deseja saber a média, o maior e o menor.")
contagem = 0
total = 0
fim = 0
menor = 1000000000
maior = 0
while fim != 1:
    contagem += 1
    soma = int(input("Informe o numero:"))
    total += soma
    resultado = total/contagem
    if soma < menor:
        menor = soma
    if soma > maior:
        maior = soma
    cont = str(input("Deseja continuar?S/N")).upper()
    if cont == "N":
        fim = 1
print(f"A média foi {resultado},o maior numero foi {maior} o menor foi {menor}")
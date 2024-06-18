numero = int(input('Digite um numero:'))
numero2 = int(input('Digite outro:'))
numero3 = int(input('outro novamente:'))
menor = numero
if numero2<numero and numero2<numero3:
    menor = numero2
if numero3<numero  and numero3<numero2:
    menor = numero3

maior = numero
if  numero2>numero and numero2>numero3:
    maior = numero2
if numero3>numero and numero3>numero2:
    maior = numero3
    print(f'o maior numero é {maior}')
print(f'o menor numero é {menor}')
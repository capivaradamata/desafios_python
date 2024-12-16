import random
maior = 0
menor = 1000
for numero in range(0,5):
    numero = random.randint(0, 100, )
    lista = (numero)
    print(f"{lista}" , end =" ")
    if maior < numero:
        maior = lista
    if menor > numero:
        menor = numero
print("")
print(f"O maior numero é {maior}")
print(f"O menor numero é {menor}")
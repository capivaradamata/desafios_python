num1 = (input("Digite um numero:"))
num2 = (input("Digite outro:"))
num3 = (input("Digite mais um:"))
num4 = (input("Digite o último:"))
lista = (num1, num2 , num3 , num4)
print(f"Voce digitou os numeros {lista}")
contagem = 0
for nove in lista:
    if nove == 9 :
        contagem += 1
pos_tres = lista.index("3")
print(f"O numero 3 apareceu na posição {pos_tres +1}")
contagem_par = int(0)
for par in lista:
    num = int(par)
    if num % 2 == 0:
        contagem_par +=1
print(f"Foram digitados {contagem_par} numeros pares!")

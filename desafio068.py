from random import randint
print("Escolha par ou Impar")
contagem = 0
while True:
    dado = int(input("Par(1)""Impar(2):"))
    aleatorio = randint(1,20)
    if aleatorio%2 == 0 and  dado == 2:
        contagem += 1
        print(f"Parabens, você ganhou {contagem} Vezes")
    elif aleatorio%2 == 1 and dado == 1:
        contagem += 1
        print(f"Parabens, você ganhou {contagem} Vezes")
    else:break
print("Infelizmente voce perdeu")

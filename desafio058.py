from random import randint
count = 0
chute = 0
escolhido = randint(1,10)
while chute != escolhido:
    chute = int(input("Adivinhe o numero entre 0 e 10 escolhido pelo compuador:"))
    count = count + 1
    if chute != escolhido:
        print("Você errou, tente novamete")
print(f"Parabens, você acertou em {count} tentativas")
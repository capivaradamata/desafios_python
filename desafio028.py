import random
na = random.randint(0,5)
print("olá, irei pensar em um numero de 0 a 5, e você tem que adivinhar ele para ganhar de mim")
tentativa = int(input("Advinhe meu numero:"))
if na == tentativa:
    print(f"Parabens você acertou meu numero, e pensei no numero {na}!")
else:
    print("Infelizmente você não acertou, tente novamente!")
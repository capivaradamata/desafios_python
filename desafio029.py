velocidae = int(input("Qual era a velocidade de seu carro?"))
if velocidae > 80:
    print(f"Você estava a cima do limite permitido, sua multa sera de R${(float(velocidae - 80)* 7)}")
else:
    print("Parabens, você estava dirigindo dentro do limite de velocidade!")
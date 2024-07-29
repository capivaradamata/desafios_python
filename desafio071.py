import math
print("Bem vindo ao banco")
valor = int(input("Quanto deseja sacar?"))
while True:
    nota50 = int(math.floor(valor/50))
    nota20 = int(math.floor((valor%50)/20))
    nota10 = int(math.floor((valor%50)%20)/10)
    nota1 = int((((valor%50)%20)%10))
    break
print(f"Total de {nota50} cédulas de 50, Total de {nota20} céduals de 20, Total de {nota10} cédulas de 10, e total de {nota1} cédulas de 1")
print("Informe sua altura e peso para calcular seu IMC")
peso = float(input("Peso:"))
altura = float(input("altura:"))
IMC = peso/(altura*altura)
if IMC < 18.5:
    print("Você está abaixo do peso")
elif 18.5 <= IMC < 25:
    print("Você está no peso ideal")
elif 25 <= IMC < 30:
    print("Você está com sobrepeso")
elif 30 <= IMC < 40:
    print("Você está obeso")
elif IMC >= 40:
    print("Você está em obesidade morbida")
import math
print('Diga os catetos de um trianngulo para saber sua hipoetenusa')
cateto_1 = float(input('qual é o cateto oposto?'))
cateto_2 = float(input('qual é o cateto adjacente?'))
somacat = math.pow(cateto_1, 2) + math.pow(cateto_2, 2)
hipotenusa = math.sqrt(somacat)
print(f'A hipotenusa dos catetos é {hipotenusa}')
print(f'{math.cos(30)}')
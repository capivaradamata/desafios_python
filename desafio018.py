import math
print('Digite um angulo para saber seu seno, cosseno e tangente')
angulo = float(input('informe o angulo:'))
print(f'o valor de seno do angulo {math.trunc(angulo)} é {math.trunc(math.sin(angulo))}', end=', ')
print(f'o valor do cosseno do angulo {math.trunc(angulo)} é {math.trunc(math.cos(angulo))}', end=', ')
print(f'e o valor da tangente do angulo {math.trunc(angulo)} é {math.trunc(math.tan(angulo))}.')
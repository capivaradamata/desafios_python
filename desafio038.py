print('Digite 2 valores para saber qual é o maior')
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
if n1 > n2:
    print(f'o primeiro valor é o maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
elif n1 == n2: print('Os valores são iguais!')
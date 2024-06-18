ano = int(input('Qual ano você está?'))
if ano % 4 == 0 and ano != 100 or ano % 400 == 0:
    print('Seu ano é bissesto')
else: print('Seu ano não é bissesto')
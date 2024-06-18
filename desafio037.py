print('Converta seu numero para Binário, octal ou hexadecimal!')
numero = int(input('Digite o numero:'))
base = int(input('Para qual base você gostaria de converter? \ndigite 1 para Binário\nDigite 2 para octal\nDigite 3 para Hexadecimal \nQual opção'))
if base == 1:
    print(f'{bin(numero)[2:]} esse é o seu numero em Binário!')
elif base == 2:
    print(f'{oct(numero)[2:]} esse é seu numero em Octal')
elif base == 3:
    print(f'{hex(numero)[2:]} esse é seu numero em Hexadecimal')
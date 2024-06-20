print("Olá, informe 2 valores para poder realizar a operação desejada!")
va1 = int(input("Informe o primeiro numero:"))
va2 = int(input("Informe o segundo numero:"))
f = 0
while f != 5:
    op = int(input("Escolha qual opção você deseja: \n(1)somar \n(2)Multiplicar \n(3)Maior \n(4)Novos numeros \n(5)Sair do programa"))
    if op == 1:
        somado = va1 + va2
        print(f"O resultado é {somado}")
    elif op == 2:
        multiplicado = va1*va2
        print(f"O resultado é {multiplicado}")
    elif op ==3:
        if va2>va1:
            maior = va2
        else:maior = va1
        print(f"O resultado é {maior}")
    elif op == 4:
        print("informe novos numeros:")
        va1 = int(input("Informe o primeiro numero:"))
        va2 = int(input("Informe o segundo numero:"))
    elif op == 5:
        f = 5

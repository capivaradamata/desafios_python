print("informe os lados do tringulo para saber se é possivel formar e se possivel, a sua categoria")
lado1 = int(input("Lado 1:"))
lado2 = int(input("lado 2:"))
lado3 = int(input("lado 3:"))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print("é possivel formar essa triangulo")
    if lado1 == lado2 and lado1 == lado3:
        print("O triagulo é Equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triangulo é  Isoceles")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("O triangulo é Escaleno")
else:
    print("O trinangulo não é possivel")

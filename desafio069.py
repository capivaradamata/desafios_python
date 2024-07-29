sexo = ""
contidade = contsexo = contmu = 0
while True:
    print("CADASTRE A PESSOA")
    idade = int(input("Idade:"))
    if idade > 18:
        contidade += 1
    sexo = str(input("M/F:")).upper()
    if sexo == "M":
        contsexo += 1
    if idade < 20 and sexo == "F":
        contmu += 1
    while True:
        if sexo != "M" and sexo != "F" :
            sexo = str(input("M/F:")).upper()
            if sexo == "M":
                contsexo += 1
            if idade < 20 and sexo == "F":
                contmu += 1
        else:break
    cont = str(input("Quer continuar?(S/N)")).upper()
    while True:
        if cont != "S" and cont != "N":
            cont = str(input("Quer continuar?(S/N)")).upper()
        else: break
    if cont == "N":
        break
print(f"O total de pessoas com mais de 18 anos é {contidade}, o total de homens é {contsexo}, o total de mulheres com menos de 20 é {contmu}")
print("Será requisitado Nome, Idade e Sexo")
velho = 0
contagem = 0
nome_do_velho = ''
total_idade = 0
cot = 0
sexo = ''
for c in range(0,4,1):
    nome = str(input("Informe o nome:"))
    idade = int(input("Informe a idade:"))
    total_idade = idade + total_idade
    cot = cot + 1
    sexonum = int(input("Digite o numero para escolher o seu sexo \n 1)Masculino \n 2)Feminino \n:"))
    if  sexonum == 1:
        sexo = "Masculino"
    else:
        sexo = "Feminino"
    if sexo == "Masculino" and velho < idade:
        nome_do_velho = nome
        velho = idade
    print(velho)
    if  idade < 20 and sexo ==  "Feminino":
            contagem =+ 1
print(f"A media de idade de idade do grupo é {total_idade/cot}!\nO homem mais velho é {nome_do_velho}!\nHá {contagem} mulheres com menos de 20 anos!")

sexo = ""
while sexo != "F" and sexo != "M" :
    sexo = str.upper(input("Informe seu sexo conforme o exemplo, digite F ou M :"))
    if sexo != "F" and sexo != "M":
        print("Voce digitou errado, tente novamente!")
print("Obrigado por informar")
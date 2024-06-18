print("Informe suas notas para saber seu atual estado de matéria")
nota1 = float(input("Nota de sua Primeira Prova:"))
nota2 = float(input("Nota de sua Segunda Prova:"))
media = (nota1 + nota2)/2
if  media < 5:
    print("Você está reprovado")
elif 5 <= media <7:
    print("Você está de recuperação")
elif media >= 7:
    print("Você está aprovado")
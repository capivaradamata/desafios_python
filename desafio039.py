import datetime
data = datetime.date.today().year
nascimento = int(input('Qual o ano de seu nascimento:'))
idade = data - nascimento
if idade < 18:
    print(f'Ainda não está em tempo de alistamento, mas em {(18 - idade)} anos será a data de seu alistamento')
elif idade > 18:
    print(f"Já passou sua idade de alistamento em {idade - 18} anos, regularize sua situação")
elif idade == 18:
    print("Está em ano de alistamento, vá a uma junta militar")

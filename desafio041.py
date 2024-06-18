from datetime import date
print("informe seu ano de nascimento para saber sua categoria")
nascimento = int(input("Informe o ano de nascimento:"))
data = date.today().year
idade = data - nascimento
if idade < 9:
    print("Você é da classificação Mirim")
elif 9 <= idade < 14:
    print("Você é da classificação infantil")
elif 14 <= idade < 19:
    print("Você é da classificação Junior")
elif 19<= idade < 20:
    print("Você é da classificação Senior")
elif idade >= 20:
    print("Você é da classificação master")

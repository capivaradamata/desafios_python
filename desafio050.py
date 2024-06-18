print("Digite 6 numeros inteiros e sera somado aqueles que são pares!")
nun1 = int(input("Numero 1:"))
nun2 = int(input("Numero 2:"))
nun3 = int(input("Numero 3:"))
nun4 = int(input("Numero 4:"))
nun5 = int(input("Numero 5:"))
nun6 = int(input("Numero 6:"))
total = 0
for c in [nun1, nun2, nun3, nun4, nun5, nun6]:
    if c % 2 == 0:
        total = total + c
print(f'A soma dos numeros pares é {total}')
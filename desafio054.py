print("você informara a idade de 7 pessoas para saber se são maiores de idade")
tot = 0
for c in range(0,7):
    idade = int(input("Diga a idade para saber se é maior de idade:"))
    if idade > 21:
        tot += 1
print(f"Há {tot} pessoas mairoes de idade")
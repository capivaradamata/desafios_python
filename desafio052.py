nun = int(input("Digite um numero par saber se é primo:"))
tot = 0
for c in range(1, nun + 1):
    if nun % c == 0:
        tot += 1
if tot == 2:
    print(f'{nun} é um numero primo')
else:
    print(f"{nun} não é um numero primo")

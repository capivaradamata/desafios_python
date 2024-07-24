n1 = 0
n2 = 1
quantidade = int(input("Qual a quantidade de numeros da sequência quer saber?"))
print(f"{n1}-{n2}", end="-")
while quantidade != 0:
    quantidade -= 1
    if n2==1:
        n = n1 + n2
    else: n = n + n2
    print(n, end="-")
    n2 = n + n2
    print(n2, end="-")
termo = int(input("Qual o primeiro termo das Progressão aritimética:"))
razão = int(input("Qual a razão dessa Progressão:"))
aba = []
for c in range(0,10):
    aba.append(termo + (razão * c))
print(f"Os 10 primeiros termos são {aba}")

print("Digite os numeros que deseja saber as soma")
print("Digite 999 para parar de somar")
end = 0
total = 0
while end != 1:
    soma = int(input("Digite o numero para adicionalo a soma:"))
    total += soma
    if  soma == 999:
        end = 1
        total += -999
        print(f"O total da soma é {total}")

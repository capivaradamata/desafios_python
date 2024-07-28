print("Informe os numeros que deseja somar")
resultado = soma = contagem = 0
while True:
    soma = int(input("Informe o numero:"))
    if soma == 999:
        break
    else:resultado += + soma
    contagem += 1
print(f"Você somou {contagem} numeros, e a sma foi {resultado}")

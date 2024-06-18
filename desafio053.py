frase = str(input("Digite uma frase para saber se é palindromo:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if junto == inverso:
    print(f" A frase {frase} é um palindromo")
else:
    print(f"A frase {frase} não é um palindromo")
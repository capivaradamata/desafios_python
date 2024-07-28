contagem = 0
while True:
    dado = int(input("Qual tabuada você deseja saber?"))
    if dado < 0:
        break
    contagem = 0
    while True:
        contagem += 1
        if contagem == 11:
            break
        else: print(f"1 * {dado} = {dado*contagem}")

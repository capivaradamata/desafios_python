from random import choice
print("esse é um jogo de jokenpô")
jogador = int(input("qual é a sua jogada \nPedra(1) \nPapel(2) \nTesoura(3) \n:"))
jogadas = ["Pedra", "Papel", "Tesoura"]
maquina = choice(jogadas)
if jogador == 1 and maquina == "Papel":
    print(f"Você perdeu, a maquina tirou {maquina}")
elif jogador ==1 and maquina == "Tesoura":
    print(f"Você ganhou, a maquina tirou {maquina}")
elif jogador ==2 and maquina == "Pedra":
    print(f"Você ganhou, a maquina tirou {maquina}")
elif jogador ==2 and maquina == "Tesoura":
    print(f"Você perdeu, a maquina tirou {maquina}")
elif jogador ==3 and maquina == "Pedra":
    print(f"Você perdeu, a maquina tirou {maquina}")
elif jogador ==3 and maquina == "Papel":
    print(f"Você ganhou, a maquina tirou {maquina}")
else:
    print(f"Você empatou, a maquina tiorou {maquina}, logo o mesmo que você")
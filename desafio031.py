distancia = float(input("Qual a distancia da sua viagem?"))
if  distancia <= 200:
    print(f'{distancia * 0.5}R$ será o custo da passagem')
else: print(f'{distancia * 0.45}R$ seráo valor da da passagem')